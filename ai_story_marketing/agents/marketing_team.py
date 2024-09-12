# 📁 File: ai_story_marketing/ai_story_marketing/agents/marketing_team.py

# 🎭 Welcome to the Marketing Team agent! 🎬
# This creative agent will help us develop amazing marketing concepts for our stories! 🚀

from .base_agent import BaseAgent  # We're using the superhero costume we made earlier!

class MarketingTeam(BaseAgent):
    """
    🎭 This is our Marketing Team agent.
    It's like a group of creative geniuses who come up with awesome ideas to promote our stories!
    """

    def __init__(self, model):
        """
        🎬 This is where we set up our Marketing Team with its idea-generating superpowers!
        
        Args:
            model: The AI model that gives our Marketing Team its creativity
        """
        super().__init__(model)  # We're using the setup from our BaseAgent
        self.marketing_materials = {
            'commercial': None,
            'movie_poster': None,
            'viral_campaign': None
        }

    def process(self, story, personas, target_audience):
        """
        💡 This is where the magic happens! Our Marketing Team creates concepts for different marketing materials.
        
        Args:
            story (str): The story we're promoting
            personas (list): The marketing personas we're targeting
            target_audience (str): Description of our target audience
        
        Returns:
            dict: A dictionary containing concepts for each type of marketing material
        """
        for material in self.marketing_materials.keys():
            # Let's create a prompt for our AI to generate concepts for each marketing material
            prompt = self.format_prompt(
    "Create an innovative concept for a {material} to promote the following story. "
    "Your concept should:\n"
    "1. Capture the essence and main themes of the story\n"
    "2. Appeal to the target audience: {audience}\n"
    "3. Resonate with these personas: {personas}\n"
    "4. Be visually striking and memorable\n"
    "5. Include a tagline or key message\n"
    "6. Consider the appropriate tone and style for the story and audience\n"
    "7. Incorporate key marketing elements identified earlier\n\n"
    "Story summary: {story}\n\n"
    "Provide a detailed description of your {material} concept, including visual elements, "
    "copy, and the rationale behind your choices.",
    material=material.replace('_', ' '),
    audience=target_audience,
    personas=", ".join(personas),
    story=story[:250] + "..."
)
            
            # Now, let's ask our AI to create the concept
            self.marketing_materials[material] = self.generate_text(prompt)
        
        # Let's remember these concepts in our magical backpack (context)
        self.update_context({
            "marketing_concepts": self.marketing_materials
        })
        
        return self.marketing_materials

    def get_concept(self, material=None):
        """
        🎨 This lets us see the marketing concepts our team has created.
        
        Args:
            material (str, optional): The specific marketing material to get the concept for. 
                                      If None, returns all concepts.
        
        Returns:
            dict or str: The concept for the specified material or all concepts
        """
        if material:
            return self.marketing_materials.get(material, "No concept available for this material")
        return self.marketing_materials

# 🧪 Let's add some tests to make sure our Marketing Team works correctly
def test_marketing_team():
    # 🤖 Create a pretend AI model for testing
    class DummyModel:
        def generate(self, prompt):
            material = prompt.split('{material}')[1].split()[0]
            return f"Exciting {material} concept: [Creative idea goes here]"
    
    # 🦸‍♂️ Create our Marketing Team agent
    team = MarketingTeam(DummyModel())
    
    # 📊 Test creating marketing concepts
    story = "An epic tale of adventure and discovery in a magical realm..."
    personas = ["Alex, 28, fantasy enthusiast", "Sam, 35, movie buff"]
    target_audience = "Young adults who love fantasy and adventure"
    result = team.process(story, personas, target_audience)
    
    assert isinstance(result, dict), "Result should be a dictionary"
    assert len(result) == 3, "There should be concepts for 3 marketing materials"
    assert all(material in result for material in team.marketing_materials), "All materials should have concepts"
    
    # 🎬 Test getting concept for a specific material
    commercial_concept = team.get_concept('commercial')
    assert "commercial concept" in commercial_concept, "Commercial concept should mention 'commercial'"
    
    # 🌐 Test getting all concepts
    all_concepts = team.get_concept()
    assert isinstance(all_concepts, dict), "All concepts should be a dictionary"
    assert len(all_concepts) == 3, "All concepts should have 3 materials"

# 🎉 Hooray! We've created our Marketing Team agent!
# Now we can create awesome marketing concepts to promote our stories! 🚀