# 📁 File: ai_story_marketing/ai_story_marketing/agents/story_writer.py

import logging

# Set up our magical storytelling log 📜✨
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StoryWriter:
    """
    🧙‍♂️ Our magical StoryWriter! It turns ideas into amazing stories!
    """

    def __init__(self, model):
        """
        🎭 Getting our storyteller ready with a magical AI brain!
        """
        self.model = model  # Our AI brain
        self.story = ""     # Where we'll keep our story

    def process(self, idea):
        """
        📝 This is where the magic happens! We turn an idea into a story!
        """
        logger.info(f"🌟 Starting to write a story about: {idea}")

        # Now, let's ask our AI to write the story
        response = self.model.generate(idea)
        
        # 🕵️‍♂️ Let's check if our AI gave us a good story
        if not response:
            logger.info("😴 Our Llama AI is taking a nap!")
            return "Our storyteller is taking a nap. Try again later!"

        # Yay! We got a story!
        self.story = response.strip()
        logger.info(f"✨ Wow! We created a story with {len(self.story)} characters!")
        return self.story

    def get_story(self):
        """
        📖 This lets us read the story we created
        """
        return self.story

# Let's test our StoryWriter!
if __name__ == "__main__":
    from ..models.llama_model import LlamaModel
    
    writer = StoryWriter(LlamaModel())
    for _ in range(5):  # Let's try 5 times
        story = writer.process("a magical adventure")
        print(f"🎉 Our story: {story}")
    
    print("🎊 Yay! Our StoryWriter works with our Llama AI!")