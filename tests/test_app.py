# 📁 File: ai_story_marketing/tests/test_app.py

import pytest
from ai_story_marketing.app import app, story_improver, evaluator  # Import your Flask app
from flask import session
import logging
from unittest.mock import patch, MagicMock

# Set up logging for tests
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# 🧪 This is our test setup. It runs before each test.
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# 🏠 Test if the home page loads correctly
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200  # 200 means the page loaded OK
    assert b"Story Creator" in response.data  # Check if our title is in the page

# 💡 Test submitting a story idea
def test_submit_idea(client):
    # Mock the StoryWriter and Evaluator to avoid calling the actual AI model
    with patch('ai_story_marketing.app.story_writer.process') as mock_story_writer, \
         patch('ai_story_marketing.app.evaluator.process') as mock_evaluator:
        
        mock_story_writer.return_value = "Once upon a time..."
        mock_evaluator.return_value = {"score": 8, "feedback": "Great story!"}
        
        response = client.post('/', data={'idea': 'A magical forest'})
        assert response.status_code == 200
        data = response.get_json()
        assert 'next' in data
        assert data['next'] == '/evaluate'
        
        # Check if the session was updated correctly
        with client.session_transaction() as sess:
            assert 'story' in sess
            assert 'evaluation' in sess
            assert 'progress' in sess
            assert 'story_creation' in sess['progress']
            assert 'evaluation' in sess['progress']

# 🚫 Test submitting an empty idea
def test_submit_empty_idea(client):
    response = client.post('/', data={'idea': ''})
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data
    assert "We need an idea to make a story!" in data['error']

# 📊 Test the evaluate page
def test_evaluate_page(client):
    with client.session_transaction() as sess:
        sess['story'] = "Once upon a time in a magical forest..."
        sess['evaluation'] = {'score': 8, 'feedback': "Great story!"}
    response = client.get('/evaluate')
    assert response.status_code == 200
    assert b"Your Amazing Story" in response.data

