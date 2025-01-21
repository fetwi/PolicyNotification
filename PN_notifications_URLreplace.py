from bs4 import BeautifulSoup
import os
import csv

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Read the link replacements from the CSV file
link_replacements = {}
csv_file_path = os.path.join(dir_path, "linkreplace.csv")
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        link_replacements[row['link']] = row['replace']

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

            # Write the modified content back to the file
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(str(soup))