# Print Twinkle Twinkle Little Start Poem
print("""
      Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky
      """)


# Import external module - Module is a software written by someone else.
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Let's Rock - Bharat Mata ki Jai")
engine.runAndWait()

# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that

import os
# Define the directory you want to scan
# '.' refers to the current working directory
path = "/" 

print(f"--- Contents of '{os.path.abspath(path)}' ---")

## Method 1: Using os.listdir() (Simple and direct)
print("\nMethod 1: os.listdir()")
try:
    entries = os.listdir(path)
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print("The specified directory does not exist.")
