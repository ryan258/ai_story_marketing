# 📁 File: ai_story_marketing/ai_story_marketing/agents/evaluator.py

# 🧐 Welcome to the Evaluator agent! 🏆
# This clever agent will judge the quality of our stories and help improve them! 📊

# First, let's import what we need
from .base_agent import BaseAgent  # We're using the basic structure from BaseAgent
import logging  # This helps us keep track of what's happening
import re  # This helps us find patterns in text

# Set up our magical evaluation log 📜✨
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Evaluator(BaseAgent):
    """
    🧐 This is our Evaluator agent.
    It's like a friendly teacher who reads our stories, gives them a grade, and helps make them better!
    """

    def __init__(self, model):
        """
        🎭 This is where we set up our Evaluator with its story-judging superpowers!
        
        Args:
            model: The AI model that gives our Evaluator its wisdom
        """
        super().__init__(model)  # We're using the setup from our BaseAgent
        self.score = 0  # This is where we'll keep the story's score
        self.feedback = ""  # This is where we'll keep the feedback for the story

    def process(self, story):
        """
        📝 This is where the magic happens! Our Evaluator reads a story and judges its quality.
        
        Args:
            story (str): The story to evaluate
        
        Returns:
            dict: A dictionary containing the score and feedback for the story
        """
        if not story:
            logger.warning("Received an empty story to evaluate")
            return {
                "score": 0,
                "feedback": "We couldn't evaluate the story because it was empty. Let's try creating a new story!"
            }

        # Let's create a prompt for our AI to evaluate the story
        prompt = self.format_prompt(
    "Evaluate the following story on a scale from 1 to 10, where 10 is excellent. "
    "Provide a score and detailed feedback on how to improve the story. "
    "In your evaluation, consider:\n"
    "1. Plot: Is it clear, engaging, and well-structured?\n"
    "2. Characters: Are they interesting, relatable, and well-developed?\n"
    "3. Setting: Is it vividly described and appropriate for the story?\n"
    "4. Theme: Is there a clear message or theme?\n"
    "5. Writing style: Is it engaging and suitable for a young audience?\n"
    "6. Marketing potential: Are there elements that could be used in marketing?\n"
    "Provide specific suggestions for improvement in each area. "
    "Story: {story}",
            story=story
        )
        
        # Now, let's ask our AI to evaluate the story
        evaluation = self.generate_text(prompt)
        logger.info(f"Raw evaluation: {evaluation}")

        try:
            if evaluation:
                # Look for a score in the format "X out of 10" or "X/10"
                score_match = re.search(r'(\d+(?:\.\d+)?)\s*(?:out of|\/)\s*10', evaluation)
                if score_match:
                    self.score = float(score_match.group(1))
                else:
                    self.score = 5.0  # Default score if no score is found
                    logger.warning("Could not find a score in the evaluation. Using default score of 5.0.")

                # Everything else is considered feedback
                self.feedback = evaluation.strip()
            else:
                raise ValueError("Empty evaluation received")

        except Exception as e:
            logger.error(f"Error processing evaluation: {e}")
            logger.error(f"Evaluation content: {evaluation}")
            # Provide a default evaluation
            self.score = 5.0
            self.feedback = ("We couldn't properly evaluate the story this time. "
                             "Consider adding more details to the characters and plot to make it more engaging.")
        
        # Let's remember this evaluation in our magical backpack (context)
        self.update_context({
            "latest_evaluation": {
                "score": self.score,
                "feedback": self.feedback
            }
        })
        
        return {
            "score": self.score,
            "feedback": self.feedback
        }

    def get_score(self):
        """
        🔢 This lets us see the score our Evaluator has given.
        
        Returns:
            float: The current score
        """
        return self.score

    def get_feedback(self):
        """
        💬 This lets us see the feedback our Evaluator has given.
        
        Returns:
            str: The current feedback
        """
        return self.feedback

# 🧪 Let's add some tests to make sure our Evaluator works correctly
def test_evaluator():
    # 🤖 Create a pretend AI model for testing
    class DummyModel:
        def generate(self, prompt):
            return "I'd rate this story 7.5 out of 10.\nFeedback: The story has a good premise, but could use more character development. Try adding more details about the protagonist's background and motivations. Also, consider expanding on the setting to make it more vivid and engaging."
    
    # 🦸‍♂️ Create our Evaluator agent
    evaluator = Evaluator(DummyModel())
    
    # 📝 Test evaluating a story
    story = "Once upon a time, there was a brave little mouse..."
    result = evaluator.process(story)
    
    assert isinstance(result, dict), "Result should be a dictionary"
    assert "score" in result, "Result should contain a score"
    assert result["score"] == 7.5, "Score should be 7.5"
    assert "character development" in result["feedback"], "Feedback should mention character development"
    
    # 🔢 Test getting the score
    assert evaluator.get_score() == 7.5, "get_score should return 7.5"
    
    # 💬 Test getting the feedback
    assert "setting" in evaluator.get_feedback(), "get_feedback should mention setting"

    print("🎉 All tests passed! Our Evaluator is working great!")

# 🏃‍♂️ Run the tests when this file is run directly
if __name__ == "__main__":
    test_evaluator()

# 🎉 Hooray! We've created a smart Evaluator agent!
# Now it can give scores and helpful feedback to improve our stories! 🚀