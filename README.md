# TadiAI

> A personalized AI chat assistant powered by Google's Gemini API. TadiAI is a Flask web application that provides a clean browser interface for conversing with an AI that adapts to your communication style and personality.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.1%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Architecture](#architecture)
- [Troubleshooting](#troubleshooting)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Features

✨ **Core Features**

- 🤖 **AI-Powered Chat** - Leverage Google's Gemini API for intelligent conversations
- 🎯 **Personalized Responses** - Configure the AI to match your communication style and personality
- 💬 **Conversation History** - Maintains context across conversations (last 20 messages)
- 🌐 **Web Interface** - Clean, modern browser-based chat UI
- ⚡ **Real-Time Responses** - Instant message processing and replies
- 🔐 **API-Based Architecture** - RESTful backend API for scalability
- 🛠️ **Easy Configuration** - Simple environment variable setup
- 📱 **Responsive Design** - Works on desktop and mobile browsers

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8** or higher
- **pip** (Python package manager)
- **Git** (optional, for cloning the repository)
- A modern web browser (Chrome, Firefox, Safari, Edge)
- **Google Gemini API Key** ([Get one here](https://aistudio.google.com/app/apikeys))

## Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd TadiAI
```

Or download and extract the ZIP file.

### Step 2: Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**

- `Flask==3.1.3` - Web framework
- `google-genai==2.19.0` - Google Gemini API client
- `python-dotenv==1.1.1` - Environment variable management

### Step 4: Set Up Environment Variables

1. Copy `.env.example` to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your credentials:

   ```env
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   FLASK_DEBUG=1
   PORT=5000
   ```

   - `GEMINI_API_KEY`: Your Google Gemini API key
   - `FLASK_DEBUG`: Set to `1` for development mode (auto-reload on changes)
   - `PORT`: The port to run the Flask server on (default: 5000)

## Quick Start

### Running the Application

```bash
python main.py
```

The application will start on `http://localhost:5000`

### Accessing the Chat

1. Open your browser
2. Navigate to `http://localhost:5000`
3. Start typing messages and chat with TadiAI!

### Example Conversation

```text
You: Hello! What can you help me with?
TadiAI: [Response based on your configured personality]

You: Tell me about Python
TadiAI: [Personalized response about Python]
```

## Project Structure

```text
TadiAI/
├── main.py                          # Application entry point
├── run.py                           # Alternative runner
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
├── README.md                        # This file
│
├── app/
│   ├── __init__.py                 # Flask app factory & configuration
│   ├── routes.py                   # Web & API route handlers
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── gemini.py               # Gemini API integration logic
│   │
│   └── templates/
│       └── index.html              # Frontend chat interface
```

### File Descriptions

| File | Purpose |
| --- | --- |
| `main.py` | Entry point that creates and runs the Flask application |
| `app/__init__.py` | Flask app factory, loads environment variables |
| `app/routes.py` | Defines HTTP routes: `/` (chat page) and `/api/chat` (API endpoint) |
| `app/services/gemini.py` | Handles Gemini API integration and message generation |
| `app/templates/index.html` | Frontend UI for the chat interface |
| `requirements.txt` | Lists all Python package dependencies |
| `.env.example` | Template for environment configuration |

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required: Your Google Gemini API Key
GEMINI_API_KEY=your_actual_key_here

# Optional: Flask debug mode (1 = enabled, 0 = disabled)
FLASK_DEBUG=1

# Optional: Server port (default: 5000)
PORT=5000
```

### Customizing AI Personality

Edit `app/services/gemini.py` to customize how the AI responds:

```python
PERSONALITY = """
You are replying in the user's personal style. Use these personality details:
- Your communication tone (e.g., formal, casual, humorous)
- Key personality traits
- Your favorite expressions and phrases
- Response guidelines and values
"""
```

**Customization Options:**

- **Tone**: Set the conversational style (formal, casual, friendly, etc.)
- **Traits**: Define personality characteristics
- **Expressions**: Add common phrases you use
- **Guidelines**: Specify how the AI should respond to certain topics

### Model Configuration

The app uses `gemini-3.6-flash` by default. To change the model:

```python
# In app/services/gemini.py
MODEL_NAME = "gemini-3.6-flash"  # Change this to another model
```

Available models: Check [Google Gemini documentation](https://ai.google.dev/models)

## Usage

### Starting the Server

```bash
# Development mode (with hot reload)
python main.py

# Production mode
FLASK_DEBUG=0 python main.py
```

### Using the Chat Interface

1. **Send a Message**: Type in the input field at the bottom and press Enter or click Send
2. **View History**: The chat maintains your conversation history
3. **Clear Chat**: Refresh the page to start a new conversation

### Advanced Usage

#### Accessing the Chat API

The app provides a REST API endpoint for programmatic access:

**Endpoint**: `POST /api/chat`

**Request:**

```json
{
  "message": "Your message here",
  "history": [
    {"role": "user", "text": "Previous user message"},
    {"role": "model", "text": "Previous AI response"}
  ]
}
```

**Response:**

```json
{
  "response": "The AI's response to your message"
}
```

**Error Responses:**

```json
{"error": "Enter a message first."}
```

## API Endpoints

### GET /

Serves the chat interface HTML page.

**Response:** HTML chat page

---

### POST /api/chat

Processes a chat message and returns an AI response.

**Request Body:**

```json
{
  "message": "string",
  "history": [
    {"role": "user" | "model", "text": "string"}
  ]
}
```

**Response (200 OK):**

```json
{
  "response": "AI's response text"
}
```

**Response (400 Bad Request):**

```json
{
  "error": "Error message"
}
```

**Response (429 Too Many Requests):**

```json
{
  "error": "The AI usage limit has been reached. Please try again later..."
}
```

**Response (502 Bad Gateway):**

```json
{
  "error": "Gemini could not respond. Check the server logs."
}
```

## Architecture

### Application Flow

```text
┌─────────────────┐
│   Browser UI    │
│  (index.html)   │
└────────┬────────┘
         │
         │ HTTP POST /api/chat
         │
┌────────▼─────────────────┐
│   Flask Backend           │
│  - routes.py: API handler │
│  - Validates input        │
└────────┬─────────────────┘
         │
         │ Prepare request
         │
┌────────▼──────────────────────┐
│  Gemini Service               │
│  - gemini.py                  │
│  - Manages conversation state │
│  - Formats messages           │
└────────┬───────────────────────┘
         │
         │ API call
         │
┌────────▼──────────────────┐
│   Google Gemini API       │
│   (Cloud)                 │
└────────┬──────────────────┘
         │
         │ Response
         │
┌────────▼──────────────────┐
│  Response Processing      │
│  - Error handling         │
│  - Format conversion      │
└────────┬──────────────────┘
         │
         │ JSON response
         │
┌────────▼─────────────────┐
│   Browser (Update UI)    │
│   Display AI response    │
└──────────────────────────┘
```

### Key Components

- **Frontend**: HTML/CSS/JavaScript interface (`app/templates/index.html`)
- **Backend API**: Flask routes handling HTTP requests (`app/routes.py`)
- **Service Layer**: Gemini API integration (`app/services/gemini.py`)
- **Configuration**: Flask app factory and setup (`app/__init__.py`)

## Troubleshooting

### Issue: "GEMINI_API_KEY is not configured"

**Solution:**

1. Create `.env` file in the project root
2. Add your API key: `GEMINI_API_KEY=your_key_here`
3. Restart the application

### Issue: Module not found error (e.g., "No module named 'flask'")

**Solution:**

```bash
# Activate your virtual environment first
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Then install dependencies
pip install -r requirements.txt
```

### Issue: "Connection refused" or port already in use

**Solution:**

```bash
# Use a different port
PORT=8000 python main.py

# Or kill the process using the current port
# On Windows: netstat -ano | findstr :5000
# On macOS/Linux: lsof -i :5000
```

### Issue: 429 Error - "AI usage limit has been reached"

**Solution:**

- You've hit the Google Gemini API rate limit
- Wait a few minutes and try again
- Check your API plan at [Google AI Studio](https://aistudio.google.com)
- Upgrade your API plan if needed

### Issue: Chat responses are not personalized

**Solution:**

1. Edit the `PERSONALITY` variable in `app/services/gemini.py`
2. Restart the application
3. Start a new chat conversation for changes to take effect

### Issue: Browser shows blank page or errors

**Solution:**

1. Check the browser console (F12 → Console tab) for errors
2. Check the Flask server logs in the terminal
3. Verify the server is running on the expected port
4. Clear browser cache and refresh (Ctrl+Shift+Delete)

## Development

### Running in Development Mode

```bash
# With auto-reload on file changes
FLASK_DEBUG=1 python main.py
```

### Running Tests (if available)

```bash
pytest
```

### Code Structure Best Practices

- Keep route handlers in `app/routes.py`
- Place business logic in `app/services/`
- Store templates in `app/templates/`
- Use environment variables for configuration

### Making Changes

1. Modify files in the `app/` directory
2. With `FLASK_DEBUG=1`, changes auto-reload
3. Refresh the browser to see updates
4. Check the terminal for error messages

## Contributing

Contributions are welcome! Here's how to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Guidelines

- Follow PEP 8 Python style guide
- Add comments for complex logic
- Test your changes before submitting
- Update documentation as needed

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Support

For issues, questions, or suggestions:

- Open an issue on the repository
- Check existing issues for solutions
- Review the Troubleshooting section above

## Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Powered by [Google Gemini API](https://ai.google.dev/)
- Python community for amazing libraries

---

**Last Updated**: August 2026
