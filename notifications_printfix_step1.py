import os
from bs4 import BeautifulSoup
from bs4 import NavigableString

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an .html file
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')

        # Find all button tags with class "print-clause"
        for button in soup.find_all('button', class_='print-clause'):
            # Create a new div tag
            button.insert_after('\n')

        # Add a closing div tag at the end of the document
        soup.append('\n')
        soup.append('\n')

        # Write the modified HTML back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))