import os
import re
from pathlib import Path
import sys
from dotenv import load_dotenv
from colorama import Fore
load_dotenv()

root_dir = os.environ['ROOT_DIR']
skip_amount = os.environ['SKIP_AMOUNT']
lookup_extension = os.environ['EXTENSION']
pattern = r'--[a-z-]+'

def find_string_in_directory(root_dir, search_strings):
    occurrences = {}
    for search_string in search_strings:
        occurrences[search_string] = []

    os.chdir(root_dir)
    for file_path in Path(root_dir).rglob(f"*.{lookup_extension}"):
        with open(file_path) as file:
            for line_number, line in enumerate(file, 1):
                for search_string in search_strings:
                    if search_string in line:
                        occurrences[search_string].append(file.name)
        file.close()
    return occurrences

def run_checks():
    with open('./varlist.txt', 'r') as lookup_file:
        ready_lines = [re.findall(pattern, line)[0] for line in lookup_file.readlines() if re.findall(pattern, line)]
        lookup_file.flush()

    result = find_string_in_directory(root_dir, ready_lines)

    print(Fore.GREEN, 'Tested ', len(result), ' variables')
    

    if len([x for x in result if len(x) == 0]) == 0:
        print(Fore.GREEN, 'All tested variables occurred', Fore.RED, skip_amount, Fore.GREEN, 'times in the entire project')
        return
    
    print(Fore.BLUE, 'Printing variables that did not occur', Fore.RED, skip_amount, Fore.BLUE, 'times in the entire project')

    for r in result:
        if len(result[r]) != int(skip_amount):
            print()
            print(Fore.RED, r, ' => ', len(result[r]))
            for path in result[r]:
                print(Fore.RESET, '    ', path)

print(Fore.RESET)
run_checks()
print(Fore.RESET)