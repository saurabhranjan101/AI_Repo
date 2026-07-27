from dotenv import load_dotenv
from google import genai

load_dotenv()  # Loads key from .env file

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Tell me who invented samosa in 3 lines",
    )
    # Put this inside the try block so it only runs on success
    print(interaction.output_text)

except Exception as e:
    print("Couldn't generate output.")
    print(f"Error details: {e}")  # Printing 'e' helps you debug the exact error