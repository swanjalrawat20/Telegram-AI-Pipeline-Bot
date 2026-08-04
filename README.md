# 🤖 Telegram AI Pipeline Bot

An AI-powered Telegram chatbot built using **Python**, **Telegram Bot API**, and **Groq LLM API**. The bot follows a modular pipeline architecture and supports multi-user conversation memory, logging, and intelligent AI responses.

---

## 📌 Project Overview

This project demonstrates the integration of a Large Language Model (LLM) with Telegram to create an intelligent chatbot. The bot maintains individual conversation histories for multiple users, logs all interactions, and provides contextual responses using the Groq API.

---

## ✨ Features

- 🤖 AI-powered chatbot using Groq LLM
- 💬 Context-aware conversations
- 🧠 Multi-user conversation memory
- 📝 Chat logging with timestamps
- 🧹 Clear conversation history (`/clear`)
- 📖 Help command (`/help`)
- ℹ️ About command (`/about`)
- 🚀 Easy deployment using Python
- ⚠️ Error handling for API failures
- 📂 Modular project structure

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Backend Development |
| Telegram Bot API | Telegram Integration |
| Groq API | AI Response Generation |
| python-telegram-bot | Telegram Library |
| python-dotenv | Environment Variables |

---

## 📂 Project Structure

```text
Telegram-AI-Pipeline-Bot/
│
├── bot.py
├── pipeline.py
├── config.py
├── logger.py
├── prompts.py
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
└── docs/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Telegram-AI-Pipeline-Bot.git
```

### 2. Navigate to the project

```bash
cd Telegram-AI-Pipeline-Bot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

### 7. Run the bot

```bash
python bot.py
```

---

## 💻 Available Commands

| Command | Description |
|----------|-------------|
| `/start` | Start the bot |
| `/help` | Display available commands |
| `/about` | Project information |
| `/clear` | Clear conversation history |

---

## 📸 Project Demonstration

### Bot Startup
### AI Conversation
### Conversation Memory
### Clear Conversation
### Help Command
### About Command
### Logging

## 🏗️ Project Architecture

```text
Telegram User
      │
      ▼
Telegram Bot
      │
      ▼
Python Application
      │
      ▼
Pipeline Module
      │
      ▼
Groq API
      │
      ▼
AI Response
      │
      ▼
Telegram User
```

---

## 🔍 Testing

The following features have been successfully tested:

- ✅ AI Response Generation
- ✅ Conversation Memory
- ✅ Multi-user Support
- ✅ Logging
- ✅ Error Handling
- ✅ Context-aware Responses
- ✅ Telegram Commands

---

## 🚀 Future Enhancements

- 🎤 Voice message support
- 🖼️ Image generation
- 🗄️ Database integration
- 🌐 Web dashboard
- 🐳 Docker deployment
- ☁️ Cloud hosting

---

## 👨‍💻 Author

**Swanjal Rawat**

AI & Python Developer

GitHub: https://github.com/yourusername

---

