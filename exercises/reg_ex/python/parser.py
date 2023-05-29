import re
from colorama import Fore, Style
# Write a script that prints out all lines in the text that contain a 'q'.
res = []
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/reg_ex/jumping_frog.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if re.search(r'q', line) is not None:
            res.append(line)
    print(Fore.RED + "The following lines contain q")
    print(Style.RESET_ALL)
    print(*res)

# Write a script that prints out all lines in the text that contain a word that start with a 'q' or a 'Q'.
res = []
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/reg_ex/jumping_frog.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if re.search(r'\b[qQ]', line) is not None:
            res.append(line)
    print(Fore.RED + "The following lines contain words that start with a q or a Q")
    print(Style.RESET_ALL)
    print(*res)

# Count the number of words that contain two consecutive vowels.
res = []
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/reg_ex/jumping_frog.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if re.search(r'([aeiou])\1', line) is not None:
            res.append(line)
    print(Fore.RED + "The following lines contain words that have two consecutive vowels")
    print(Style.RESET_ALL)
    print(*res)

# Count the number of lines where one word occurs twice.
res = []
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/reg_ex/jumping_frog.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if re.search(r'(\b\w\b).*\1', line) is not None:
            res.append(line)
    print(Fore.RED + "The following lines contain words where a word occurs twice")
    print(Style.RESET_ALL)
    print(*res)
