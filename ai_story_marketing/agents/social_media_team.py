# 📁 File: ai_story_marketing/ai_story_marketing/agents/social_media_team.py

# 📱 Welcome to the Social Media Team agent! 🎉
# This creative agent will help us generate amazing content for various social media platforms! 🚀

from .base_agent import BaseAgent  # We're using the superhero costume we made earlier!

class SocialMediaTeam(BaseAgent):
    """
    📱 This is our Social Media Team agent.
    It's like a group of cool friends who know all about making fun posts on social media!
    """

    def __init__(self, model):
        """
        🎭 This is where we set up our Social Media Team with its content-creating superpowers!
        
        Args:
            model: The AI model that gives our Social Media Team its creativity
        """
        super().__init__(model)  # We're using the setup from our BaseAgent
        self.platforms = ['Twitter', 'Instagram', 'Facebook', 'TikTok']  # The social media platforms we'll create content for
        self.content = {}  # This is where we'll store our created content

    def process(self, story, personas, target_audience):
        """
        🎨 This is where the magic happens! Our Social Media Team creates content for different platforms.
        
        Args:
            story (str): The story we're promoting
            personas (list): The marketing personas we're targeting
            target_audience (str): Description of our target audience
        
        Returns:
            dict: A dictionary containing content for each social media platform
        """
        for platform in self.platforms:
            # Let's create a prompt for our AI to generate content for each platform
            prompt = self.format_prompt(
    "Create an engaging {platform} post to promote the following story. "
    "Your post should:\n"
    "1. Capture the essence of the story in a concise, intriguing way\n"
    "2. Appeal to the target audience: {audience}\n"
    "3. Resonate with these personas: {personas}\n"
    "4. Include relevant hashtags and call-to-action\n"
    "5. Adhere to {platform}'s best practices and character limits\n"
    "6. Incorporate key marketing elements if possible\n\n"
    "Story summary: {story}\n\n"
    "Provide the post content and a brief explanation of your strategy.",
    platform=platform,
    audience=target_audience,
    personas=", ".join(personas),
    story=story[:150] + "..."
)
            
            # Now, let's ask our AI to create the content
            self.content[platform] = self.generate_text(prompt)
        
        # Let's remember this content in our magical backpack (context)
        self.update_context({
            "social_media_content": self.content
        })
        
        return self.content

    def get_content(self, platform=None):
        """
        📬 This lets us see the social media content our team has created.
        
        Args:
            platform (str, optional): The specific platform to get content for. If None, returns all content.
        
        Returns:
            dict or str: The content for the specified platform or all platforms
        """
        if platform:
            return self.content.get(platform, "No content available for this platform")
        return self.content

# 🧪 Let's add some tests to make sure our Social Media Team works correctly
def test_social_media_team():
    # 🤖 Create a pretend AI model for testing
    class DummyModel:
        def generate(self, prompt):
            return f"Exciting social media post for {prompt.split()[2]}!"
    
    # 🦸‍♂️ Create our Social Media Team agent
    team = SocialMediaTeam(DummyModel())
    
    # 📊 Test creating content
    story = "An amazing adventure in a magical land..."
    personas = ["John, 25, tech enthusiast", "Sarah, 30, nature lover"]
    target_audience = "Young adults interested in fantasy and adventure"
    result = team.process(story, personas, target_audience)
    
    assert isinstance(result, dict), "Result should be a dictionary"
    assert len(result) == 4, "There should be content for 4 platforms"
    assert all(platform in result for platform in team.platforms), "All platforms should have content"
    
    # 📱 Test getting content for a specific platform
    twitter_content = team.get_content('Twitter')
    assert "Twitter" in twitter_content, "Twitter content should mention Twitter"
    
    # 🌐 Test getting all content
    all_content = team.get_content()
    assert isinstance(all_content, dict), "All content should be a dictionary"
    assert len(all_content) == 4, "All content should have 4 platforms"

# 🎉 Hooray! We've created our Social Media Team agent!
# Now we can create awesome social media content to promote our stories! 🚀