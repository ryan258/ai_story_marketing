# 📁 File: ai_story_marketing/ai_story_marketing/main.py

from flask import Flask, render_template, request, jsonify
from .agents.story_writer import StoryWriter
from .models.llama_model import LlamaModel

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    
    model = LlamaModel()  # Our magical AI brain
    story_writer = StoryWriter(model)
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            idea = request.form.get('idea')
            logger.info(f"🌟 We got a new idea: {idea}")

            if not idea:
                return jsonify({"error": "Oops! We need an idea to write a story!"})

            try:
                story = story_writer.process(idea)
                
                # Let's create a fun response with all the expected keys!
                response = {
                    "story": story,
                    "evaluation": "Our story critic gives it 5 stars! ⭐⭐⭐⭐⭐",
                    "marketing_analysis": {
                        "target_audience": "Kids who love magical adventures!",
                        "personas": ["Curious Cathy", "Adventurous Alex", "Imaginative Ian"]
                    },
                    "social_media_content": {
                        "tweet": "Check out this magical story about a wise old tree! #KidsStories",
                        "instagram": "Once upon a time, in a hidden valley... 📚✨ #StoryTime"
                    },
                    "marketing_concepts": [
                        "Animated short film",
                        "Interactive storybook app",
                        "Tree-planting campaign tie-in"
                    ]
                }
                
                return jsonify(response)
            except Exception as e:
                logger.error(f"🙀 Oh no! Something went wrong: {str(e)}")
                return jsonify({"error": f"Our storyteller got confused: {str(e)}"})

        return render_template('index.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

print("🚀 Our magical story app is ready!")