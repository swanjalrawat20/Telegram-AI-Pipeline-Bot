import os
from dotenv import load_dotenv

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from pipeline import get_ai_response, reset_conversation
from logger import log_chat

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


# -------------------- Commands --------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! I am your AI Pipeline Bot.\n\n"
        "Type /help to see available commands."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🤖 AI Telegram Pipeline Bot

Available Commands:

/start - Start the bot
/help - Show this help message
/about - About this project
/clear - Clear conversation history

💬 Just send any message to chat with the AI.
"""

    await update.message.reply_text(help_text)


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = """
🤖 AI Telegram Pipeline Bot

📌 Project Features:
• AI Chat using Groq LLM
• Telegram Integration
• Multi-user Conversation Memory
• Chat Logging
• Clear Conversation Command
• Modular Python Architecture

🛠 Technologies Used:
• Python
• python-telegram-bot
• Groq API
• python-dotenv

👨‍💻 Developed as an AI Software Engineering Project.
"""

    await update.message.reply_text(about_text)


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    reset_conversation(user_id)

    await update.message.reply_text(
        "🧹 Conversation history cleared successfully!"
    )


# -------------------- AI Chat --------------------

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text

    # Show "typing..."
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )

    try:
        ai_response = get_ai_response(user_id, user_message)

        log_chat(user_message, ai_response)

        await update.message.reply_text(ai_response)

    except Exception as e:
        print(e)

        await update.message.reply_text(
            "⚠️ Sorry, something went wrong while contacting the AI.\nPlease try again in a few seconds."
        )


# -------------------- Main --------------------

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("clear", clear))

    # AI Chat
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    )

    print("🤖 Bot is running... Press Ctrl+C to stop.")

    app.run_polling()


if __name__ == "__main__":
    main()