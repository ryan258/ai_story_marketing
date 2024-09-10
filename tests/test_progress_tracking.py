# 📁 File: ai_story_marketing/tests/test_progress_tracking.py

import pytest
from flask import session
from ai_story_marketing.app import app, track_progress

# 🧪 Welcome to our test file for progress tracking! 🚀
# Here, we'll make sure our progress tracking works perfectly!

@pytest.fixture
def client():
    # 🛠️ This is our test setup. It helps us pretend to use our app!
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_track_progress(client):
    # 🏃‍♂️ Let's test if our progress tracking works!
    
    # First, let's track some progress
    with client.session_transaction() as sess:
        track_progress(sess, 'story_creation')
    
    # Now, let's check if it worked
    with client.session_transaction() as sess:
        assert 'progress' in sess
        assert sess['progress'] == ['story_creation']
    
    # Let's track another step
    with client.session_transaction() as sess:
        track_progress(sess, 'evaluation')
    
    # And check again
    with client.session_transaction() as sess:
        assert 'progress' in sess
        assert sess['progress'] == ['story_creation', 'evaluation']

def test_progress_in_templates(client):
    # 🖼️ Let's make sure our progress shows up in our evaluate page!
    
    # First, let's add some progress
    with client.session_transaction() as sess:
        sess['progress'] = ['story_creation', 'evaluation']
        sess['story'] = "Once upon a time..."
        sess['evaluation'] = {"score": 8, "feedback": "Great story!"}
    
    # Now, let's check our evaluate page
    response = client.get('/evaluate')
    assert b'Story Creation' in response.data
    assert b'Evaluation' in response.data

# 🎉 Hooray! We've written tests for our progress tracking!
# Now we can make sure it always works correctly! 🚀