with open('input', 'r') as input_file:
    input_data = input_file.read()

x = 0
y = 0
houses_set = {(0, 0)}

for ch in input_data:
    x += 1 if ch == '>' else -1 if ch == '<' else 0
    y += 1 if ch == '^' else -1 if ch == 'v' else 0
    houses_set.add((x, y))

print(len(houses_set))
