from bs4 import BeautifulSoup
import os

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an .html file
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Process lines
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if '<button class=\"print-clause btn btn-default mrgn-tp-sm mrgn-rght-sm pull-right\"><span class=\"glyphicon glyphicon-print\"></span><span class=\"wb-inv\">Print</span></button>' in line:
                # Insert text without encoding it
                new_lines.append('\n<div>\n')

        # Add a closing div tag at the end of the document
        new_lines.append('</div>')

        # Write the modified lines back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)