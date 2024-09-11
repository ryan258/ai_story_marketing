# 🚀 AI-Driven Story Creation and Marketing System

Welcome to our AI-Driven Story Creation and Marketing System! This project takes a simple idea input and generates a comprehensive story and marketing package using a chain of AI agents.

## ✨ Features

- 📝 Story creation from a simple idea input
- 🧐 Story evaluation and improvement
- 🎭 Marketing persona creation
- 📱 Social media content generation
- 🚀 Iterative story improvement
- 🎨 Marketing concept creation
- 🏃‍♂️ Progress tracking
- 📝 Markdown rendering for all generated content
- 📊 Comprehensive output generation
- 🔄 Support for multiple AI models (Llama, GPT-4, and Claude)
- 📄 PDF generation of the final output

## 🛠️ Technology Stack

- Backend: Python 🐍
- Web Framework: Flask 🌶️
- Frontend: HTML, TailwindCSS 🎨
- AI Models: LlamaModel, GPT4Model, ClaudeModel 🦙🤖🧠
- Testing: pytest 🧪
- Project Management: Poetry 📦
- Markdown Processing: Python-Markdown 📝
- Environment Variable Management: python-dotenv 🔐
- PDF Generation: ReportLab 📄

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
   - Fill in the required API keys and configuration values

## 🔄 Switching Between AI Models

This project supports three AI models: Llama, GPT-4, and Claude. Here's how to switch between them:

### Using Llama

1. Open your `.env` file.
2. Set the following variables:
   ```
   AI_MODEL=llama
   API_URL=http://localhost:11434/api/generate
   MODEL_NAME=llama3.1:latest
   ```
3. Make sure you have Ollama installed and running locally.

### Using GPT-4

1. Open your `.env` file.
2. Set the following variables:
   ```
   AI_MODEL=gpt4
   OPENAI_MODEL_NAME=gpt-4o-mini-2024-07-18
   OPENAI_API_KEY=your-openai-api-key-here
   ```
3. Replace `your-openai-api-key-here` with your actual OpenAI API key.

### Using Claude

1. Open your `.env` file.
2. Set the following variables:
   ```
   AI_MODEL=claude
   ANTHROPIC_API_KEY=your-anthropic-api-key-here
   ANTHROPIC_MODEL_NAME=claude-3-opus-20240229
   ```
3. Replace `your-anthropic-api-key-here` with your actual Anthropic API key.

## 🚀 Running the Application

1. Activate the Poetry environment:
   ```
   poetry shell
   ```
2. Run the Flask application:
   ```
   python -m ai_story_marketing.app
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
│   │   ├── llama_model.py
│   │   ├── gpt4_model.py
│   │   └── claude_model.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── evaluate.html
│   │   ├── market.html
│   │   └── result.html
│   └── utils/
│       ├── __init__.py
│       ├── context_manager.py
│       ├── output_generator.py
│       └── pdf_generator.py
└── tests/
    ├── __init__.py
    ├── test_app.py
    ├── test_evaluator.py
    ├── test_marketing_expert.py
    ├── test_marketing_team.py
    ├── test_social_media_team.py
    ├── test_progress_tracking.py
    ├── test_llama_model.py
    ├── test_gpt4_model.py
    └── test_claude_model.py
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