from groq import Groq
from config import GROQ_API_KEY
from prompts import SYSTEM_PROMPT

client = Groq(api_key=GROQ_API_KEY)

# Store conversations for each Telegram user
user_conversations = {}


def get_conversation(user_id):
    """Return conversation history for a user."""
    if user_id not in user_conversations:
        user_conversations[user_id] = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]
    return user_conversations[user_id]


def reset_conversation(user_id):
    """Clear conversation for a specific user."""
    user_conversations[user_id] = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]


def get_ai_response(user_id, user_message):
    conversation = get_conversation(user_id)

    conversation.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation
    )

    ai_reply = completion.choices[0].message.content

    conversation.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    return ai_reply