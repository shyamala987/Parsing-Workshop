from collections import defaultdict
word_freq = defaultdict(int)

with open('words.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    for word in line.split():
        word_freq[word] += 1

for word, freq in sorted(word_freq.items(), key=lambda x:-x[1]):
    print(word + "  :  " + str(freq))
