# Gemini Chatbot

> A clean, production-ready AI assistant powered by Google's Gemini models and Streamlit.

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://python.org)
[![Framework: Streamlit](https://img.shields.io/badge/framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Why This Exists

Developers and students often need a rapid, lightweight way to interact with Google's advanced Gemini AI models without dealing with complex frontend setups. Gemini Chatbot provides a distraction-free, highly customizable interface out of the box, letting you brainstorm, research, and write code instantly.

## Quick Start

You can get the chatbot running locally in under a minute using Docker:

```bash
git clone https://github.com/GaneshArwan/gemini-chatbot.git
cd gemini-chatbot

# Add your Gemini API key
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Spin up the container
docker-compose up -d --build
```
> Navigate to `http://localhost:8501` in your browser.

## Features

- **Sidebar Configuration**: Instantly switch between `gemini-1.5-pro`, `gemini-1.5-flash`, and `gemini-1.0-pro`.
- **Temperature Control**: Fine-tune the AI's creativity directly from the UI.
- **Empty State UX**: A welcoming hero layout that provides prompt ideas before the conversation begins.
- **Session Management**: A dedicated "Clear Chat" button to seamlessly wipe the conversation context.
- **Resilient**: Gracefully handles API errors and empty prompts without crashing.

## Installation (Local Python)

If you prefer to run the app directly on your host machine instead of Docker:

**Prerequisites**: Python 3.12+

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GaneshArwan/gemini-chatbot.git
   cd gemini-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your environment:**
   Create a `.env` file in the root directory and add your Google Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Start the application:**
   ```bash
   streamlit run app.py
   ```
   > The app will be available at `http://localhost:8501`.

## Testing

This project uses `pytest` and `streamlit.testing` to guarantee UI stability and feature integrity.

To run the test suite:
```bash
pip install -r requirements-dev.txt
pytest tests/
```

## Contributing

Pull requests are welcome! When adding new features, please ensure that you add accompanying tests in the `tests/` directory.

## License

MIT © [Ganesh Arwan](https://github.com/GaneshArwan)
