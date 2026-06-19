# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that

import os
# Define the directory you want to scan
# '.' refers to the current working directory
path = "." 

print(f"--- Contents of '{os.path.abspath(path)}' ---")

## Method 1: Using os.listdir() (Simple and direct)
print("\nMethod 1: os.listdir()")
try:
    entries = os.listdir(path)
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print("The specified directory does not exist.")