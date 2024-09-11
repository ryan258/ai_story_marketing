# 📁 File: ai_story_marketing/ai_story_marketing/models/gpt4_model.py

import os
from openai import OpenAI
from dotenv import load_dotenv
import logging

# Set up our magical GPT-4 log 📜✨
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 🔍 Let's load our secret information
load_dotenv()

class GPT4Model:
    """
    🧠 This is our GPT4Model class. It's like a special telephone that lets us
    talk to the super smart GPT-4 AI who can help us write amazing stories!
    """

    def __init__(self):
        """
        🎬 This is where we set up our special GPT-4 telephone.
        We're getting the secret code (API key) and the name of our AI friend from our secret information.
        """
        # Get our secret API key and model name from the secret codes
        self.api_key = os.environ.get('OPENAI_API_KEY')
        self.model_name = os.getenv('OPENAI_MODEL_NAME')

        # Check if we have our secret API key
        if not self.api_key:
            raise ValueError("Oops! We can't find the secret code (API key) to talk to GPT-4. 😕")

        # Set up our telephone to GPT-4
        self.client = OpenAI(api_key=self.api_key)

    def generate(self, prompt):
        """
        📝 This is where we ask our GPT-4 friend to help us write a story.
        
        Args:
            prompt (str): This is the idea for our story that we tell GPT-4.
        
        Returns:
            str: This is the story that our GPT-4 friend writes for us.
                 If something goes wrong, we return None.
        """
        try:
            # 📞 We're calling our GPT-4 friend
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that writes creative stories."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000  # This is how long we want the story to be
            )
            
            # 📖 Let's get the story our GPT-4 friend wrote for us
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            # 😟 Uh-oh, something went wrong when talking to our GPT-4 friend
            logger.error(f"Oops! We couldn't talk to our GPT-4 friend. Here's what happened: {str(e)}")
            return None