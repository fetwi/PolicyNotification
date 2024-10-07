import os
import re

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Function to extract ID from filename
def extract_id(filename):
    parts = filename.split('~')
    if len(parts) > 2:
        return parts[1]
    return None

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        # Extract ID from filename
        file_id = extract_id(filename)
        
        if file_id:
            # Open the file in read mode and read all content
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.readlines()

            # Prepare the HTML to be inserted
            if filename.startswith('en'):
                html_to_insert = f'<h2 class="pn-content-title">Content of {file_id}</h2>\n'
            elif filename.startswith('fr'):
                html_to_insert = f'<h2 class="pn-content-title">Contenu du {file_id}</h2>\n'
            else:
                html_to_insert = ''

            # Insert the HTML after the first line
            if html_to_insert:
                content.insert(1, html_to_insert)

            # Write the modified content back to the file
            with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
                file.writelines(content)

            # Print the filename and the modified content
            print(f"Filename: {filename}")