import os
import re

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Define regex patterns to match header tags
h1_pattern = re.compile(r'<h1(.*?)>(.*?)<\/h1>', re.DOTALL)
h2_pattern = re.compile(r'<h2(.*?)>(.*?)<\/h2>', re.DOTALL)
header_patterns = {
    'h6': (re.compile(r'<h6(.*?)>(.*?)<\/h6>', re.DOTALL), '<h6\\1>\\2</h6>'),  # h6 remains h6
    'h5': (re.compile(r'<h5(.*?)>(.*?)<\/h5>', re.DOTALL), '<h6\\1>\\2</h6>'),
    'h4': (re.compile(r'<h4(.*?)>(.*?)<\/h4>', re.DOTALL), '<h5\\1>\\2</h5>'),
    'h3': (re.compile(r'<h3(.*?)>(.*?)<\/h3>', re.DOTALL), '<h4\\1>\\2</h4>'),
    'h2': (re.compile(r'<h2(.*?)>(.*?)<\/h2>', re.DOTALL), '<h3\\1>\\2</h3>'),
    'h1': (re.compile(r'<h1(.*?)>(.*?)<\/h1>', re.DOTALL), '<h2\\1>\\2</h2>')
}

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        # Open the file in read mode and read all content
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if the content contains <h2> tags
        if h2_pattern.search(content):
            # Downgrade all header tags by one level
            modified_content = content
            for tag, (pattern, replacement) in header_patterns.items():
                modified_content = re.sub(pattern, replacement, modified_content)

            # Write the modified content back to the file
            with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
                file.write(modified_content)

            # Print the filename
            print(f"Processed Filename: {filename}")