# 🧪 Test the continue action on the evaluate page
def test_evaluate_continue(client):
    with client.session_transaction() as sess:
        sess['story'] = "Once upon a time..."
        sess['evaluation'] = {'score': 8, 'feedback': "Great story!"}
    
    response = client.post('/evaluate', json={'choice': 'continue'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert data['next'] == '/market'

# 🧪 Test the rewrite action on the evaluate page
def test_evaluate_rewrite(client):
    with client.session_transaction() as sess:
        sess['story'] = "Once upon a time..."
        sess['evaluation'] = {'score': 8, 'feedback': "Great story!"}
        sess['progress'] = ['story_creation', 'evaluation']
    
    response = client.post('/evaluate', json={'choice': 'rewrite'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert data['next'] == '/'
    
    with client.session_transaction() as sess:
        assert 'story' not in sess
        assert 'evaluation' not in sess
        assert sess['progress'] == []

# 🧪 Test the improve story action
@patch('ai_story_marketing.app.story_improver.process')
@patch('ai_story_marketing.app.evaluator.process')
def test_improve_story(mock_evaluator, mock_improver, client):
    mock_improver.return_value = "Once upon a time, in a magical forest..."
    mock_evaluator.return_value = {'score': 9, 'feedback': "Even better!"}
    
    with client.session_transaction() as sess:
        sess['story'] = "There was a rabbit named Hoppy."
        sess['evaluation'] = {'score': 7, 'feedback': "Needs more detail."}
    
    response = client.post('/improve_story', json={})
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert data['next'] == '/evaluate'
    
    with client.session_transaction() as sess:
        assert sess['story'] == "Once upon a time, in a magical forest..."
        assert sess['evaluation']['score'] == 9
        assert 'story_improvement' in sess['progress']

# 🧪 Test improve story with missing data
def test_improve_story_missing_data(client):
    response = client.post('/improve_story', json={})
    assert response.status_code == 200
    assert response.get_json()['error'] == "Oops! We lost your story or evaluation. Let's start over!"


# 🧪 Test the improve_story route
def test_improve_story(client):
    with client.session_transaction() as sess:
        sess['story'] = "There was a rabbit named Hoppy."
        sess['evaluation'] = {
            'score': 6,
            'feedback': "Add more details about the setting and make the rabbit braver."
        }
    
    # Mock the StoryImprover and Evaluator
    with patch('ai_story_marketing.app.story_improver.process') as mock_improver, \
         patch('ai_story_marketing.app.evaluator.process') as mock_evaluator:
        
        mock_improver.return_value = "In a lush forest, there was a brave rabbit named Hoppy..."
        mock_evaluator.return_value = {"score": 8, "feedback": "Much better!"}
        
        response = client.post('/improve_story')
        assert response.status_code == 200
        data = response.get_json()
        assert 'message' in data
        assert 'next' in data
        assert data['next'] == '/evaluate'

        with client.session_transaction() as sess:
            assert 'story' in sess
            assert sess['story'] != "There was a rabbit named Hoppy."  # The story should have changed
            assert 'evaluation' in sess
            assert sess['evaluation']['score'] == 8  # The score should have changed

# 🎭 Test the market page
def test_market_page(client):
    with client.session_transaction() as sess:
        sess['story'] = "Once upon a time in a magical forest..."
    
    # Mock the marketing-related functions
    with patch('ai_story_marketing.app.marketing_expert.process') as mock_marketing, \
         patch('ai_story_marketing.app.social_media_team.process') as mock_social, \
         patch('ai_story_marketing.app.marketing_team.process') as mock_marketing_team:
        
        mock_marketing.return_value = {
            "target_audience": "Young readers",
            "personas": ["Curious Kid", "Adventure Lover"]
        }
        mock_social.return_value = {"Twitter": "Check out this magical story!"}
        mock_marketing_team.return_value = {"poster": "A colorful forest scene"}
        
        response = client.get('/market')
        assert response.status_code == 200
        assert b"Marketing Magic" in response.data
        
        # Check if the session was updated correctly
        with client.session_transaction() as sess:
            assert 'marketing_analysis' in sess
            assert 'social_media_content' in sess
            assert 'marketing_concepts' in sess
            assert 'progress' in sess
            assert 'marketing_analysis' in sess['progress']
            assert 'social_media' in sess['progress']
            assert 'marketing_concepts' in sess['progress']

# 🎉 Test the result page
def test_result_page(client):
    with client.session_transaction() as sess:
        sess['story'] = "Once upon a time in a magical forest..."
        sess['evaluation'] = {'score': 8, 'feedback': "Great story!"}
        sess['marketing_analysis'] = {'target_audience': "Children", 'personas': ["Curious Kid"]}
        sess['social_media_content'] = {'Twitter': "Check out this magical story!"}
        sess['marketing_concepts'] = {'poster': "A colorful forest scene"}
    response = client.get('/result')
    assert response.status_code == 200
    assert b"Your Amazing Story and Marketing Plan" in response.data

# 📄 Test the PDF download route
@patch('ai_story_marketing.app.PDFGenerator')
def test_download_pdf(MockPDFGenerator, client):
    mock_pdf_generator = MockPDFGenerator.return_value
    mock_pdf_generator.generate_pdf.return_value = True
    
    with client.session_transaction() as sess:
        sess['story'] = "Once upon a time..."
        sess['evaluation'] = {'score': 8, 'feedback': "Great!"}
        sess['marketing_analysis'] = {'target_audience': "Kids", 'personas': ["Curious Child"]}
        sess['social_media_content'] = {'Twitter': "Check this out!"}
        sess['marketing_concepts'] = {'poster': "Colorful scene"}
    
    response = client.get('/download-pdf')

    if response.status_code == 200:
        assert response.headers['Content-Type'] == 'application/pdf'
        assert response.headers['Content-Disposition'] == 'attachment; filename=your_story_package.pdf'
    elif response.status_code == 302:
        # If there's a redirect, it should be to the result page
        assert response.location.endswith('/result')
    else:
        pytest.fail(f"Unexpected status code: {response.status_code}")

# 🐛 Test error handling
def test_error_handling(client):
    # Test submitting an empty idea
    response = client.post('/', data={'idea': ''})
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data
    
    # Test accessing evaluate page without a story
    response = client.get('/evaluate')
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data
    assert data['next'] == '/'
    
    # Test accessing market page without a story
    response = client.get('/market')
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data
    assert data['next'] == '/'
    
    # Test accessing result page without all required data
    response = client.get('/result')
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data
    assert data['next'] == '/'

print("🎉 Yay! We've written comprehensive tests for our Story Creator app!")