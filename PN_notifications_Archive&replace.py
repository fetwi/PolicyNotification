import os
import csv
from bs4 import BeautifulSoup

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Read the link replacements from the CSV file
link_replacements = {}
csv_file_path = os.path.join(dir_path, "linkreplaceEN.csv")
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if len(row) >= 2:
            link_replacements[row[0]] = row[1]

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')

            # Replace URLs in the content
            for a_tag in soup.find_all('a', href=True):
                if a_tag['href'] in link_replacements:
                    a_tag['href'] = link_replacements[a_tag['href']]
                    a_tag.string = "ARCHIVED: " + (a_tag.string or '') 

            # Write the modified content back to the file
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(str(soup))