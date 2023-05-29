import re
res = []
def stringFinder(file, string):
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(string, line) is not None:
                res.append(line)

    print(*res)

stringFinder('example.txt', 'blah')