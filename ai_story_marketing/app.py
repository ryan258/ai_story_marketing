# 📁 File: ai_story_marketing/ai_story_marketing/app.py

# 🎈 Welcome to our super cool Story Creation and Marketing App! 🚀
# This is where all the magic happens to turn your ideas into amazing stories!

# First, let's import all the tools we need 🧰
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import os
from dotenv import load_dotenv
import markdown
from .agents.story_writer import StoryWriter
from .agents.evaluator import Evaluator
from .agents.marketing_expert import MarketingExpert
from .agents.social_media_team import SocialMediaTeam
from .agents.marketing_team import MarketingTeam
from .models.llama_model import LlamaModel
from .utils.output_generator import OutputGenerator

# Let's set up our app's secret hideout 🕵️‍♂️
load_dotenv()  # This loads all our secret codes from a special file

# Now, let's create our Flask app - it's like a magic wand for websites! 🪄
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'my_secret_key')  # This is like a secret password for our app
app.config['SESSION_TYPE'] = 'filesystem'  # This tells our app to remember things even when we close it
Session(app)  # This turns on the remembering power!

# Let's create all our special story-making friends 🧙‍♂️👥
model = LlamaModel()  # This is our magical AI brain
story_writer = StoryWriter(model)
evaluator = Evaluator(model)
marketing_expert = MarketingExpert(model)
social_media_team = SocialMediaTeam(model)
marketing_team = MarketingTeam(model)

# And let's not forget our magical notebook to write everything down 📓
output_generator = OutputGenerator()

# 🏃‍♂️ This is our new function to keep track of our progress!
def track_progress(session, step):
    if 'progress' not in session:
        session['progress'] = []
    if step not in session['progress']:
        session['progress'].append(step)

# 📝 This function converts Markdown to HTML
def convert_markdown_to_html(text):
    return markdown.markdown(text)

# This is the page you see when you first open our app 🏠
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Someone gave us a new idea! Let's make a story! 💡
        idea = request.form.get('idea')
        if not idea:
            return jsonify({"error": "Oops! We need an idea to make a story!"})

        try:
            # Time to create our story! 📚
            story = story_writer.process(idea)
            session['story'] = story  # Let's remember this story for later
            track_progress(session, 'story_creation')  # 🏃‍♂️ Let's track our progress!

            # Now, let's see how good our story is! 🧐
            evaluation = evaluator.process(story)
            session['evaluation'] = evaluation
            track_progress(session, 'evaluation')  # 🏃‍♂️ More progress!

            return jsonify({"message": "Great! We've created your story. Let's make it even better!", "next": "/evaluate"})

        except Exception as e:
            return jsonify({"error": f"Oh no! Our story machine got confused: {str(e)}"})

    # If no one gave us an idea yet, let's just show the page where they can give us one
    return render_template('home.html', progress=session.get('progress', []))

# This is where we show how good our story is and ask if we should make it better 🌟
@app.route('/evaluate', methods=['GET', 'POST'])
def evaluate():
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice == 'continue':
            return jsonify({"message": "Awesome! Let's create some marketing magic!", "next": "/market"})
        elif choice == 'rewrite':
            # They want a new story! Let's clear the old one and start over.
            session.pop('story', None)
            session.pop('evaluation', None)
            session['progress'] = []  # 🏃‍♂️ Let's reset our progress too!
            return jsonify({"message": "No problem! Let's try again with a new story.", "next": "/"})

    story = convert_markdown_to_html(session.get('story', ''))
    evaluation = session.get('evaluation')
    if not story or not evaluation:
        return jsonify({"error": "Oops! We lost your story. Let's start over!", "next": "/"})
    evaluation['feedback'] = convert_markdown_to_html(evaluation.get('feedback', ''))
    return render_template('evaluate.html', story=story, evaluation=evaluation, progress=session.get('progress', []))

# This is where we figure out who will love our story! 🎭
@app.route('/market', methods=['GET', 'POST'])
def market():
    if request.method == 'POST':
        track_progress(session, 'marketing')  # 🏃‍♂️ Let's track our marketing progress!
        return jsonify({"message": "Great! We've created your marketing plan. Let's see the whole package!", "next": "/result"})

    story = session.get('story')
    if not story:
        return jsonify({"error": "Oops! We lost your story. Let's start over!", "next": "/"})

    try:
        # Time to figure out who will love our story! 🎭
        marketing_analysis = marketing_expert.process(story)
        
        # Convert Markdown to HTML for marketing analysis
        marketing_analysis['target_audience'] = convert_markdown_to_html(marketing_analysis['target_audience'])
        marketing_analysis['personas'] = [convert_markdown_to_html(persona) for persona in marketing_analysis['personas']]
        
        session['marketing_analysis'] = marketing_analysis
        track_progress(session, 'marketing_analysis')  # 🏃‍♂️ More progress!

        # Let's create some cool social media posts! 📱
        social_media_content = social_media_team.process(story, marketing_analysis['personas'], marketing_analysis['target_audience'])
        session['social_media_content'] = social_media_content
        track_progress(session, 'social_media')  # 🏃‍♂️ We're getting there!

        # And finally, let's come up with some awesome marketing ideas! 🎬
        marketing_concepts = marketing_team.process(story, marketing_analysis['personas'], marketing_analysis['target_audience'])
        session['marketing_concepts'] = marketing_concepts
        track_progress(session, 'marketing_concepts')  # 🏃‍♂️ Almost done!

        return render_template('market.html', marketing_analysis=marketing_analysis, progress=session.get('progress', []))

    except Exception as e:
        return jsonify({"error": f"Oh no! Our marketing machine got confused: {str(e)}"})

# This is where we show everything we made! 🎉
@app.route('/result')
def result():
    # Let's gather all the cool stuff we made
    story = session.get('story')
    evaluation = session.get('evaluation')
    marketing_analysis = session.get('marketing_analysis')
    social_media_content = session.get('social_media_content')
    marketing_concepts = session.get('marketing_concepts')

    if not all([story, evaluation, marketing_analysis, social_media_content, marketing_concepts]):
        return jsonify({"error": "Oops! We lost some of your data. Let's start over!", "next": "/"})

    # Convert Markdown to HTML for all content
    story = convert_markdown_to_html(story)
    evaluation['feedback'] = convert_markdown_to_html(evaluation['feedback'])
    
    # Convert marketing analysis
    marketing_analysis['target_audience'] = convert_markdown_to_html(marketing_analysis['target_audience'])
    marketing_analysis['personas'] = [convert_markdown_to_html(persona) for persona in marketing_analysis['personas']]
    
    # Convert social media content
    for platform in social_media_content:
        social_media_content[platform] = convert_markdown_to_html(social_media_content[platform])
    
    # Convert marketing concepts
    for concept in marketing_concepts:
        marketing_concepts[concept] = convert_markdown_to_html(marketing_concepts[concept])

    # Now, let's put it all together in one magical package! ✨
    output_generator.add_content("story", story)
    output_generator.add_content("evaluation", evaluation)
    output_generator.add_content("marketing_analysis", marketing_analysis)
    output_generator.add_content("social_media_content", social_media_content)
    output_generator.add_content("marketing_concepts", marketing_concepts)

    result = output_generator.generate_output()

    return render_template('result.html', result=result, progress=session.get('progress', []))

# This turns on our app when we're ready to play! 🎮
if __name__ == "__main__":
    app.run(debug=True)

# 🎉 Hooray! Our magical story app is ready to make some amazing stories! 🚀