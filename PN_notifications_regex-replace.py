import os
import re

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Define the regex pattern to match (example pattern)
pattern = re.compile(r'_{3,}', re.DOTALL)

# Define the custom HTML code to replace the matched content
replacement_html = '<span class="blankline" aria-label="Blank placeholder"></span> '

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        # Open the file in read mode and read all content
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace the matched content using the regex pattern with the custom HTML code
        modified_content = re.sub(pattern, replacement_html, content)

        # Write the modified content back to the file
        with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
            file.write(modified_content)

        # Print the filename
        print(f"Processed Filename: {filename}")

# change this code so that it replaces the matched content with a custom html code.