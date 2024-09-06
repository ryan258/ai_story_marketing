# File: ai_story_marketing/ai_story_marketing/agents/base_agent.py

from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, model):
        self.model = model
        self.context = {}

    @abstractmethod
    def process(self, input_data):
        """
        Process the input data and return the result.
        This method should be implemented by all subclasses.
        """
        pass

    def update_context(self, new_data):
        """
        Update the agent's context with new data.
        """
        self.context.update(new_data)

    def get_context(self):
        """
        Return the current context.
        """
        return self.context

    def generate_text(self, prompt):
        """
        Generate text using the associated AI model.
        """
        return self.model.generate(prompt)

    def format_prompt(self, template, **kwargs):
        """
        Format a prompt template with the given kwargs.
        """
        return template.format(**kwargs)