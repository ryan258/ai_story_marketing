# 📁 File: ai_story_marketing/ai_story_marketing/agents/story_improver.py

from .base_agent import BaseAgent
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class StoryImprover(BaseAgent):
    def __init__(self, model):
        super().__init__(model)

    def process(self, story, feedback):
        logger.debug(f"Improving story: {story[:50]}... with feedback: {feedback}")
        
        prompt = self.format_prompt(
            "Improve the following story based on this feedback:\n\n"
            "Feedback: {feedback}\n\n"
            "Original Story: {story}\n\n"
            "Please provide the full improved story, incorporating the feedback.",
            feedback=feedback,
            story=story
        )

        try:
            improved_story = self.generate_text(prompt)
            
            if not improved_story:
                logger.warning("Received empty response from AI model")
                return f"Story remains unchanged: {story}"  # Return original story with a message if improvement fails
            
            logger.debug(f"Improved story: {improved_story[:50]}...")
            return improved_story

        except Exception as e:
            logger.error(f"Error in story improvement: {str(e)}")
            return f"Story remains unchanged due to an error: {story}"  # Return original story with an error message