# 🚀 AI-Driven Story Creation and Marketing System

Welcome to our AI-Driven Story Creation and Marketing System! This project takes a simple idea input and generates a comprehensive story and marketing package using a chain of AI agents.

## ✨ Features

- 📝 Story creation from a simple idea input
- 🧐 Story evaluation
- 🎭 Marketing persona creation
- 📱 Social media content generation
- 🎨 Marketing concept creation
- 🏃‍♂️ Progress tracking
- 📝 Markdown rendering for all generated content
- 📊 Comprehensive output generation

## 🛠️ Technology Stack

- Backend: Python 🐍
- Web Framework: Flask 🌶️
- Frontend: HTML, TailwindCSS 🎨
- AI Model: LlamaModel (simplified version for educational purposes) 🦙
- Testing: pytest 🧪
- Project Management: Poetry 📦
- Markdown Processing: Python-Markdown 📝
- Environment Variable Management: python-dotenv 🔐

## 🏗️ Setup

1. Ensure you have Python 3.11+ installed.
2. Install Poetry if you haven't already:
   ```
   pip install poetry
   ```
3. Clone this repository:
   ```
   git clone https://github.com/yourusername/ai-story-marketing.git
   cd ai-story-marketing
   ```
4. Install dependencies:
   ```
   poetry install
   ```
5. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Fill in any required API keys or configuration values

## 🚀 Running the Application

1. Activate the Poetry environment:
   ```
   poetry shell
   ```
2. Run the Flask application:
   ```
   python ai_story_marketing/app.py
   ```
3. Open a web browser and navigate to `http://127.0.0.1:5000`

## 🧪 Running Tests

To run the test suite:

```
pytest
```

To run tests with verbose output:

```
pytest -v
```

## 📁 Project Structure

```
ai_story_marketing/
├── pyproject.toml
├── poetry.lock
├── .env
├── README.md
├── ai_story_marketing/
│   ├── __init__.py
│   ├── app.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base_agent.py
│   │   ├── story_writer.py
│   │   ├── evaluator.py
│   │   ├── marketing_expert.py
│   │   ├── social_media_team.py
│   │   └── marketing_team.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── llama_model.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── evaluate.html
│   │   ├── market.html
│   │   └── result.html
│   └── utils/
│       ├── __init__.py
        ├── context_manager.py
│       └── output_generator.py
└── tests/
    ├── __init__.py
    ├── test_app.py
    ├── test_evaluator.py
    ├── test_marketing_expert.py
    ├── test_marketing_team.py
    ├── test_social_media_team.py
    ├── test_progress_tracking.py
    └── test_llama_model.py
```

## 👥 Contributing

We welcome contributions to this project! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Submit a pull request

Please make sure to update tests as appropriate and adhere to the existing coding style.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy story creating! If you have any questions or run into any issues, please open an issue on the GitHub repository. 📚✨