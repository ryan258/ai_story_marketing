# 📁 File: ai_story_marketing/tests/test_story_improver.py

import pytest
from unittest.mock import MagicMock
from ai_story_marketing.agents.story_improver import StoryImprover

# 🧪 Welcome to the StoryImprover Test file! 🚀
# Here, we're going to make sure our StoryImprover agent is working properly!

def test_story_improver_initialization():
    # 🏗️ Let's make sure we can create our StoryImprover
    mock_model = MagicMock()
    improver = StoryImprover(mock_model)
    assert improver is not None, "StoryImprover should be created successfully"

def test_story_improver_process():
    # 🔍 Let's test if our StoryImprover can improve a story correctly
    mock_model = MagicMock()
    mock_model.generate.return_value = "Once upon a time, in a magical forest full of talking animals, there lived a brave little rabbit named Hoppy who loved to go on adventures..."
    
    improver = StoryImprover(mock_model)
    
    original_story = "There was a rabbit named Hoppy."
    feedback = "Add more details about the setting and make the rabbit braver."
    
    improved_story = improver.process(original_story, feedback)
    
    assert "magical forest" in improved_story, "Improved story should include new details about the setting"
    assert "brave little rabbit" in improved_story, "Improved story should make the rabbit braver"
    assert "adventures" in improved_story, "Improved story should add new elements based on the feedback"

def test_story_improver_empty_response():
    # 😴 Let's test what happens if our AI returns an empty response
    mock_model = MagicMock()
    mock_model.generate.return_value = ""
    
    improver = StoryImprover(mock_model)
    
    original_story = "There was a rabbit named Hoppy."
    feedback = "Add more details."
    
    improved_story = improver.process(original_story, feedback)
    
    assert "remains unchanged" in improved_story, "Should return a message indicating the story wasn't changed"

def test_story_improver_exception_handling():
    # 🐛 Let's test how our StoryImprover handles exceptions
    mock_model = MagicMock()
    mock_model.generate.side_effect = Exception("Oops! Something went wrong.")
    
    improver = StoryImprover(mock_model)
    
    original_story = "There was a rabbit named Hoppy."
    feedback = "Add more details."
    
    improved_story = improver.process(original_story, feedback)
    
    assert "remains unchanged" in improved_story, "Should return a message indicating the story wasn't changed due to an error"

# 🏃‍♂️ This is where we run all our tests!
if __name__ == "__main__":
    pytest.main()

# 🎉 Hooray! We've created tests for our StoryImprover agent!
# Now we can be sure it's working correctly! 🚀