from google import genai
from dotenv import load_dotenv
load_dotenv() ##this will load the key from the .env file

client = genai.Client() #We are creating an object from Client() class using genai module

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    # input="Explain how AI works in a few words"
    input="Tell me who invented samosa in 3 lines"
)

print(interaction.output_text)