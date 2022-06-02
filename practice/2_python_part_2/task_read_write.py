"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""

import os

path = '/Users/nia/projects/PYTHON-BASIC/practice/2_python_part_2/files'

folder = sorted(os.listdir(path))
all_el = []

for file in folder:
    curr_file = path + '/' + file
    with open(curr_file, 'r') as rf:
        value = rf.read()
        all_el.append(value)

with open('result.txt', 'w') as wf:
    print(', '.join(all_el), file=wf)
