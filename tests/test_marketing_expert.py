# 📁 File: ai_story_marketing/tests/test_marketing_expert.py

# 🧪 Welcome to the Marketing Expert Test file! 🚀
# Here we'll make sure our Marketing Expert agent is working correctly! 🕵️‍♂️

import unittest
from unittest.mock import MagicMock
from ai_story_marketing.agents.marketing_expert import MarketingExpert  # Import our MarketingExpert class

class TestMarketingExpert(unittest.TestCase):
    """
    🧐 This is our TestMarketingExpert class.
    It's like a detective that checks if our Marketing Expert agent is doing its job right!
    """

    def setUp(self):
        """
        🎬 This method runs before each test.
        It's like setting up the stage before we perform our play!
        """
        # Create a fake AI model for testing
        self.mock_model = MagicMock()
        self.mock_model.generate.return_value = """
        Persona 1: Emily, 28, urban professional
        Persona 2: Michael, 35, tech enthusiast
        Persona 3: Sarah, 42, busy mom
        Target Audience: Young to middle-aged adults interested in technology and family life
        """
        
        # Create our Marketing Expert with the fake model
        self.expert = MarketingExpert(self.mock_model)

    def test_process(self):
        """
        🔍 This test checks if our Marketing Expert can process a story correctly.
        """
        story = "A heartwarming tale of a family discovering the joys of new technology..."
        result = self.expert.process(story)

        # Check if the result is a dictionary
        self.assertIsInstance(result, dict, "Result should be a dictionary")

        # Check if the result contains 'personas' and 'target_audience' keys
        self.assertIn('personas', result, "Result should contain a 'personas' key")
        self.assertIn('target_audience', result, "Result should contain a 'target_audience' key")

        # Check if we have 3 personas
        self.assertEqual(len(result['personas']), 3, "There should be 3 personas")

        # Check if the target audience is a non-empty string
        self.assertIsInstance(result['target_audience'], str, "Target audience should be a string")
        self.assertGreater(len(result['target_audience']), 0, "Target audience should not be empty")

    def test_get_personas(self):
        """
        👥 This test checks if we can get the personas correctly.
        """
        # First, process a story to generate personas
        self.expert.process("A story about technology and family life...")
        
        personas = self.expert.get_personas()
        self.assertEqual(len(personas), 3, "There should be 3 personas")
        self.assertTrue(any("Emily" in p for p in personas), "Emily should be in the personas")
        self.assertTrue(any("Michael" in p for p in personas), "Michael should be in the personas")
        self.assertTrue(any("Sarah" in p for p in personas), "Sarah should be in the personas")

    def test_get_target_audience(self):
        """
        🎯 This test checks if we can get the target audience correctly.
        """
        # First, process a story to generate target audience
        self.expert.process("A story about technology and family life...")
        
        target_audience = self.expert.get_target_audience()
        self.assertIsInstance(target_audience, str, "Target audience should be a string")
        self.assertIn("Young to middle-aged adults", target_audience, "Target audience should match expected description")

    def test_context_update(self):
        """
        🧠 This test checks if our context is being updated correctly.
        """
        story = "A tale of technology and family..."
        self.expert.process(story)
        
        context = self.expert.get_context()
        self.assertIn('marketing_analysis', context, "Context should contain marketing analysis")
        self.assertIn('personas', context['marketing_analysis'], "Marketing analysis should include personas")
        self.assertIn('target_audience', context['marketing_analysis'], "Marketing analysis should include target audience")

if __name__ == '__main__':
    unittest.main()

# 🎉 Hooray! We've created comprehensive tests for our Marketing Expert agent!
# Now we can be sure it's working correctly! 🚀