import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("🤖 AI Chatbot Started! (type 'exit' to quit)\n")

conversation = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    conversation.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # lightweight fast model
            messages=conversation
        )

        bot_reply = response.choices[0].message.content
        print("Bot:", bot_reply)

        conversation.append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        print("Error:", e)
