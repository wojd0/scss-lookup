import os
import re
from pathlib import Path
from dotenv import load_dotenv
from colorama import Fore
load_dotenv()

root_dir = os.environ['ROOT_DIR']

pattern = r'--[a-z-]+'


def find_string_in_directory(root_dir, search_strings):
    occurrences = {}
    for search_string in search_strings:
        occurrences[search_string] = []

    os.chdir(root_dir)
    for file_path in Path(root_dir).rglob(f"*.{os.environ['EXTENSION']}"):
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                for search_string in search_strings:
                    if search_string in line:
                        occurrences[search_string].append(file.name)
    return occurrences


with open('./varlist.txt', 'r') as lookup_file:
    ready_lines = [re.findall(pattern, line)[0] for line in lookup_file if re.findall(pattern, line)]

    result = find_string_in_directory(root_dir, ready_lines)

    print(Fore.GREEN, 'Tested ', len(result), ' variables')
    print(Fore.BLUE, 'Printing variables that did not occur', Fore.RED, os.environ['SKIP_AMOUNT'], Fore.BLUE, 'times in the entire project')

    for r in result:
        if len(result[r]) != int(os.environ['SKIP_AMOUNT']):
            print()
            print(Fore.RED, r, ' => ', len(result[r]))
            for path in result[r]:
                print(Fore.RESET, '    ', path)
    # print(line)
