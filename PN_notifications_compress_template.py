import os
import csv
import urllib.parse

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
notifications_dir = os.path.join(dir_path, "notifications")
template_file = os.path.join(dir_path, "templatepn.csv")
output_file = os.path.join(dir_path, "output.txt")

# Function to read, join, and URI encode notification file content
def read_join_and_encode_notification(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().replace('\n', ' ')
    encoded_content = urllib.parse.quote(content)
    return encoded_content

# Read the template CSV and process each line
with open(template_file, 'r', encoding='utf-8') as csvfile, open(output_file, 'w', encoding='utf-8', errors='ignore') as outfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 0:
            filename = row[0]
            notification_file = os.path.join(notifications_dir, filename)
            if os.path.exists(notification_file):
                encoded_content = read_join_and_encode_notification(notification_file)
                modified_line = ','.join(row).replace('[here]', encoded_content)
                outfile.write(modified_line + '\n')
            else:
                print(f"Notification file {filename} not found.")