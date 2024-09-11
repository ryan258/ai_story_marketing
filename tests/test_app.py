# 📁 File: ai_story_marketing/tests/test_app.py

import pytest
from ai_story_marketing.app import app  # Import your Flask app
from flask import session
import logging

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
    response = client.post('/', data={'idea': 'A magical forest'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'next' in data
    assert data['next'] == '/evaluate'

# 📊 Test the evaluate page
def test_evaluate_page(client):
    with client.session_transaction() as sess:
        sess['story'] = "Once upon a time in a magical forest..."
        sess['evaluation'] = {'score': 8, 'feedback': "Great story!"}
    response = client.get('/evaluate')
    assert response.status_code == 200
    assert b"Your Amazing Story" in response.data

# 🧪 This is our test for the new improve_story route
def test_improve_story(client):
    with client.session_transaction() as sess:
        sess['story'] = "There was a rabbit named Hoppy."
        sess['evaluation'] = {
            'score': 6,
            'feedback': "Add more details about the setting and make the rabbit braver."
        }
    
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
        assert sess['evaluation']['score'] != 6  # The score should have changed

# 🧪 This is our updated test for the integration of story improvement in the evaluate route
def test_evaluate_with_improvement(client):
    with client.session_transaction() as sess:
        original_story = "There was a rabbit named Hoppy."
        sess['story'] = original_story
        sess['evaluation'] = {
            'score': 6,
            'feedback': "Add more details about the setting and make the rabbit braver."
        }
    
    # Improve the story
    response = client.post('/improve_story')
    assert response.status_code == 200
    logger.debug(f"Improve story response: {response.get_json()}")

    # Check the evaluate page
    response = client.get('/evaluate')
    assert response.status_code == 200
    content = response.data.decode('utf-8')
    logger.debug(f"Evaluate page content: {content[:500]}...")  # Log first 500 characters

    assert "Apply Improvements" in content

    # Check if the story has been changed
    with client.session_transaction() as sess:
        improved_story = sess.get('story', '')
        logger.debug(f"Original story: {original_story}")
        logger.debug(f"Improved story: {improved_story[:100]}...")  # Log first 100 characters
        assert improved_story != original_story, "The story should have been improved"
    
    # Check if the improved story is in the page content
    assert improved_story in content, "The improved story should be displayed on the page"

    # Check if a new evaluation is present
    assert "Score:" in content
    with client.session_transaction() as sess:
        new_evaluation = sess.get('evaluation', {})
        logger.debug(f"New evaluation: {new_evaluation}")
        assert 'score' in new_evaluation, "There should be a new evaluation score"
        assert 'feedback' in new_evaluation, "There should be new evaluation feedback"

# 🧪 This is our test for error handling in the improve_story route
def test_improve_story_error_handling(client):
    # Test without a story in the session
    response = client.post('/improve_story')
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data
    assert data['next'] == '/'

    # Test with a story but without an evaluation
    with client.session_transaction() as sess:
        sess['story'] = "There was a rabbit named Hoppy."
    
    response = client.post('/improve_story')
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data
    assert data['next'] == '/'

# 🎭 Test the market page
def test_market_page(client):
    with client.session_transaction() as sess:
        sess['story'] = "Once upon a time in a magical forest..."
    response = client.get('/market')
    assert response.status_code == 200
    assert b"Marketing Magic" in response.data

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

# 🐛 Test error handling
def test_error_handling(client):
    response = client.post('/', data={'idea': ''})  # Submit an empty idea
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data

print("🎉 Yay! We've written tests for our Story Creator app!")