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
                content = file.read()

            # Add the specified HTML after the print button based on filename prefix
            if filename.startswith('en'):
                modified_content = re.sub(r'(<button[^>]*>Print</button>)', r'\1<h2 class="pn-content-title">Content of ' + file_id + r'</h2>', content)
            elif filename.startswith('fr'):
                modified_content = re.sub(r'(<button[^>]*>Print</button>)', r'\1<h2 class="pn-content-title">Contenu du ' + file_id + r'</h2>', content)

            # Write the modified content back to the file
            with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
                file.write(modified_content)

            # Print the filename and the modified content
            print(f"Filename: {filename}")