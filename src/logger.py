from datetime import datetime


def log_chat(user_message, ai_response):
    with open("logs/bot.log", "a", encoding="utf-8") as file:
        file.write(
            f"[{datetime.now()}]\n"
            f"User: {user_message}\n"
            f"Bot: {ai_response}\n"
            f"{'-'*50}\n"
        )