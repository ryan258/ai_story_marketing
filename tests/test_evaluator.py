# 📁 File: ai_story_marketing/tests/test_evaluator.py

# 🧪 Welcome to the Evaluator Test file! 🚀
# Here we'll make sure our Evaluator agent is working correctly! 🕵️‍♂️

import unittest
from unittest.mock import MagicMock
from ai_story_marketing.agents.evaluator import Evaluator  # Import our Evaluator class

class TestEvaluator(unittest.TestCase):
    """
    🧐 This is our TestEvaluator class.
    It's like a detective that checks if our Evaluator agent is doing its job right!
    """

    def setUp(self):
        """
        🎬 This method runs before each test.
        It's like setting up the stage before we perform our play!
        """
        # Create a fake AI model for testing
        self.mock_model = MagicMock()
        self.mock_model.generate.return_value = "Score: 8/10\nFeedback: Great story!"
        
        # Create our Evaluator with the fake model
        self.evaluator = Evaluator(self.mock_model)

    def test_process(self):
        """
        🔍 This test checks if our Evaluator can process a story correctly.
        """
        story = "Once upon a time, there was a brave little mouse..."
        result = self.evaluator.process(story)

        # Check if the result is a dictionary
        self.assertIsInstance(result, dict, "Result should be a dictionary")

        # Check if the result contains 'score' and 'feedback' keys
        self.assertIn('score', result, "Result should contain a 'score' key")
        self.assertIn('feedback', result, "Result should contain a 'feedback' key")

        # Check if the score is a number between 0 and 10
        self.assertIsInstance(result['score'], (int, float), "Score should be a number")
        self.assertGreaterEqual(result['score'], 0, "Score should be at least 0")
        self.assertLessEqual(result['score'], 10, "Score should be at most 10")

        # Check if the feedback is a non-empty string
        self.assertIsInstance(result['feedback'], str, "Feedback should be a string")
        self.assertGreater(len(result['feedback']), 0, "Feedback should not be empty")

    def test_get_score(self):
        """
        🔢 This test checks if we can get the score correctly.
        """
        self.evaluator.score = 7
        self.assertEqual(self.evaluator.get_score(), 7, "get_score should return the correct score")

    def test_get_feedback(self):
        """
        💬 This test checks if we can get the feedback correctly.
        """
        self.evaluator.feedback = "Good job!"
        self.assertEqual(self.evaluator.get_feedback(), "Good job!", "get_feedback should return the correct feedback")

if __name__ == '__main__':
    unittest.main()

# 🎉 Hooray! We've created tests for our Evaluator agent!
# Now we can be sure it's working correctly! 🚀