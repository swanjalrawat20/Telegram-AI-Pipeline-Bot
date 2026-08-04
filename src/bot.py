import os
from dotenv import load_dotenv
from hf_pipelines import analyze_sentiment
from hf_pipelines import summarize_text
from hf_pipelines import generate_text
from hf_pipelines import translate_text
from hf_pipelines import classify_text
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

async def sentiment(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/sentiment I love AI"
        )
        return

    text = " ".join(context.args)

    result = analyze_sentiment(text)

    await update.message.reply_text(result)

async def summarize(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/summarize <your text>"
        )
        return

    text = " ".join(context.args)

    summary = summarize_text(text)

    await update.message.reply_text(
        f"📝 Summary:\n\n{summary}"
    )

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/generate <your prompt>"
        )
        return

    prompt = " ".join(context.args)

    result = generate_text(prompt)

    await update.message.reply_text(result)

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/translate Hello everyone"
        )
        return

    text = " ".join(context.args)

    translated = translate_text(text)

    await update.message.reply_text(
        f"🌍 French Translation:\n\n{translated}"
    )

async def classify(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/classify <your text>"
        )
        return

    text = " ".join(context.args)

    result = classify_text(text)

    await update.message.reply_text(result)

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
    app.add_handler(CommandHandler("sentiment", sentiment))
    app.add_handler(CommandHandler("summarize", summarize))
    app.add_handler(CommandHandler("generate", generate))
    app.add_handler(CommandHandler("translate", translate))
    app.add_handler(CommandHandler("classify", classify))

    # AI Chat
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    )

    print("🤖 Bot is running... Press Ctrl+C to stop.")

    app.run_polling()


if __name__ == "__main__":
    main()