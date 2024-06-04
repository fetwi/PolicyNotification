import os

# Define the directory
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(dir_path, "clauses")

# Define the lines to prepend and append
line_to_begin = "<button class=\"print-clause btn btn-default mrgn-tp-sm mrgn-rght-sm pull-right\"><span class=\"glyphicon glyphicon-print\"></span><span class=\"wb-inv\">Print</span></button><div>\n"
line_to_end = "\n</div>"

# iterate over all files in the directory
for filename in os.listdir(directory):
    # check if the file is a .txt file
    if filename.endswith('.txt'):
        # open the file in read mode and read all lines
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # add the specified lines to the beginning and end
        lines.insert(0, line_to_begin)
        lines.append(line_to_end)

        # open the file in write mode and write the modified lines
        with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
            file.writelines(lines)