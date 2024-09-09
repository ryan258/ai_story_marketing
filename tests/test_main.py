# 📁 File: ai_story_marketing/tests/test_main.py

# 🧪 Welcome to our test lab! 🔬
# This is where we make sure our main application is working perfectly!

import pytest
from ai_story_marketing.main import create_app

def test_create_app():
    """
    🏗️ Test if our app is created successfully and responds correctly
    """
    # Create a test version of our app
    app = create_app()
    
    # Check if our app was created successfully
    assert app is not None, "App should be created"
    
    # Use a test client to check if our routes work
    with app.test_client() as client:
        # Test the home page
        response = client.get('/')
        assert response.status_code == 200, "Homepage should be accessible"
        
        # Test submitting an idea
        response = client.post('/', data={'idea': 'A story about a magical tree'})
        assert response.status_code == 200, "Should accept idea submission"
        
        # Check if the response is in JSON format
        assert response.is_json, "Response should be in JSON format"
        
        # Check the response content
        results = response.get_json()
        print(f"Response content: {results}")  # Let's see what we're getting back
        
        if 'error' in results:
            pytest.fail(f"Error in response: {results['error']}")
        else:
            expected_keys = ['story', 'evaluation', 'marketing_analysis', 'social_media_content', 'marketing_concepts']
            for key in expected_keys:
                assert key in results, f"Response should include {key}"

def test_error_handling():
    """
    🦸‍♂️ Test if our error handling works correctly
    """
    app = create_app()
    
    with app.test_client() as client:
        # Test with an empty idea (should trigger an error)
        response = client.post('/', data={'idea': ''})
        assert response.status_code == 200, "Should handle errors gracefully"
        
        results = response.get_json()
        assert 'error' in results, "Should return an error message for invalid input"
        print(f"Error message for empty idea: {results['error']}")  # Let's see the error message

# 🎉 Hooray! We've updated our tests to give us more information!
# Now we can better understand what's happening when we run our tests! 🚀