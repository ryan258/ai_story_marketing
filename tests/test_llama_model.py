# 📁 File: ai_story_marketing/tests/test_llama_model.py

# 🧪 Welcome to the Llama Model Test file! 🦙
# Here, we're going to make sure our Llama friend is working properly!

import pytest
from unittest.mock import patch, Mock
from ai_story_marketing.models.llama_model import LlamaModel

# 🎭 This is a pretend version of our Llama friend for testing
@pytest.fixture
def mock_llama_response():
    return {
        "response": "Once upon a time, there was a brave little mouse named Squeaky..."
    }

# 🔍 Let's test if our LlamaModel is set up correctly
def test_llama_model_initialization():
    # 🏗️ We're creating our Llama telephone
    llama = LlamaModel()
    
    # 🕵️‍♂️ Let's check if our Llama telephone has the right information
    assert llama.api_url is not None, "Oops! We forgot the address of our Llama friend!"
    assert llama.model_name is not None, "Oh no! We forgot our Llama friend's name!"

# 📞 Let's test if we can talk to our Llama friend successfully
@patch('requests.post')
def test_llama_model_generate_success(mock_post, mock_llama_response):
    # 🎭 We're pretending to talk to our Llama friend
    mock_post.return_value.json.return_value = mock_llama_response
    mock_post.return_value.raise_for_status.return_value = None
    
    llama = LlamaModel()
    story_idea = "A brave little mouse goes on an adventure"
    
    # 📝 Let's ask our pretend Llama to write a story
    result = llama.generate(story_idea)
    
    # 🧐 Let's check if we got a story back
    assert result == mock_llama_response["response"], "Oh no! Our Llama friend didn't give us the story we expected!"
    
    # 🕵️‍♂️ Let's make sure we called our Llama friend correctly
    mock_post.assert_called_once()
    args, kwargs = mock_post.call_args
    assert kwargs['json']['prompt'] == story_idea, "Oops! We didn't send the right story idea to our Llama friend!"

# 😟 Let's test what happens if we can't reach our Llama friend
@patch('requests.post')
def test_llama_model_generate_failure(mock_post):
    # 🎭 We're pretending that we can't reach our Llama friend
    mock_post.side_effect = Exception("Oh no! We can't reach our Llama friend!")
    
    llama = LlamaModel()
    story_idea = "A brave little mouse goes on an adventure"
    
    # 📝 Let's try to ask our Llama to write a story
    result = llama.generate(story_idea)
    
    # 🧐 Let's check if we got None when we couldn't reach our Llama
    assert result is None, "Uh-oh! We should get None when we can't talk to our Llama friend!"

# 🏃‍♂️ This is where we run all our tests!
if __name__ == "__main__":
    pytest.main()