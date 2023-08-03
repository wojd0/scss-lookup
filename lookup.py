import os
import re
import glob
from pathlib import Path

# CHANGE THOSE VARIABLE VALUES

root_dir = os.environ['ROOT_DIR']

def extract_first_word(string):
    pattern = r'[a-zA-Z-]'
    match = ''.join(re.findall(pattern, string))
    return match


def find_string_in_directory(root_dir, search_strings):
    occurrences = {}
    os.chdir(root_dir)
    for file_path in Path(root_dir).rglob(f"*.{os.environ['EXTENSION']}"):
        with open(file_path, 'r') as file_path:
            for line_number, line in enumerate(file_path, 1):
                  for search_string in search_strings:
                     if search_string in line:
                           occurrences[search_string] = occurrences.get(search_string, 0) + 1
    return occurrences



with open('/Users/wojciech.duda/Dev/tolookfor.txt', 'r') as lookup_file:
    ready_lines = []
    for line in lookup_file:
        line = line.strip()

        if  '--' not in line: continue

        last_index = line.index(')') if ')' in line else line.index(':')
        line = line[line.index('--'): last_index]
        ready_lines += [line]
        # line = extract_first_word(line)
    result = find_string_in_directory(root_dir, ready_lines)
    print('Tested ', len(result), ' variables')
    for r in result:
         if result[r] != os.environ['SKIP_AMOUNT']:
             print(r,' <=> ', result[r])
    # print(line)
