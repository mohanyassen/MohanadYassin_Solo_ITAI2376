# Smart AI Health Assistant 🤖

## Project Title

Smart AI Health Assistant

---

## One Sentence Description

A simple AI health assistant that provides wellness advice, nutrition information, and basic health tracking using a rule-based AI agent system with tools and memory.

---

## Team Information

Solo Project — Mohanad Yassin

---

## Problem Statement

Many people struggle with maintaining healthy habits such as proper sleep, hydration, stress management, and nutrition awareness. This project provides a simple AI assistant that helps users receive general wellness guidance and track basic health information.

---

## Target Users

* Individuals interested in improving daily wellness habits
* Students and busy adults needing quick health reminders
* Users who want a lightweight personal wellness assistant

---

## Chosen Option

Option A — Single AI Agent

The original midterm proposal included advanced AI models and wearable integrations. For the final implementation, the project was simplified into a reliable and beginner-friendly single-agent system focused on health guidance, memory, and tool usage.

---

# Architecture Overview

The Smart AI Health Assistant uses a simple AI agent workflow that processes user input, selects the appropriate tool, checks memory, and returns a response.

### System Flow

User Input → AI Agent → Tool Selection → Memory Check → Response

### Tools Used

* Nutrition Tool
* Health Advice Tool

### Memory System

The system stores user information such as weight and sleep data locally using a JSON memory file.

### Reasoning Pattern

The assistant uses a rule-based reasoning structure inspired by ReAct-style agent systems:

1. Analyze user input
2. Decide which tool to use
3. Execute the tool
4. Return a response

---

# Frameworks and Technologies Used

## Programming Language

* Python 3.13

## Tools & Technologies

* Python
* JSON Memory Storage
* Rule-based AI Agent Design

## Libraries

* langchain
* openai
* requests
* python-dotenv

---

# Installation Instructions

## Step 1 — Install Python

Install Python 3.13 or newer.

Download:
https://www.python.org/downloads/

---

## Step 2 — Install Required Packages

Open terminal in the project folder and run:

```bash
pip install langchain openai python-dotenv requests
```

---

## Step 3 — Project Structure

The project structure should look like this:

```text
health-agent/
│
├── main.py
├── memory.json
├── README.md
├── REFLECTION.md
│
├── src/
│   ├── agent.py
│   ├── tools.py
│   ├── memory.py
│
└── demo/
```

---

# How to Run the Project

Open terminal in the project folder and run:

```bash
py main.py
```

The assistant will start and display:

```text
Smart Health Assistant AI 🤖
You:
```

---

# Example Usage

## Scenario 1 — Health Advice

User:

```text
I feel tired
```

Agent:

```text
You may need more sleep (7–9 hours). Drink water and rest.
```

---

## Scenario 2 — Nutrition Tool

User:

```text
Calories in banana
```

Agent:

```text
Banana has about 105 calories.
```

---

## Scenario 3 — Memory System

User:

```text
My weight is 180
```

Agent:

```text
Got it — I saved your weight.
```

---

# Features

* Basic wellness advice
* Nutrition calorie lookup
* Stress and fatigue suggestions
* Local memory storage
* Tool-based reasoning system
* Interactive terminal chat interface

---

# Deep Learning Connection

Although this implementation uses a simplified rule-based design, it connects to concepts learned in ITAI 2376:

* AI Agent architecture
* Reasoning and action workflows
* Retrieval and memory systems
* Transformer-inspired conversational flow
* Health-assistant AI concepts from the original blueprint

The original blueprint proposed CNNs and Transformers. The final version focuses on implementing a working AI agent system with tools and memory.

---

# Known Limitations

* No real large language model integration
* Limited nutrition database
* Rule-based responses only
* No voice input support
* No real medical diagnosis capability
* No wearable device integration

---

# Future Improvements

* Add OpenAI GPT integration
* Expand food and nutrition database
* Add wearable API integrations
* Improve memory and personalization
* Add voice assistant capabilities
* Add graphical user interface (GUI)

---

# Demo Video

Demo video available here:

https://github.com/mohanyassen/MohanadYassin_Solo_ITAI2376/releases/tag/v1.0

---

# Repository Information

GitHub Repository Naming Convention:

```text
MohanadYassin_Solo_ITAI2376
```

---

# Academic Integrity Statement

This project was designed and implemented as an original student project for ITAI 2376. AI tools and coding assistants were used for guidance and learning support during development.

---

# Final Notes

This project demonstrates the core structure of an AI agent system using tools, memory, and reasoning patterns in a beginner-friendly implementation.
