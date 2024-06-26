import os
from bs4 import BeautifulSoup

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an .html file
    if filename.endswith('.txt'):  # Assuming .txt files contain HTML content
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')

        # Find all img tags
        img_tags = soup.find_all('img')
        for img in img_tags:
            # Check if the alt attribute contains specific text
            if 'only to clients' in img.get('alt', '') or 'only accessible to' in img.get('alt', ''):
                # Create a new p tag with specific content
                new_tag = soup.new_tag("span")
                new_tag.string = " (accessible only on the Government of Canada network)"
                # Replace img tag with p tag
                img.replace_with(new_tag)
            elif 'aux clients ayant' in img.get('alt', '') or 'aux fonctionnaires des' in img.get('alt', ''):
                # Create a new p tag with specific content
                new_tag = soup.new_tag("span")
                new_tag.string = " (accessible uniquement sur le réseau du gouvernement du Canada)"
                # Replace img tag with p tag
                img.replace_with(new_tag)

            # Move p tag outside of a tag if it's within one
            if new_tag.parent.name == 'a':
                new_tag.parent.insert_after(new_tag)

        # Write the modified HTML back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))