import os
import re

# Define the file paths
dir_path = os.path.dirname(os.path.realpath(__file__))
output_file_path = os.path.join(dir_path, "output.txt")
template_en_path =  os.path.join(dir_path, "paste-templatepn-en.html")
template_fr_path = os.path.join(dir_path, "paste-templatepn-fr.html")
output_en_path = os.path.join(dir_path, "V3/pn-en-paste.html")
output_fr_path = os.path.join(dir_path, "V3/pn-fr-paste.html")

# Read the output.txt file
with open(output_file_path, 'r') as file:
    lines = file.readlines()

# Extract content for en and fr
content_en = []
content_fr = []
for line in lines:
    if line.startswith('en'):
        content_en.append(line.split(',', 1)[1].strip())
    elif line.startswith('fr'):
        content_fr.append(line.split(',', 1)[1].strip())

# Join the content with new lines
content_en = '\n'.join(content_en)
content_fr = '\n'.join(content_fr)

# Function to replace {here} placeholder in the template file and save to a new file
def replace_placeholder(template_path, content, output_path):
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    updated_content = re.sub(r'{here}', content, template_content)
    
    with open(output_path, 'w') as file:
        file.write(updated_content)

# Replace {here} placeholder in the respective template files and save to new output files
replace_placeholder(template_en_path, content_en, output_en_path)
replace_placeholder(template_fr_path, content_fr, output_fr_path)

print("Placeholders replaced and saved to new files successfully.")