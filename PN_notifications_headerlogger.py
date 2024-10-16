import os
import re

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Function to check for h1 or h2 tags in the content
def contains_h1_or_h2(content):
    return re.search(r'<h1', content, re.IGNORECASE) is not None

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        # Open the file in read mode and read all content
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if the content contains h1 or h2 tags
        if contains_h1_or_h2(content):
            # Print the filename
            print(f"Filename: {filename}")