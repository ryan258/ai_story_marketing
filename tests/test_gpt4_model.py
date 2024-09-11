# 📁 File: ai_story_marketing/tests/test_gpt4_model.py

import pytest
from unittest.mock import patch, MagicMock
from ai_story_marketing.models.gpt4_model import GPT4Model

@pytest.fixture
def mock_openai_response():
    return MagicMock(choices=[MagicMock(message=MagicMock(content="Once upon a time, there was a brave little robot..."))])

def test_gpt4_model_initialization():
    with patch('os.getenv') as mock_getenv:
        mock_getenv.side_effect = ['fake-api-key', 'fake-model-name']
        gpt4 = GPT4Model()
    
    assert gpt4.api_key == 'fake-api-key', "Oops! We didn't get the right API key!"
    assert gpt4.model_name == 'fake-model-name', "Oh no! We forgot our GPT-4 friend's name!"

def test_gpt4_model_initialization_no_api_key():
    with patch('os.getenv') as mock_getenv:
        mock_getenv.return_value = None
        
        with pytest.raises(ValueError):
            GPT4Model()

@patch('openai.OpenAI')
def test_gpt4_model_generate_success(mock_openai, mock_openai_response):
    mock_openai.return_value.chat.completions.create.return_value = mock_openai_response
    
    with patch('os.getenv') as mock_getenv:
        mock_getenv.side_effect = ['fake-api-key', 'fake-model-name']
        gpt4 = GPT4Model()
    
    story_idea = "A brave little robot goes on an adventure"
    
    result = gpt4.generate(story_idea)
    
    assert result == "Once upon a time, there was a brave little robot...", "Oh no! Our GPT-4 friend didn't give us the story we expected!"
    
    mock_openai.return_value.chat.completions.create.assert_called_once_with(
        model='fake-model-name',
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes creative stories."},
            {"role": "user", "content": story_idea}
        ],
        max_tokens=1000
    )

@patch('openai.OpenAI')
def test_gpt4_model_generate_failure(mock_openai):
    mock_openai.return_value.chat.completions.create.side_effect = Exception("Oh no! We can't reach our GPT-4 friend!")
    
    with patch('os.getenv') as mock_getenv:
        mock_getenv.side_effect = ['fake-api-key', 'fake-model-name']
        gpt4 = GPT4Model()
    
    story_idea = "A brave little robot goes on an adventure"
    
    result = gpt4.generate(story_idea)
    
    assert result is None, "Uh-oh! We should get None when we can't talk to our GPT-4 friend!"

if __name__ == "__main__":
    pytest.main()