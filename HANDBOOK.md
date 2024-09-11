# 📁 File: HANDBOOK.md

# 🍎 AI Story Creator and Marketing Helper: Teacher's Handbook

Welcome, teachers! This handbook will guide you through teaching your 5th-grade students how to build and use the AI Story Creator and Marketing Helper. Let's embark on this exciting journey of creativity and technology! 🚀

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [Learning Objectives](#learning-objectives)
3. [Prerequisite Knowledge](#prerequisite-knowledge)
4. [Lesson Plan Overview](#lesson-plan-overview)
5. [Detailed Lesson Plans](#detailed-lesson-plans)
6. [Additional Resources](#additional-resources)
7. [Troubleshooting Guide](#troubleshooting-guide)

## 1. Introduction

This project introduces students to the world of artificial intelligence, creative writing, and basic programming concepts. By the end of this course, students will have created their own AI-powered story creator and marketing tool!

## 2. Learning Objectives

By the end of this course, students will be able to:
- Understand basic concepts of AI and machine learning
- Write simple Python code and understand its structure
- Create and manipulate web pages using HTML and CSS
- Understand the basics of web applications and servers
- Develop creative writing skills with AI assistance
- Learn about marketing and social media concepts

## 3. Prerequisite Knowledge

Students should have basic computer skills, including:
- Using a web browser
- Basic typing skills
- Familiarity with file management (creating, saving, and opening files)

No prior programming experience is required, but an interest in technology and storytelling is beneficial!

## 4. Lesson Plan Overview

1. Introduction to AI and the Project (1 session)
2. Setting Up the Development Environment (1 session)
3. Creating the Story Writer Agent (2 sessions)
4. Building the Evaluator Agent (2 sessions)
5. Implementing the Story Improver Agent (2 sessions)
6. Developing the Marketing Expert Agent (2 sessions)
7. Creating the Social Media Team Agent (2 sessions)
8. Building the Marketing Team Agent (2 sessions)
9. Putting It All Together: The Main Application (3 sessions)
10. Testing and Debugging (2 sessions)
11. Final Project Showcase (1 session)

Total: 20 sessions (adjust as needed for your class schedule)

## 5. Detailed Lesson Plans

### Lesson 1: Introduction to AI and the Project

**Objective:** Introduce students to AI concepts and the project overview.

**Activities:**
1. Class discussion: What is AI? How do we interact with AI in daily life?
2. Introduce the AI Story Creator project and its components.
3. Brainstorming session: What kind of stories would students like to create?

**Homework:** Research and write a short paragraph about an AI application they find interesting.

### Lesson 2: Setting Up the Development Environment

**Objective:** Prepare students' computers for development.

**Activities:**
1. Install Python and Poetry (with IT support if needed).
2. Clone the project repository.
3. Set up the virtual environment using Poetry.
4. Run the basic "Hello, World!" Flask application.

**Homework:** Customize the "Hello, World!" application with their name.

### Lessons 3-4: Creating the Story Writer Agent

**Objective:** Implement the basic story writing functionality.

**Activities:**
1. Introduce the concept of "agents" in our AI system.
2. Explain the structure of the `story_writer.py` file.
3. Implement the `process` method to generate a basic story.
4. Test the Story Writer agent with various prompts.

**Homework:** Write a short story and think about how an AI might generate it.

### Lessons 5-6: Building the Evaluator Agent

**Objective:** Create an agent that can evaluate the quality of a story.

**Activities:**
1. Discuss what makes a good story (plot, characters, setting, etc.).
2. Implement the `process` method in `evaluator.py` to score stories.
3. Test the Evaluator agent with stories from the Story Writer.

**Homework:** Evaluate a classmate's story using criteria discussed in class.

### Lessons 7-8: Implementing the Story Improver Agent

**Objective:** Develop an agent that can suggest improvements to a story.

**Activities:**
1. Discuss common ways to improve a story (adding details, improving dialogue, etc.).
2. Implement the `process` method in `story_improver.py`.
3. Integrate the Story Improver with the Story Writer and Evaluator.

**Homework:** Improve a story provided by the teacher using techniques discussed in class.

### Lessons 9-10: Developing the Marketing Expert Agent

**Objective:** Create an agent that can analyze a story's target audience.

**Activities:**
1. Introduce basic marketing concepts (target audience, personas).
2. Implement the `process` method in `marketing_expert.py`.
3. Test the Marketing Expert agent with various stories.

**Homework:** Create a "persona" for their favorite book or movie's target audience.

### Lessons 11-12: Creating the Social Media Team Agent

**Objective:** Build an agent that generates social media content for stories.

**Activities:**
1. Discuss different social media platforms and their content styles.
2. Implement the `process` method in `social_media_team.py`.
3. Generate social media posts for student-written stories.

**Homework:** Create a social media post for their favorite book or movie.

### Lessons 13-14: Building the Marketing Team Agent

**Objective:** Develop an agent that creates marketing concepts for stories.

**Activities:**
1. Introduce various marketing materials (posters, trailers, etc.).
2. Implement the `process` method in `marketing_team.py`.
3. Generate marketing concepts for student-written stories.

**Homework:** Design a simple poster for their favorite book or movie.

### Lessons 15-17: Putting It All Together: The Main Application

**Objective:** Integrate all agents into a cohesive web application.

**Activities:**
1. Explain the structure of `app.py` and how it uses all the agents.
2. Implement the main routes and logic in `app.py`.
3. Create HTML templates for each page of the application.
4. Style the application using basic CSS.

**Homework:** Sketch a design for an additional feature they'd like to see in the app.

### Lessons 18-19: Testing and Debugging

**Objective:** Ensure the application works correctly and handle errors.

**Activities:**
1. Introduce the concept of testing in software development.
2. Write and run tests for each agent and the main application.
3. Identify and fix any bugs found during testing.

**Homework:** Write a test case for a specific function in the application.

### Lesson 20: Final Project Showcase

**Objective:** Celebrate student achievements and share their projects.

**Activities:**
1. Each student or group presents their AI Story Creator project.
2. Discuss challenges faced and how they were overcome.
3. Brainstorm ideas for future improvements or extensions of the project.

**Homework:** Write a reflection on what they learned from the project and how they might use AI in the future.

## 6. Additional Resources

- [Python for Kids](https://www.amazon.com/Python-Kids-Playful-Introduction-Programming/dp/1593274076)
- [AI for Kids](https://www.amazon.com/AI-Kids-Artificial-Intelligence-Project-Based/dp/1119696445)
- [Flask Web Development](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Creative Writing Prompts for Kids](https://www.journalbuddies.com/prompts-by-grade/creative-writing-prompts-for-kids/)

## 7. Troubleshooting Guide

Here are some common issues students might face and how to resolve them:

1. **Python installation issues:** Ensure you're using Python 3.11 or newer. Reinstall if necessary.
2. **Poetry problems:** Make sure Poetry is in the system PATH. Try restarting the computer after installation.
3. **Dependencies not installing:** Check internet connection. Try running `poetry update`.
4. **Application not starting:** Ensure all required environment variables are set in the `.env` file.
5. **AI model not responding:** Check API keys and model names in the `.env` file.

Remember, coding often involves troubleshooting. Encourage students to read error messages carefully and use them as clues to solve problems!

Happy teaching! 🍎✨