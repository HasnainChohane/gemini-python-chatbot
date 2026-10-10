# Gemini Python Chatbot

A lightweight, interactive Command Line Interface (CLI) chatbot built with Python using the official Google Gen AI SDK and python-dotenv for secure environment variable management. 

Powered by the highly efficient gemini-3.8-flash model, this terminal-based application retains conversation context across turns.

---

## Features

- **Contextual Awareness:** Uses client.chats.create to remember previous conversational turns.
- **Secure Configuration:** Environment variables are strictly kept out of source code via .env files.
- **Instant Output:** Built with output flushing to ensure rapid response delivery directly to your terminal.

---

## Installation and Setup

Follow these steps to run the chatbot locally on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com
cd gemini-python-chatbot
```

### 2. Install Dependencies
Install the required packages using pip:
```bash
pip install google-genai python-dotenv
```

### 3. Configure the Environment
Create a .env file in the root directory of the project:
```bash
# On Linux/macOS
touch .env

# On Windows (Command Prompt)
type nul > .env
```

Open the .env file and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

*(Note: The .env file is explicitly included in the .gitignore to prevent secret leaking.)*

---

## Usage

Start the interactive session by running the main Python script:

```bash
python gemini.py
```

- Type your query and press Enter to receive a response from Gemini.
- Type exit at any time to gracefully terminate the application.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
