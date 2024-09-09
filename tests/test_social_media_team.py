# 📁 File: ai_story_marketing/tests/test_social_media_team.py

# 🧪 Welcome to the Social Media Team Test file! 🚀
# Here we'll make sure our Social Media Team agent is working correctly! 🕵️‍♂️

import unittest
from unittest.mock import MagicMock
from ai_story_marketing.agents.social_media_team import SocialMediaTeam  # Import our SocialMediaTeam class

class TestSocialMediaTeam(unittest.TestCase):
    """
    🧐 This is our TestSocialMediaTeam class.
    It's like a detective that checks if our Social Media Team agent is doing its job right!
    """

    def setUp(self):
        """
        🎬 This method runs before each test.
        It's like setting up the stage before we perform our play!
        """
        # Create a fake AI model for testing
        self.mock_model = MagicMock()
        self.mock_model.generate.return_value = "Exciting social media post!"
        
        # Create our Social Media Team with the fake model
        self.team = SocialMediaTeam(self.mock_model)

    def test_process(self):
        """
        🔍 This test checks if our Social Media Team can create content for all platforms.
        """
        story = "An amazing adventure in a magical land..."
        personas = ["John, 25, tech enthusiast", "Sarah, 30, nature lover"]
        target_audience = "Young adults interested in fantasy and adventure"
        
        result = self.team.process(story, personas, target_audience)

        # Check if the result is a dictionary
        self.assertIsInstance(result, dict, "Result should be a dictionary")

        # Check if we have content for all platforms
        for platform in self.team.platforms:
            self.assertIn(platform, result, f"Result should contain content for {platform}")
            self.assertEqual(result[platform], "Exciting social media post!", f"Content for {platform} should match expected")

    def test_get_content(self):
        """
        📱 This test checks if we can get content correctly for specific platforms and all platforms.
        """
        # First, process a story to generate content
        self.team.process("A story...", ["Persona"], "Target audience")
        
        # Test getting content for a specific platform
        twitter_content = self.team.get_content('Twitter')
        self.assertEqual(twitter_content, "Exciting social media post!", "Twitter content should match expected")
        
        # Test getting content for a non-existent platform
        nonexistent_content = self.team.get_content('MySpace')
        self.assertEqual(nonexistent_content, "No content available for this platform", "Should handle non-existent platforms")
        
        # Test getting all content
        all_content = self.team.get_content()
        self.assertIsInstance(all_content, dict, "All content should be a dictionary")
        self.assertEqual(len(all_content), 4, "All content should have 4 platforms")

    def test_context_update(self):
        """
        🧠 This test checks if our context is being updated correctly.
        """
        story = "A tale of adventure..."
        personas = ["Adventure seeker"]
        target_audience = "Thrill-seekers"
        self.team.process(story, personas, target_audience)
        
        context = self.team.get_context()
        self.assertIn('social_media_content', context, "Context should contain social media content")
        self.assertIsInstance(context['social_media_content'], dict, "Social media content should be a dictionary")
        self.assertEqual(len(context['social_media_content']), 4, "Social media content should have 4 platforms")

if __name__ == '__main__':
    unittest.main()

# 🎉 Hooray! We've created comprehensive tests for our Social Media Team agent!
# Now we can be sure it's creating awesome content for all platforms! 🚀