# 📁 File: ai_story_marketing/ai_story_marketing/app.py

# 🎈 Welcome to our super cool Story Creation and Marketing App! 🚀
# This is where all the magic happens to turn your ideas into amazing stories!

# First, let's import all the tools we need 🧰
from flask import Flask, render_template, request, jsonify, send_file, flash, redirect, url_for, after_this_request, session
from flask.sessions import SessionInterface  # This helps us create our own way to remember things
from cachelib import FileSystemCache  # This is our new tool to store memories
import os
import time
from dotenv import load_dotenv
import markdown
import logging
import tempfile
from werkzeug.utils import secure_filename

# Import our special AI agents 🤖
from .agents.story_writer import StoryWriter
from .agents.evaluator import Evaluator
from .agents.story_improver import StoryImprover
from .agents.marketing_expert import MarketingExpert
from .agents.social_media_team import SocialMediaTeam
from .agents.marketing_team import MarketingTeam

# Import our AI models 🧠
from .models.llama_model import LlamaModel
from .models.gpt4_model import GPT4Model
from .models.claude_model import ClaudeModel

# Import our helpful utilities 🛠️
from .utils.output_generator import OutputGenerator
from .utils.pdf_generator import PDFGenerator

# Let's set up our app's secret hideout 🕵️‍♂️
load_dotenv()  # This loads all our secret codes from a special file

# Set up our magical app log 📜✨
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Now, let's create our Flask app - it's like a magic wand for websites! 🪄
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'my_secret_key')  # This is like a secret password for our app
app.config['SESSION_COOKIE_NAME'] = 'ai_story_session'  # This is the name of our special remember-me cookie

# 🧠 Let's set up our new way to remember things!
cache = FileSystemCache('/tmp/flask_session', threshold=500, default_timeout=60*60*24*7)

# 📝 This function converts Markdown to HTML
def convert_markdown_to_html(text):
    return markdown.markdown(text)

# This is our special way to remember things about each person using our app
class CachingSessionInterface(SessionInterface):
    def open_session(self, app, request):
        # When someone uses our app, we try to remember them
        sid = request.cookies.get(app.config['SESSION_COOKIE_NAME'])
        if sid:
            return cache.get(sid) or {}
        return {}

    def save_session(self, app, session, response):
        # We save what we need to remember about this person
        domain = self.get_cookie_domain(app)
        path = self.get_cookie_path(app)
        if session:
            if 'sid' not in session:
                session['sid'] = os.urandom(16).hex()
            cache.set(session['sid'], dict(session))
            response.set_cookie(app.config['SESSION_COOKIE_NAME'], session['sid'],
                                httponly=True, secure=self.get_cookie_secure(app),
                                domain=domain, path=path)

# We tell our app to use this special way of remembering
app.session_interface = CachingSessionInterface()

# Let's choose which AI brain we want to use 🧠
ai_model_name = os.getenv('AI_MODEL', 'llama')
logger.info(f"Using AI model: {ai_model_name}")

# Create the appropriate AI model based on the configuration
if ai_model_name == 'llama':
    model = LlamaModel()
elif ai_model_name == 'gpt4':
    model = GPT4Model()
elif ai_model_name == 'claude':
    model = ClaudeModel()
else:
    raise ValueError(f"Unsupported AI model: {ai_model_name}")

# Let's create all our special story-making friends 🧙‍♂️👥
story_writer = StoryWriter(model)
evaluator = Evaluator(model)
story_improver = StoryImprover(model)
marketing_expert = MarketingExpert(model)
social_media_team = SocialMediaTeam(model)
marketing_team = MarketingTeam(model)

# And let's not forget our magical notebook to write everything down 📓
output_generator = OutputGenerator()

# 🏃‍♂️ This is our function to keep track of our progress!
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
    if request.method == 'GET':
        # 🧹 Clear all session data when accessing the home page
        session.clear()

    if request.method == 'POST':
        # Someone gave us a new idea! Let's make a story! 💡
        idea = request.form.get('idea')
        if not idea:
            return jsonify({"error": "Oops! We need an idea to make a story!"})

        try:
            # Time to create our story! 📚
            logger.info(f"Generating story for idea: {idea}")
            story = story_writer.process(idea)
            
            if not story:
                logger.error("Story generation failed")
                return jsonify({"error": "Oh no! Our story machine couldn't create a story this time. Please try again!"})

            # Now, let's evaluate our story! 🔄
            logger.info("Evaluating story")
            evaluation = evaluator.process(story)
            
            session['story'] = story
            session['evaluation'] = evaluation
            track_progress(session, 'story_creation')
            track_progress(session, 'evaluation')

            return jsonify({"message": "Great! We've created your story. Let's make it even better!", "next": "/evaluate"})

        except Exception as e:
            logger.error(f"Error in story creation process: {str(e)}")
            return jsonify({"error": f"Oh no! Our story machine got confused: {str(e)}"})

    # If no one gave us an idea yet, let's just show the page where they can give us one
    return render_template('home.html')

