import os
import re

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Define the img tag pattern
img_pattern = re.compile(r'<img[^>]*>', re.IGNORECASE)

# iterate over all files in the directory
for filename in os.listdir(directory):
    # check if the file is a .txt file
    if filename.endswith('.txt'):
        # open the file in read mode and read all lines
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()

        # check if the content contains an img tag
        match = img_pattern.search(content)
        if match:
            print(f"{filename}, {match.group()}")