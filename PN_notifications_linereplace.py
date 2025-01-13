from bs4 import BeautifulSoup
import os

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Process lines
        new_lines = []
        button_found = False
        for i, line in enumerate(lines):
            if i == 1 and line.strip() == '<div>':
                new_lines.append('<div class="pn-content">\n')
            else:
                new_lines.append(line)

        # Write the modified lines back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)