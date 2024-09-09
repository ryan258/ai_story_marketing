# 📁 File: ai_story_marketing/ai_story_marketing/agents/base_agent.py

# 🤖 Welcome to the Base Agent file! 🚀
# This is like the superhero costume that all our AI agents will wear! 🦸‍♂️

from abc import ABC, abstractmethod  # This helps us create a blueprint for our agents

class BaseAgent(ABC):
    """
    🏗️ This is the foundation for all our AI agents.
    It's like a recipe that tells us what every agent should be able to do!
    """

    def __init__(self, model):
        """
        🎭 This is where we set up our agent with its super AI powers!
        
        Args:
            model: The AI model that gives our agent its smarts
        """
        self.model = model  # The AI brain of our agent
        self.context = {}   # A magical backpack to store important information

    @abstractmethod
    def process(self, input_data):
        """
        🧠 This is the main job of our agent. It takes input and does something smart with it!
        
        Every agent we create must have its own version of this method.
        
        Args:
            input_data: The information our agent needs to work with
        
        Returns:
            The result of the agent's work
        """
        pass  # We'll fill this in for each specific agent later

    def update_context(self, new_data):
        """
        📚 This helps our agent remember important things.
        
        Args:
            new_data (dict): New information to add to our agent's memory
        """
        self.context.update(new_data)

    def get_context(self):
        """
        🔍 This lets us see what our agent remembers.
        
        Returns:
            dict: All the information our agent has stored
        """
        return self.context

    def generate_text(self, prompt):
        """
        💬 This is how our agent talks! It uses its AI brain to create text.
        
        Args:
            prompt (str): The question or instruction we give to the AI
        
        Returns:
            str: The AI's response
        """
        return self.model.generate(prompt)

    def format_prompt(self, template, **kwargs):
        """
        ✨ This helps our agent create special messages.
        
        Args:
            template (str): A fill-in-the-blank message
            **kwargs: The words to fill in the blanks
        
        Returns:
            str: The completed message
        """
        return template.format(**kwargs)

# 🧪 Let's add some tests to make sure our BaseAgent works correctly
def test_base_agent():
    # 🤖 Create a pretend AI model for testing
    class DummyModel:
        def generate(self, prompt):
            return f"AI says: {prompt}"
    
    # 🦸‍♂️ Create a pretend agent using our BaseAgent
    class TestAgent(BaseAgent):
        def process(self, input_data):
            return f"Processed: {input_data}"
    
    # 🏗️ Set up our test agent
    agent = TestAgent(DummyModel())
    
    # 🧠 Test the process method
    assert agent.process("hello") == "Processed: hello", "Process method should work correctly"
    
    # 📚 Test updating and getting context
    agent.update_context({"key": "value"})
    assert agent.get_context() == {"key": "value"}, "Context should be updated and retrieved correctly"
    
    # 💬 Test generating text
    assert agent.generate_text("hello") == "AI says: hello", "Text generation should work correctly"
    
    # ✨ Test formatting prompts
    template = "Hello, {name}!"
    formatted = agent.format_prompt(template, name="World")
    assert formatted == "Hello, World!", "Prompt formatting should work correctly"

# 🎉 Hooray! We've created the base for all our AI agents!
# Next, we'll create specific agents that use this base! 🚀