# File: ai_story_marketing/ai_story_marketing/main.py

from ui.app import create_app

def main():
    app = create_app()
    app.run()

if __name__ == "__main__":
    main()