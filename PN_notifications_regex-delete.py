import os
import re

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Define the regex pattern to match (example pattern)
pattern = re.compile(r'(<!-- InstanceBegin)(.*?)(Cette page Web a été archivée dans le Web.<\/em><\/a><\/p>)', re.DOTALL)

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        # Open the file in read mode and read all content
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove the matched content using the regex pattern
        modified_content = re.sub(pattern, '', content)

        # Write the modified content back to the file
        with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
            file.write(modified_content)

        # Print the filename
        print(f"Processed Filename: {filename}")