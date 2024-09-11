# 📁 File: ai_story_marketing/ai_story_marketing/agents/story_writer.py

# 🧙‍♂️ Welcome to the StoryWriter agent! 📚
# This magical agent turns ideas into amazing stories and helps improve them! ✨

# First, let's import what we need
from .base_agent import BaseAgent  # We're using the basic structure from BaseAgent
import logging  # This helps us keep track of what's happening

# Set up our magical storytelling log 📜✨
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StoryWriter(BaseAgent):
    """
    🧙‍♂️ Our magical StoryWriter! It turns ideas into amazing stories!
    """

    def __init__(self, model):
        """
        🎭 Getting our storyteller ready with a magical AI brain!
        
        Args:
            model: The AI model that gives our StoryWriter its creativity
        """
        super().__init__(model)  # We're using the setup from our BaseAgent
        self.story = ""  # This is where we'll keep our story

    def process(self, idea):
        """
        📝 This is where the magic happens! We turn an idea into a story!
        
        Args:
            idea (str): The story idea to write about
        
        Returns:
            str: The created story
        """
        logger.info(f"🌟 Starting to write a story about: {idea}")

        # Let's create a prompt for our AI to write the story
        prompt = self.format_prompt(
            "Write a short, engaging story based on this idea: {idea}. "
            "Include interesting characters, a clear plot, and vivid descriptions. "
            "The story should be at least 200 words long.",
            idea=idea
        )

        # Now, let's ask our AI to write the story
        try:
            response = self.generate_text(prompt)
            
            # 🕵️‍♂️ Let's check if our AI gave us a good story
            if not response:
                logger.warning("😴 Our AI returned an empty response.")
                return None

            # Yay! We got a story!
            self.story = response.strip()
            word_count = len(self.story.split())
            logger.info(f"✨ Wow! We created a story with {word_count} words!")
            
            if word_count < 200:
                logger.warning(f"Story is shorter than expected ({word_count} words)")
            
            return self.story

        except Exception as e:
            logger.error(f"🚨 An error occurred while creating the story: {str(e)}")
            return None

    def improve_story(self, feedback):
        """
        🚀 This is where we make our story even better based on feedback!
        
        Args:
            feedback (str): Feedback on how to improve the story
        
        Returns:
            str: The improved story
        """
        logger.info(f"🔧 Improving the story based on feedback: {feedback}")

        # Let's create a prompt for our AI to improve the story
        prompt = self.format_prompt(
            "Improve the following story based on this feedback: {feedback}\n\n"
            "Original Story: {story}\n\n"
            "Please provide the full improved story.",
            feedback=feedback,
            story=self.story
        )

        # Let's ask our AI to improve the story
        try:
            response = self.generate_text(prompt)

            # 🕵️‍♂️ Let's check if our AI gave us an improved story
            if not response:
                logger.warning("😴 Our AI returned an empty response for story improvement.")
                return "Our storyteller is taking a nap. The story remains unchanged."

            # Yay! We got an improved story!
            self.story = response.strip()
            logger.info(f"✨ Wow! We improved our story! It now has {len(self.story.split())} words!")
            return self.story

        except Exception as e:
            logger.error(f"🚨 An error occurred while improving the story: {str(e)}")
            return "Oops! Our storyteller got confused. The story remains unchanged."

    def get_story(self):
        """
        📖 This lets us read the story we created
        
        Returns:
            str: The current story
        """
        return self.story

# 🧪 Let's add some tests to make sure our StoryWriter works correctly
def test_story_writer():
    # 🤖 Create a pretend AI model for testing
    class DummyModel:
        def generate(self, prompt):
            return "Once upon a time, in a magical forest, there lived a brave little rabbit named Hoppy..."

    # 🦸‍♂️ Create our StoryWriter agent
    writer = StoryWriter(DummyModel())
    
    # 📝 Test creating a story
    idea = "A brave rabbit's adventure"
    story = writer.process(idea)
    assert "brave little rabbit" in story, "Story should include content from the idea"
    
    # 🚀 Test improving the story
    feedback = "Add more details about the magical forest"
    improved_story = writer.improve_story(feedback)
    assert "magical forest" in improved_story, "Improved story should incorporate feedback"
    
    # 📖 Test getting the story
    assert writer.get_story() == improved_story, "get_story should return the latest version of the story"

    print("🎉 All tests passed! Our StoryWriter is working great!")

# 🏃‍♂️ Run the tests when this file is run directly
if __name__ == "__main__":
    test_story_writer()

# 🎉 Hooray! We've created a magical StoryWriter agent!
# Now it can create and improve amazing stories! 🚀