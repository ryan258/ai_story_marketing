# 📁 File: ai_story_marketing/ai_story_marketing/main.py

# Let's import all the cool stuff we need! 🧙‍♂️
from flask import Flask, render_template, request, jsonify
from .agents.story_writer import StoryWriter
from .agents.evaluator import Evaluator
from .agents.marketing_expert import MarketingExpert
from .agents.social_media_team import SocialMediaTeam
from .agents.marketing_team import MarketingTeam
from .models.llama_model import LlamaModel
from .utils.output_generator import OutputGenerator

import logging

# Set up our magical story-telling log 📜✨
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    # Create our Flask app - it's like a magic wand for websites! 🪄
    app = Flask(__name__)
    
    # Create our AI brain and all our special agent friends 🧠👥
    model = LlamaModel()  # Our magical AI brain
    story_writer = StoryWriter(model)
    evaluator = Evaluator(model)
    marketing_expert = MarketingExpert(model)
    social_media_team = SocialMediaTeam(model)
    marketing_team = MarketingTeam(model)
    
    # Create our output generator - it's like a magical notebook! 📓
    output_generator = OutputGenerator()

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            # Get the idea from our young storytellers! 💡
            idea = request.form.get('idea')
            logger.info(f"🌟 We got a new idea: {idea}")

            if not idea:
                return jsonify({"error": "Oops! We need an idea to write a story!"})

            try:
                # Let's create our story! 📚
                story = story_writer.process(idea)
                output_generator.add_content("story", story)
                
                # Now, let's see how good our story is! 🧐
                evaluation = evaluator.process(story)
                output_generator.add_content("evaluation", evaluation)
                
                # Time to figure out who will love our story! 🎭
                marketing_analysis = marketing_expert.process(story)
                output_generator.add_content("marketing_analysis", marketing_analysis)  # Changed from 'marketing_persona' to 'marketing_analysis'
                
                # Let's create some cool social media posts! 📱
                social_media_content = social_media_team.process(story, marketing_analysis['personas'], marketing_analysis['target_audience'])
                output_generator.add_content("social_media_content", social_media_content)
                
                # And finally, let's come up with some awesome marketing ideas! 🎬
                marketing_concepts = marketing_team.process(story, marketing_analysis['personas'], marketing_analysis['target_audience'])
                output_generator.add_content("marketing_concepts", marketing_concepts)  # Changed from 'marketing_materials' to 'marketing_concepts'
                
                # Now, let's put it all together in one magical package! ✨
                response = output_generator.generate_output()
                
                return jsonify(response)
            except Exception as e:
                logger.error(f"🙀 Oh no! Something went wrong: {str(e)}")
                return jsonify({"error": f"Our storyteller got confused: {str(e)}"})

        # If it's not a POST request, let's show our magical story creation page!
        return render_template('index.html')

    return app

# If we're running this file directly, let's start our app!
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

print("🚀 Our magical story app is ready!")