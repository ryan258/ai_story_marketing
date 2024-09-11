# 📁 File: ai_story_marketing/tests/test_gpt4_model.py

import pytest
from unittest.mock import patch
from ai_story_marketing.models.gpt4_model import GPT4Model
import os
from dotenv import load_dotenv
import re


# Load environment variables from .env file
load_dotenv()

# 🧪 Test suite for the GPT4Model

def test_gpt4_model_initialization():
    """
    Test if the GPT4Model initializes correctly with environment variables.
    """
    # 🏗️ Create a GPT4Model instance
    gpt4 = GPT4Model()
    
    # 🔍 Check if the API key and model name are set correctly
    assert gpt4.api_key == os.getenv('OPENAI_API_KEY'), "API key should be set from environment variable"
    assert gpt4.model_name == os.getenv('OPENAI_MODEL_NAME'), "Model name should be set from environment variable"

def test_gpt4_model_initialization_no_api_key():
    """
    Test if the GPT4Model raises an error when no API key is provided.
    """
    # 🚫 Temporarily remove the API key from environment
    with patch.dict(os.environ, {'OPENAI_API_KEY': ''}):
        # 🧪 Check if ValueError is raised when creating GPT4Model without API key
        with pytest.raises(ValueError, match=re.escape("Oops! We can't find the secret code (API key) to talk to GPT-4. 😕")):
            GPT4Model()

def test_gpt4_model_generate_success():
    """
    Test if the GPT4Model can successfully generate a story.
    This test uses the actual API key and model name from .env file.
    """
    # 🏗️ Create a GPT4Model instance
    gpt4 = GPT4Model()
    
    # 💡 Provide a story idea
    story_idea = "A brave little robot goes on an adventure in a magical forest"
    
    # 📝 Generate the story
    result = gpt4.generate(story_idea)
    
    # 🔍 Check if we got a non-empty story
    assert result is not None and result.strip() != "", "GPT-4 should generate a non-empty story"
    
    # 📏 Check if the generated story is of reasonable length (e.g., at least 100 characters)
    assert len(result) >= 100, "Generated story should be of reasonable length"
    
    # 🧠 Check if the generated story includes elements from the original idea
    assert "robot" in result.lower() or "adventure" in result.lower() or "forest" in result.lower(), \
        "Generated story should include elements from the original idea"

def test_gpt4_model_generate_failure():
    """
    Test how the GPT4Model handles API errors.
    """
    # 🏗️ Create a GPT4Model instance
    gpt4 = GPT4Model()
    
    # 🚫 Simulate an API error by temporarily setting an invalid API key
    with patch('openai.OpenAI') as mock_openai:
        mock_openai.return_value.chat.completions.create.side_effect = Exception("API Error")
        gpt4 = GPT4Model()

        # 💡 Provide a story idea
        story_idea = "A brave little robot goes on an adventure"
        
        # 📝 Attempt to generate the story
        result = gpt4.generate(story_idea)
        
        # 🔍 Check if the result is None, indicating an error occurred
        assert result is None, "GPT4Model should return None when an API error occurs"

# 🏃‍♂️ Run the tests
if __name__ == "__main__":
    pytest.main(['-v', __file__])

# 🎉 Hooray! We've created comprehensive tests for our GPT4Model!
# These tests ensure our model initializes correctly, generates stories successfully,
# and handles errors appropriately. 🚀