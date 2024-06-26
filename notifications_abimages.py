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
            img.decompose()

        # Write the modified HTML back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))