input_file = 'transpose-file.txt'
with open(input_file, 'r') as file:
    lines = file.readlines()

num_rows = len(lines)
num_cols = len(lines[0].split())

transposed_lines = []
for j in range(num_cols):
    transposed_line = ' '.join([lines[i].split()[j] for i in range(num_rows)])
    transposed_lines.append(transposed_line)

for j in range(num_cols):
    print(transposed_lines[j])
