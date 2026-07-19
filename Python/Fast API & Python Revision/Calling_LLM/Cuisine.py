from google import genai
from dotenv import load_dotenv
load_dotenv() ##this will load the key from the .env file
client = genai.Client()

def generate_recipe(ingredients, cuisine, diet):
    prompt = f'''
    Generate one food recipe using these ingredients: {','.join(ingredients)} ##this is convert list to string
    Recipe should not be more than 100 words
    Cuisine: {cuisine}
    Diet: {diet}
    '''
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        # input="Explain how AI works in a few words"
        input= prompt
    )
    #print(interaction.output_text)
    return interaction.output_text
recipe = generate_recipe(["Corn", "black bean", "Onion", "corn","avacado"], "Mexican", "Vegeterian")
print(recipe)