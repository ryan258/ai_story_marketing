# 📁 File: ai_story_marketing/ai_story_marketing/main.py

# 🎉 Welcome to our AI Story Marketing application! 🚀
# This is where our adventure begins! 🌟

# 📚 First, we need to bring in some helpful tools
from flask import Flask, render_template, request  # This helps us make a web application
from dotenv import load_dotenv  # This lets us use secret information safely
import os  # This helps us work with files and folders

# 🧙‍♂️ We'll import our magical AI agents here (we'll create these later!)
# from agents.story_writer import StoryWriter
# from agents.evaluator import Evaluator
# from agents.marketing_expert import MarketingExpert
# from agents.social_media_team import SocialMediaTeam
# from agents.marketing_team import MarketingTeam

# 🔧 Let's set up our application
def create_app():
    # 🏗️ Create our Flask app (it's like building a castle!)
    app = Flask(__name__)
    
    # 🔐 Load our secret information
    load_dotenv()
    
    # 🌐 This is what happens when someone visits our website
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            # 🎭 TODO: Handle the user's idea submission
            # We'll add more code here later!
            pass
        return render_template('index.html')  # Show our homepage
    
    # 🏰 Return our finished app
    return app

# 🏁 This is where our program starts running
if __name__ == "__main__":
    # 🚀 Launch our app!
    app = create_app()
    app.run(debug=True)  # The 'debug=True' part helps us see errors

# 🧪 Let's add some tests to make sure our app works correctly
def test_create_app():
    # 🏗️ Create a test version of our app
    app = create_app()
    
    # 🕵️ Check if our app was created successfully
    assert app is not None, "App should be created"
    
    # 🌐 Make sure our homepage works
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200, "Homepage should be accessible"

# 🎉 Hooray! We've set up the basic structure of our application!
# Next, we'll create our AI agents and add more exciting features! 🚀