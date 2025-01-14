from bs4 import BeautifulSoup
import os
import csv

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "notifications")

# Create or open the CSV file to log href values
csv_file_path = os.path.join(dir_path, "links.csv")
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Filename', 'Href'])

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a .txt file
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                soup = BeautifulSoup(content, 'html.parser')

                # Find all href values
                for a_tag in soup.find_all('a', href=True):
                    csvwriter.writerow([filename, a_tag['href']])