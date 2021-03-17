with open('input', 'r') as input_file:
    input_data = input_file.read()

print(sum([1 if ch == '(' else -1 for ch in input_data]))