# This is where we show how good our story is and ask if we should make it better 🌟
@app.route('/evaluate', methods=['GET', 'POST'])
def evaluate():
    if request.method == 'POST':
        choice = request.json.get('choice')
        if choice == 'continue':
            return jsonify({"success": True, "message": "Awesome! Let's create some marketing magic!", "next": "/market"})
        elif choice == 'rewrite':
            session.pop('story', None)
            session.pop('evaluation', None)
            session['progress'] = []
            return jsonify({"message": "No problem! Let's try again with a new story.", "next": "/"})

    story = session.get('story', '')
    evaluation = session.get('evaluation')
    logger.debug(f"Story for evaluation: {story[:50]}...")
    logger.debug(f"Evaluation: {evaluation}")
    
    if not story or not evaluation:
        logger.warning("Story or evaluation missing from session in evaluate route")
        return jsonify({"error": "Oops! We lost your story. Let's start over!", "next": "/"})

    # Convert Markdown to HTML for story and evaluation feedback
    story_html = convert_markdown_to_html(story)
    evaluation['feedback'] = convert_markdown_to_html(evaluation['feedback'])   

    return render_template('evaluate.html', 
                           story=story_html, 
                           evaluation=evaluation, 
                           progress=session.get('progress', []))

@app.route('/improve_story', methods=['POST'])
def improve_story():
    story = session.get('story')
    evaluation = session.get('evaluation')
    
    logger.debug(f"Original story: {story[:50] if story else 'None'}...")
    logger.debug(f"Original evaluation: {evaluation}")
    
    if not story or not evaluation:
        logger.warning("Story or evaluation missing from session")
        return jsonify({"error": "Oops! We lost your story or evaluation. Let's start over!", "next": "/"})
    
    try:
        improved_story = story_improver.process(story, evaluation['feedback'])
        logger.debug(f"Improved story: {improved_story[:50]}...")
        
        session['story'] = improved_story
        new_evaluation = evaluator.process(improved_story)
        logger.debug(f"New evaluation: {new_evaluation}")
        session['evaluation'] = new_evaluation
        
        track_progress(session, 'story_improvement')
        
        return jsonify({
            "message": "Great! We've improved your story. Let's see how it looks now!",
            "next": "/evaluate"
        })
    
    except Exception as e:
        logger.error(f"Error in story improvement process: {str(e)}", exc_info=True)
        return jsonify({"error": f"Oh no! Our story improver got confused: {str(e)}"})

# This is where we figure out who will love our story! 🎭
@app.route('/market', methods=['GET', 'POST'])
def market():
    if request.method == 'POST':
        track_progress(session, 'marketing')  # 🏃‍♂️ Let's track our marketing progress!
        return jsonify({"message": "Great! We've created your marketing plan. Let's see the whole package!", "next": "/result"})

    story = session.get('story')
    if not story:
       return jsonify({"success": False, "error": "Oops! We lost your story. Let's start over!", "next": "/"})

    try:
        # Time to figure out who will love our story! 🎭
        marketing_analysis = marketing_expert.process(story)
        logger.info(f"Marketing analysis result: {marketing_analysis}")
        
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
        logger.error(f"Error in marketing process: {str(e)}")
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

# This is where we create a PDF of everything we made! 📄
@app.route('/download-pdf')
def download_pdf():
    try:
        # Let's gather all the cool stuff we made
        story = session.get('story')
        evaluation = session.get('evaluation')
        marketing_analysis = session.get('marketing_analysis')
        social_media_content = session.get('social_media_content')
        marketing_concepts = session.get('marketing_concepts')

        # 🧐 Check if we have all the pieces we need
        if not all([story, evaluation, marketing_analysis, social_media_content, marketing_concepts]):
            # 😕 Uh-oh, something's missing!
            flash("Oops! We lost some of your data. Let's start over!", "error")
            return redirect(url_for('home'))

        # 🎨 Let's create our PDF!
        pdf_generator = PDFGenerator()
        content = {
            "story": story,
            "evaluation": evaluation,
            "marketing_analysis": marketing_analysis,
            "social_media_content": social_media_content,
            "marketing_concepts": marketing_concepts
        }
        
        # 📁 Create a temporary file with a secure filename
        temp_dir = tempfile.gettempdir()
        temp_filename = secure_filename(f"story_package_{int(time.time())}.pdf")
        pdf_path = os.path.join(temp_dir, temp_filename)
        
        try:
            pdf_generator.generate_pdf(content, pdf_path)
        except Exception as e:
            logger.error(f"Error generating PDF: {str(e)}")
            flash("Sorry, we couldn't create your PDF right now. Please try again later!", "error")
            return redirect(url_for('result'))

        if not os.path.exists(pdf_path):
            raise FileNotFoundError
        
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"Generated PDF file not found: {pdf_path}")
        
        # 📤 Now, let's send this PDF to be downloaded
        return send_file(pdf_path, as_attachment=True, download_name="your_story_package.pdf")

    except Exception as e:
        # 😱 Oh no! Something went wrong
        logger.error(f"Error generating PDF: {str(e)}")
        flash("Sorry, we couldn't create your PDF right now. Please try again later!", "error")
        return redirect(url_for('result')), 302

    finally:
        # 🧹 Clean up the PDF file after sending
        def cleanup_pdf(path):
            max_attempts = 5
            for attempt in range(max_attempts):
                try:
                    if os.path.exists(path):
                        os.remove(path)
                    break
                except PermissionError:
                    if attempt < max_attempts - 1:
                        time.sleep(0.1)  # Wait a bit before trying again
                    else:
                        logger.warning(f"Failed to delete temporary PDF file: {path}")

        # Schedule the cleanup to run after the response has been sent
        @after_this_request
        def cleanup(response):
            cleanup_pdf(pdf_path)
            return response

# This turns on our app when we're ready to play! 🎮
if __name__ == "__main__":
    app.run(debug=True)

# 🎉 Hooray! Our magical story app is ready to make some amazing stories! 🚀