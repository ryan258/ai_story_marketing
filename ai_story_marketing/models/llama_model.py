# 📁 File: ai_story_marketing/ai_story_marketing/models/llama_model.py

import random  # We'll use this to make our AI a bit random and fun!

class LlamaModel:
    """
    🦙 Our magical Llama AI model! It's not a real AI, but it's fun to pretend!
    """

    def __init__(self):
        # 🎭 Let's set up our pretend AI with some fun story pieces
        self.characters = ["wise old tree", "curious rabbit", "friendly cloud", "brave little mouse"]
        self.places = ["enchanted forest", "hidden valley", "magical garden", "cozy treehouse"]
        self.events = ["found a secret map", "learned to fly", "made new friends", "solved a tricky puzzle"]

    def generate(self, prompt):
        """
        ✨ This is where our Llama AI creates a fun little story!
        """
        # 🎲 Let's randomly choose if our AI is awake or napping
        if random.choice([True, False]):
            # 🌟 If it's awake, let's make a story!
            character = random.choice(self.characters)
            place = random.choice(self.places)
            event = random.choice(self.events)
            
            story = f"Once upon a time, in a {place}, there was a {character}. "
            story += f"One day, the {character} {event}. "
            story += "And they all lived happily ever after!"
            
            return story
        else:
            # 😴 If it's napping, let's say so!
            return None  # This will tell our StoryWriter that the AI is "napping"

# 🧪 Let's test our LlamaModel!
if __name__ == "__main__":
    llama = LlamaModel()
    for _ in range(5):  # Let's try 5 times
        story = llama.generate("Any prompt")
        if story:
            print(f"🦙 Llama says: {story}")
        else:
            print("😴 Llama is napping!")
    
    print("🎉 Yay! Our pretend Llama AI is working!")