# 📁 File: ai_story_marketing/ai_story_marketing/agents/story_writer.py

# 📚 Welcome to the StoryWriter agent! 🖋️
# This magical agent will help us create amazing stories! 🧙‍♂️

from .base_agent import BaseAgent  # We're using the superhero costume we made earlier!

class StoryWriter(BaseAgent):
    """
    🖋️ This is our StoryWriter agent.
    It's like a friendly robot that loves to write stories!
    """

    def __init__(self, model):
        """
        🎭 This is where we set up our StoryWriter with its story-writing superpowers!
        
        Args:
            model: The AI model that gives our StoryWriter its creativity
        """
        super().__init__(model)  # We're using the setup from our BaseAgent
        self.story = ""  # This is where we'll keep our story

    def process(self, idea):
        """
        📝 This is where the magic happens! Our StoryWriter takes an idea and turns it into a story.
        
        Args:
            idea (str): The main idea or prompt for our story
        
        Returns:
            str: The completed story
        """
        # Let's create a prompt for our AI to write the story
        prompt = self.format_prompt(
            "Write a short story based on this idea: {idea}. "
            "The story should have a beginning, middle, and end. "
            "Make it exciting and fun to read!",
            idea=idea
        )
        
        # Now, let's ask our AI to write the story
        self.story = self.generate_text(prompt)
        
        # Let's remember this story in our magical backpack (context)
        self.update_context({"latest_story": self.story})
        
        return self.story

    def get_story(self):
        """
        📖 This lets us read the story our StoryWriter has created.
        
        Returns:
            str: The current story
        """
        return self.story

# 🧪 Let's add some tests to make sure our StoryWriter works correctly
def test_story_writer():
    # 🤖 Create a pretend AI model for testing
    class DummyModel:
        def generate(self, prompt):
            return f"Once upon a time... {prompt}"
    
    # 🦸‍♂️ Create our StoryWriter agent
    writer = StoryWriter(DummyModel())
    
    # 📝 Test writing a story
    idea = "a brave little mouse"
    story = writer.process(idea)
    assert "Once upon a time" in story, "Story should start with 'Once upon a time'"
    assert "brave little mouse" in story, "Story should include the original idea"
    
    # 📚 Test getting the story
    assert writer.get_story() == story, "get_story should return the latest story"
    
    # 🧠 Test that the story is saved in the context
    assert writer.get_context()["latest_story"] == story, "Story should be saved in context"

# 🎉 Hooray! We've created our StoryWriter agent!
# Now we can create amazing stories with the power of AI! 🚀