# 📁 File: ai_story_marketing/ai_story_marketing/models/llama_model.py

# 🦙 Welcome to the Llama Model file! 🌟
# This is where we talk to our smart Llama friend to help us write stories!

import requests  # We use this to send messages to our Llama
import os  # This helps us read secret information
from dotenv import load_dotenv  # This loads our secret information

# 🔍 Let's load our secret information
load_dotenv()

class LlamaModel:
    """
    🦙 This is our Llama Model class. It's like a special telephone that lets us
    talk to a very smart Llama who can help us write stories!
    """

    def __init__(self):
        """
        🎬 This is where we set up our special Llama telephone.
        We're getting the address (URL) and name of our Llama friend from our secret information.
        """
        self.api_url = os.getenv('API_URL')  # The address where our Llama lives
        self.model_name = os.getenv('MODEL_NAME')  # The name of our Llama friend

    def generate(self, prompt):
        """
        📝 This is where we ask our Llama friend to help us write a story.
        
        Args:
            prompt (str): This is the idea for our story that we tell the Llama.
        
        Returns:
            str: This is the story that our Llama friend writes for us.
                 If something goes wrong, we return None.
        """
        try:
            # 📮 We're sending a message to our Llama friend
            response = requests.post(self.api_url, json={
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            })
            
            # 📬 Let's check if our message was sent successfully
            response.raise_for_status()
            
            # 📖 Now, let's read the story our Llama friend wrote for us
            result = response.json()
            return result['response']
        
        except Exception as e:
            # 😟 Uh-oh, something went wrong when talking to our Llama friend
            print(f"Oops! We couldn't talk to our Llama friend. Here's what happened: {e}")
            return None

# 🧪 Let's test our Llama Model to make sure it works!
if __name__ == "__main__":
    llama = LlamaModel()
    story_idea = "A brave little mouse goes on an adventure in a big city"
    story = llama.generate(story_idea)
    
    if story:
        print("🎉 Yay! Our Llama friend wrote us a story!")
        print("📖 Here's the story:")
        print(story)
    else:
        print("😔 Oh no! Our Llama friend couldn't write a story this time.")