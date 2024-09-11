# 📁 File: README.md

# 🚀 AI Story Creator and Marketing Helper

Hey there, young storytellers! 👋 Welcome to our super cool AI Story Creator and Marketing Helper! This awesome project takes your amazing ideas and turns them into fantastic stories with the help of some friendly AI robots! 🤖✨

## ✨ What Can It Do?

- 📝 Create awesome stories from your ideas
- 🧐 Check how good the stories are
- 🚀 Make stories even better with smart suggestions
- 🎭 Figure out who would love to read your stories
- 📱 Make cool posts for social media about your stories
- 🎨 Come up with fun ways to tell people about your stories
- 🏃‍♂️ Keep track of how far along your story is with a cool progress bar
- 📝 Turn computer language into human language
- 📊 Put all the cool stuff together in one place
- 🧠 Use different smart AI brains to help (like Llama, GPT-4, and Claude)
- 📄 Make a fancy PDF of your story and marketing plan

## 🛠️ What We Used to Build It

- Backend: Python (it's like the brain of our project) 🐍
- Web Stuff: Flask (it helps make websites) 🌶️
- Pretty Designs: HTML and TailwindCSS (to make everything look cool) 🎨
- Smart AI Helpers: LlamaModel, GPT4Model, ClaudeModel (they're like different flavors of AI) 🦙🤖🧠
- Testing: pytest (to make sure everything works right) 🧪
- Project Helper: Poetry (it keeps all our computer tools organized) 📦
- Special Language Helper: Python-Markdown (it makes computer words look nice) 📝
- Secret Keeper: python-dotenv (it keeps our secrets safe) 🔐
- PDF Maker: ReportLab (it turns our stories into fancy PDFs) 📄

## 🏗️ How to Set It Up

1. Make sure you have Python 3.11 or newer on your computer.
2. Ask a grown-up to help you install Poetry:
   ```
   pip install poetry
   ```
3. Get our project from the internet:
   ```
   git clone https://github.com/ryan258/ai-story-marketing.git
   cd ai-story-marketing
   ```
4. Install all the tools we need:
   ```
   poetry install
   ```
5. Set up some secret codes:
   - Copy the file named `.env.example` and rename it to `.env`
   - Ask a teacher or parent to help you fill in the secret codes

## 🔄 How to Choose Different AI Helpers

We have three super smart AI friends to help us: Llama, GPT-4, and Claude. Here's how to pick which one you want to use:

### To Use Llama 🦙

1. Open the `.env` file.
2. Write these magic words in it:
   ```
   AI_MODEL=llama
   API_URL=http://localhost:11434/api/generate
   MODEL_NAME=llama3.1:latest
   ```
3. Make sure Ollama is installed and running on your computer.

### To Use GPT-4 🤖

1. Open the `.env` file.
2. Write these magic words in it:
   ```
   AI_MODEL=gpt4
   OPENAI_MODEL_NAME=gpt-4o-mini-2024-07-18
   OPENAI_API_KEY=your-secret-key-here
   ```
3. Ask a grown-up to help you get a secret key from OpenAI.

### To Use Claude 🧠

1. Open the `.env` file.
2. Write these magic words in it:
   ```
   AI_MODEL=claude
   ANTHROPIC_API_KEY=your-secret-key-here
   ANTHROPIC_MODEL_NAME=claude-3-opus-20240229
   ```
3. Ask a grown-up to help you get a secret key from Anthropic.

## 🚀 How to Start the Story Creator

1. Turn on the special Poetry world:
   ```
   poetry shell
   ```
2. Start the Story Creator:
   ```
   python -m ai_story_marketing.app
   ```
3. Open your web browser and go to `http://127.0.0.1:5000`

## 🧪 How to Check If Everything Works

To make sure everything is working right:

```
pytest
```

If you want to see more details:

```
pytest -v
```

## 📁 What's Inside Our Project

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
│   │   ├── story_improver.py
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
    ├── test_story_improver.py
    ├── test_progress_tracking.py
    ├── test_llama_model.py
    ├── test_gpt4_model.py
    └── test_claude_model.py
```

## 👥 How to Help Make It Better

We love when people help make our project even cooler! Here's how you can help:

1. Make a copy of the project (called "forking")
2. Create a new branch: `git checkout -b cool-new-feature`
3. Make your awesome changes and save them: `git commit -m 'Add some cool feature'`
4. Send your changes to your copy: `git push origin cool-new-feature`
5. Ask us to add your changes to our project (called a "pull request")

Remember to update the tests if you change anything, and try to write your code neatly like we did!

## 📄 Rules for Using Our Project

This project is free to use, change, and share under the MIT License. You can find all the rules in the [LICENSE](LICENSE) file.

## 🆘 Need Help?

If you have any questions or run into any problems, just let us know by opening an "issue" on our GitHub page. We're here to help!

---

Have fun creating amazing stories! Remember, every great writer started with a single idea. Now you have a whole team of AI friends to help bring your ideas to life! Happy storytelling! 📚✨