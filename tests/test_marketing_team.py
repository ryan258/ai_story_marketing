# 📁 File: ai_story_marketing/tests/test_marketing_team.py

# 🧪 Welcome to the Marketing Team Test file! 🚀
# Here we'll make sure our Marketing Team agent is working correctly! 🕵️‍♂️

import unittest
from unittest.mock import MagicMock
from ai_story_marketing.agents.marketing_team import MarketingTeam  # Import our MarketingTeam class

class TestMarketingTeam(unittest.TestCase):
    """
    🧐 This is our TestMarketingTeam class.
    It's like a detective that checks if our Marketing Team agent is doing its job right!
    """

    def setUp(self):
        """
        🎬 This method runs before each test.
        It's like setting up the stage before we perform our play!
        """
        # Create a fake AI model for testing
        self.mock_model = MagicMock()
        self.mock_model.generate.return_value = "Exciting marketing concept!"
        
        # Create our Marketing Team with the fake model
        self.team = MarketingTeam(self.mock_model)

    def test_process(self):
        """
        🔍 This test checks if our Marketing Team can create concepts for all marketing materials.
        """
        story = "An epic tale of adventure and discovery in a magical realm..."
        personas = ["Alex, 28, fantasy enthusiast", "Sam, 35, movie buff"]
        target_audience = "Young adults who love fantasy and adventure"
        
        result = self.team.process(story, personas, target_audience)

        # Check if the result is a dictionary
        self.assertIsInstance(result, dict, "Result should be a dictionary")

        # Check if we have concepts for all marketing materials
        for material in self.team.marketing_materials.keys():
            self.assertIn(material, result, f"Result should contain concept for {material}")
            self.assertEqual(result[material], "Exciting marketing concept!", f"Concept for {material} should match expected")

    def test_get_concept(self):
        """
        🎨 This test checks if we can get concepts correctly for specific materials and all materials.
        """
        # First, process a story to generate concepts
        self.team.process("A story...", ["Persona"], "Target audience")
        
        # Test getting concept for a specific material
        commercial_concept = self.team.get_concept('commercial')
        self.assertEqual(commercial_concept, "Exciting marketing concept!", "Commercial concept should match expected")
        
        # Test getting concept for a non-existent material
        nonexistent_concept = self.team.get_concept('radio_ad')
        self.assertEqual(nonexistent_concept, "No concept available for this material", "Should handle non-existent materials")
        
        # Test getting all concepts
        all_concepts = self.team.get_concept()
        self.assertIsInstance(all_concepts, dict, "All concepts should be a dictionary")
        self.assertEqual(len(all_concepts), 3, "All concepts should have 3 materials")

    def test_context_update(self):
        """
        🧠 This test checks if our context is being updated correctly.
        """
        story = "A tale of adventure..."
        personas = ["Adventure seeker"]
        target_audience = "Thrill-seekers"
        self.team.process(story, personas, target_audience)
        
        context = self.team.get_context()
        self.assertIn('marketing_concepts', context, "Context should contain marketing concepts")
        self.assertIsInstance(context['marketing_concepts'], dict, "Marketing concepts should be a dictionary")
        self.assertEqual(len(context['marketing_concepts']), 3, "Marketing concepts should have 3 materials")

if __name__ == '__main__':
    unittest.main()

# 🎉 Hooray! We've created comprehensive tests for our Marketing Team agent!
# Now we can be sure it's creating awesome marketing concepts for all materials! 🚀