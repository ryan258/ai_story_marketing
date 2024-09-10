# 📁 File: ai_story_marketing/tests/test_app.py

import pytest
from ai_story_marketing.app import app  # Import your Flask app
from flask import session

# 🧪 This is our test setup. It runs before each test.
@pytest.fixture
def client():
    app.config['TESTING'] = True  # This tells Flask we're testing
    app.config['SECRET_KEY'] = 'test_secret_key'  # We need this for sessions to work in tests
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