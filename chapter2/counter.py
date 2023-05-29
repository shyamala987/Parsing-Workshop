import re

def counter(file):
    count = 0
    with open(file, 'r') as file_input:
        lines = file_input.read()
    
    words = re.findall(r'\b[a-zA-Z]+\b', lines)
    numbers = re.findall(r'\b\d+\b', lines)

    print("Alphabetical words are : ", words)
    print("Alphabetical words count = ", len(words))

    print("Numerical words are :", numbers)
    print("Numerical count is :", len(numbers))
    print("Numerical sum is : ", str(sum([int(i) for i in numbers])))

counter("example.txt")