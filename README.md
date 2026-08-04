# 🤖 Telegram AI Pipeline Bot

An AI-powered Telegram chatbot built using **Python**, **Telegram Bot API**, **Groq LLM**, and **Hugging Face Transformers**. The bot provides intelligent conversations along with multiple Natural Language Processing (NLP) capabilities such as sentiment analysis, text summarization, text generation, translation, and zero-shot text classification.

---

# 📌 Project Overview

This project demonstrates the integration of a Large Language Model (Groq LLM) and Hugging Face Transformers with the Telegram Bot API. Users can interact with an AI chatbot for general conversations or use specialized NLP pipelines through simple Telegram commands.

The project follows a modular software engineering architecture with separate modules for AI pipelines, logging, configuration management, and conversation memory, making it scalable and easy to maintain.

---

# ✨ Features

- 🤖 AI Chat using Groq LLM
- 😊 Sentiment Analysis
- 📝 Text Summarization
- ✍️ Text Generation
- 🌍 English → French Translation
- 🏷️ Zero-Shot Text Classification
- 💬 Context-aware AI conversations
- 🧠 Multi-user conversation memory
- 📜 Chat logging with timestamps
- 🧹 Clear conversation history
- ⚙️ Lazy loading of Hugging Face models
- 🔐 Environment variable support (.env)
- ⚠️ Error handling
- 📂 Modular project architecture

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Backend Development |
| Telegram Bot API | Telegram Integration |
| python-telegram-bot | Telegram Library |
| Groq API | Conversational AI |
| Hugging Face Transformers | NLP Pipelines |
| PyTorch | Deep Learning Backend |
| python-dotenv | Environment Variables |

---

# 🤖 AI Models Used

| Feature | Model |
|---------|------|
| AI Chat | Groq Llama 3 |
| Sentiment Analysis | Default Hugging Face Sentiment Pipeline |
| Text Summarization | sshleifer/distilbart-cnn-12-6 |
| Text Generation | distilgpt2 |
| Translation | Helsinki-NLP/opus-mt-en-fr |
| Zero-Shot Classification | facebook/bart-large-mnli |

---

# 📂 Project Structure

```text
Telegram_AI_Pipeline_Bot/
│
├── bot.py
├── hf_pipelines.py
├── pipeline.py
├── config.py
├── prompts.py
├── logger.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── logs/
│   └── bot.log
│
├── screenshots/
│

```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/Telegram-AI-Pipeline-Bot.git
```

## 2. Navigate to the project

```bash
cd Telegram-AI-Pipeline-Bot
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Create a `.env` file

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

## 7. Run the Bot

```bash
python bot.py
```

---

# 💻 Available Commands

| Command | Description |
|----------|-------------|
| `/start` | Start the bot |
| `/help` | Display available commands |
| `/about` | About the project |
| `/clear` | Clear conversation history |
| `/sentiment` | Analyze text sentiment |
| `/summarize` | Summarize long text |
| `/generate` | Generate text from a prompt |
| `/translate` | Translate English to French |
| `/classify` | Classify text into predefined categories |

---

# 📸 Project Demonstration

## Bot Startup

## AI Chat

## Sentiment Analysis

## Text Summarization

## Text Generation

## Translation

## Zero-Shot Classification


# 🏗️ Project Architecture

```text
                    Telegram User
                          │
                          ▼
                    Telegram Bot
                          │
                          ▼
                  Python Application
                          │
            ┌─────────────┴─────────────┐
            │                           │
            ▼                           ▼
       Groq LLM                 Hugging Face
            │                    Transformers
            │                           │
            ▼                           ▼
     AI Conversation        NLP Pipelines
                             │
         ┌───────────────────┼────────────────────┐
         │                   │                    │
         ▼                   ▼                    ▼
 Sentiment Analysis   Text Summarization   Text Generation
         │                   │                    │
         ├───────────────────┼────────────────────┤
         ▼                   ▼                    ▼
 Translation         Zero-Shot Classification
                          │
                          ▼
                  Telegram Response
```

---

# 🔍 Testing

The following functionalities have been successfully tested:

- ✅ Groq AI Chat
- ✅ Sentiment Analysis
- ✅ Text Summarization
- ✅ Text Generation
- ✅ English → French Translation
- ✅ Zero-Shot Classification
- ✅ Multi-user Conversation Memory
- ✅ Logging
- ✅ Telegram Commands
- ✅ Error Handling

---

# 🚀 Future Enhancements

- 🌐 Multi-language Translation
- 🎤 Voice Message Support
- 🖼️ Image Captioning
- 📄 PDF Summarization
- 🎙️ Speech-to-Text
- 🧠 Retrieval-Augmented Generation (RAG)
- 🐳 Docker Deployment
- ☁️ Cloud Deployment
- 🌍 Web Dashboard using Streamlit or Flask

---

# 👨‍💻 Author

**Swanjal Rawat**

B.Tech Computer Science Engineering

AI | Machine Learning | Python | Generative AI



# ⭐ If you found this project useful, consider giving it a star!
