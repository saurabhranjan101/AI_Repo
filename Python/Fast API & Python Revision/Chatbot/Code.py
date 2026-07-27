from google import genai
from dotenv import load_dotenv
load_dotenv()
client = genai.Client()
conversation = []

def chat(user_message):
    conversation.append({"role":"user","part":[{"text": user_message}]})
    try:
        response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents= conversation
        )
        reply = response.text
    except Exception as e:
        return f"Sorry, something went wrong:{e}"
    conversation.append({"role":"model","part":[{"text": reply}]})
    return reply
print(chat("Hi, I am Saurabh. Please remenber my name"))
print(chat("What is my name?"))