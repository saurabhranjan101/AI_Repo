from dotenv import load_dotenv
from google import genai

load_dotenv()  # Loads key from .env file

client = genai.Client()

# Read file
filename = "meeting.txt"
with open(filename, "r") as f:
    content = f.read()

# Ask LLM to summarize the file content
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=f"Summarize the following document in 5 lines:\n\n{content}"
)

print(interaction.output_text)
with open("summary.txt","w") as f:
    f.write(interaction.output_text)