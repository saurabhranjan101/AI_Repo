import streamlit as st
from google import genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = genai.Client()

# Function to generate recipe
def generate_recipe(ingredients, cuisine, diet):
    prompt = f'''
    Generate one food recipe using these ingredients: {','.join(ingredients)}
    Recipe should not be more than 100 words
    Cuisine: {cuisine}
    Diet: {diet}
    '''
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=prompt
    )
    return interaction.output_text

# Streamlit UI
st.title("🍲 AI Recipe Generator")

st.write("Enter ingredients, cuisine type, and diet preference to generate a recipe.")

ingredients_input = st.text_area("Ingredients (comma separated)", "Corn, black bean, onion, avocado")
cuisine_input = st.text_input("Cuisine", "Mexican")
diet_input = st.text_input("Diet", "Vegetarian")

if st.button("Generate Recipe"):
    ingredients = [i.strip() for i in ingredients_input.split(",")]
    recipe = generate_recipe(ingredients, cuisine_input, diet_input)
    st.subheader("Generated Recipe")
    st.write(recipe)