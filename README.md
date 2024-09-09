# File: ai_story_marketing/README.md

# AI-Driven Story Creation and Marketing System

This system takes a simple idea input and generates a comprehensive story and marketing package using a chain of AI agents.

## Project Structure

```
ai_story_marketing/
├── pyproject.toml
├── poetry.lock
├── .env
├── README.md
├── ai_story_marketing/
│   ├── __init__.py
│   ├── main.py
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
│   │   ├── gpt4_model.py
│   │   ├── claude_model.py
│   │   └── llama_model.py
│   ├── ui/
│   │   ├── __init__.py
│   │   └── app.py
│   └── utils/
│       ├── __init__.py
│       ├── context_manager.py
│       └── output_generator.py
└── tests/
    └── __init__.py
```

## Main Components

1. **Agents**: Each agent (StoryWriter, Evaluator, MarketingExpert, SocialMediaTeam, MarketingTeam) inherits from BaseAgent and specializes in a specific task.
   - Implemented (All agents are now functional)

2. **Models**: Interfaces for different AI models (GPT-4, Claude, Llama) that can be used by the agents.

3. **UI**: A Flask-based web interface for interacting with the system.

4. **Utils**: Utility classes including ContextManager for maintaining context across agents and OutputGenerator for compiling the final output.
   - Partially implemented (ContextManager functionality included in BaseAgent)

5. **LlamaModel**: A simplified, educational version of an AI model for story generation.

## Setup

1. Ensure you have Python 3.8+ installed.
2. Install Poetry: `pip install poetry`
3. Clone this repository and navigate to the project directory.
4. Install dependencies: `poetry install`
5. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Fill in the required API keys and configuration values

## Usage

1. Activate the Poetry environment: `poetry shell`
2. Run the application: `python ai_story_marketing/main.py`
3. Open a web browser and navigate to `http://localhost:5000`
4. Enter your idea and follow the prompts to generate your story and marketing package.

## Development

- To run tests: `poetry run pytest`
- To run tests with verbose output: `poetry run pytest -v -s`
- To add new dependencies: `poetry add <package-name>`
- Tests implemented for all main components

## Main Features

- Story Creation: Generates a simple story based on user input.
- Story Evaluation: Provides a placeholder evaluation of the generated story.
- Marketing Persona Creation: Creates placeholder target audience personas.
- Social Media Content Generation: Generates placeholder content for various social media platforms.
- Marketing Material Creation: Generates placeholder concepts for marketing campaigns.
- Comprehensive Output: Compiles all generated content into a single JSON response.

## Educational Note

This project uses a simplified version of an AI model (LlamaModel) for educational purposes. In a real-world scenario, we would integrate with actual machine learning models.


## Technology Stack

- Backend: Python
- Frontend: Flask, TailwindCSS
- AI Models: Simplified educational implementation (LlamaModel)
- Project Management: Poetry
- PDF Generation: FPDF

## Future Improvements

- Implement more sophisticated AI model interactions with real machine learning models
- Enhance the web interface with real-time updates
- Add support for image generation in marketing materials
- Implement user accounts and project saving functionality
- Implement comprehensive error handling and logging

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
