# 📁 File: ai_story_marketing/ai_story_marketing/agents/evaluator.py

# 🧐 Welcome to the Evaluator agent! 🏆
# This clever agent will judge the quality of our stories! 📊

from .base_agent import BaseAgent  # We're using the superhero costume we made earlier!

class Evaluator(BaseAgent):
    """
    🧐 This is our Evaluator agent.
    It's like a friendly teacher who reads our stories and gives them a grade!
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
        # Let's create a prompt for our AI to evaluate the story
        prompt = self.format_prompt(
            "Evaluate the following story and give it a score out of 10. "
            "Also provide brief feedback. "
            "Story: {story}",
            story=story
        )
        
        # Now, let's ask our AI to evaluate the story
        evaluation = self.generate_text(prompt)
        
        # Let's extract the score and feedback from the evaluation
        try:
            score_line, feedback = evaluation.split('\n', 1)
            self.score = float(score_line.split(':')[1].strip().split('/')[0])
            self.feedback = feedback.split(':', 1)[1].strip()
        except:
            self.score = 0
            self.feedback = "Error processing evaluation"
        
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
            return "Score: 8/10\nFeedback: Great story with interesting characters!"
    
    # 🦸‍♂️ Create our Evaluator agent
    evaluator = Evaluator(DummyModel())
    
    # 📝 Test evaluating a story
    story = "Once upon a time in a magical forest..."
    result = evaluator.process(story)
    assert isinstance(result, dict), "Result should be a dictionary"
    assert "score" in result, "Result should contain a score"
    assert "feedback" in result, "Result should contain feedback"
    assert result["score"] == 8, "Score should be 8"
    assert result["feedback"] == "Great story with interesting characters!", "Feedback should match"
    
    # 🔢 Test getting the score
    assert evaluator.get_score() == 8, "get_score should return 8"
    
    # 💬 Test getting the feedback
    assert evaluator.get_feedback() == "Great story with interesting characters!", "get_feedback should return the correct feedback"

# 🎉 Hooray! We've updated our Evaluator agent with new methods!
# Now it can give scores and feedback like a real teacher! 🚀