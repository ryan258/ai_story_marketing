# 📁 File: ai_story_marketing/ai_story_marketing/agents/marketing_expert.py

# 🎯 Welcome to the Marketing Expert agent! 📊
# This clever agent will help us understand our audience and create amazing marketing personas! 🧑‍🤝‍🧑

from .base_agent import BaseAgent  # We're using the superhero costume we made earlier!

class MarketingExpert(BaseAgent):
    """
    📊 This is our Marketing Expert agent.
    It's like a friendly market researcher who knows all about our readers!
    """

    def __init__(self, model):
        """
        🎭 This is where we set up our Marketing Expert with its audience-understanding superpowers!
        
        Args:
            model: The AI model that gives our Marketing Expert its wisdom
        """
        super().__init__(model)  # We're using the setup from our BaseAgent
        self.personas = []  # This is where we'll keep our marketing personas
        self.target_audience = {}  # This is where we'll store information about our target audience

    def process(self, story):
        """
        🧠 This is where the magic happens! Our Marketing Expert analyzes the story and creates personas.
        
        Args:
            story (str): The story to analyze
        
        Returns:
            dict: A dictionary containing the personas and target audience information
        """
        # Let's create a prompt for our AI to analyze the story and create personas
        prompt = self.format_prompt(
            "Analyze the following story and create 3 marketing personas. "
            "Also provide a brief description of the target audience. "
            "Story: {story}",
            story=story
        )
        
        # Now, let's ask our AI to do the analysis
        analysis = self.generate_text(prompt)
        
        # Let's extract the personas and target audience information from the analysis
        try:
            personas, target_audience = analysis.split('Target Audience:', 1)
            self.personas = [p.strip() for p in personas.split('Persona')[1:]]
            self.target_audience = target_audience.strip()
        except:
            self.personas = []
            self.target_audience = "Error processing analysis"
        
        # Let's remember this analysis in our magical backpack (context)
        self.update_context({
            "marketing_analysis": {
                "personas": self.personas,
                "target_audience": self.target_audience
            }
        })
        
        return {
            "personas": self.personas,
            "target_audience": self.target_audience
        }

    def get_personas(self):
        """
        👥 This lets us see the marketing personas our expert has created.
        
        Returns:
            list: The current list of personas
        """
        return self.personas

    def get_target_audience(self):
        """
        🎯 This lets us see the target audience information our expert has identified.
        
        Returns:
            str: The current target audience description
        """
        return self.target_audience

# 🧪 Let's add some tests to make sure our Marketing Expert works correctly
def test_marketing_expert():
    # 🤖 Create a pretend AI model for testing
    class DummyModel:
        def generate(self, prompt):
            return """
            Persona 1: John, 35, tech-savvy professional
            Persona 2: Sarah, 28, adventure enthusiast
            Persona 3: Alex, 42, busy parent
            Target Audience: Young to middle-aged adults interested in technology and adventure
            """
    
    # 🦸‍♂️ Create our Marketing Expert agent
    expert = MarketingExpert(DummyModel())
    
    # 📊 Test analyzing a story
    story = "A thrilling tale of a tech startup's adventure in the Silicon Valley..."
    result = expert.process(story)
    assert isinstance(result, dict), "Result should be a dictionary"
    assert "personas" in result, "Result should contain personas"
    assert "target_audience" in result, "Result should contain target audience info"
    assert len(result["personas"]) == 3, "There should be 3 personas"
    assert "young to middle-aged adults" in result["target_audience"].lower(), "Target audience should match expected"
    
    # 👥 Test getting the personas
    personas = expert.get_personas()
    assert len(personas) == 3, "There should be 3 personas"
    assert any("John" in p for p in personas), "John should be in the personas"
    assert any("Sarah" in p for p in personas), "Sarah should be in the personas"
    assert any("Alex" in p for p in personas), "Alex should be in the personas"
    
    # 🎯 Test getting the target audience
    target_audience = expert.get_target_audience()
    assert "young to middle-aged adults" in target_audience.lower(), "Target audience should match expected"

# 🎉 Hooray! We've created our Marketing Expert agent!
# Now we can understand our audience and create amazing marketing strategies! 🚀