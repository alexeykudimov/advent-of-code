with open('input', 'r') as input_file:
    input_data = input_file.read()

santa_x = 0
santa_y = 0
robosanta_x = 0
robosanta_y = 0

houses_set = {(0, 0)}

for pos, ch in enumerate(input_data):
    if pos % 2 == 0:
        santa_x += 1 if ch == '>' else -1 if ch == '<' else 0
        santa_y += 1 if ch == '^' else -1 if ch == 'v' else 0
        houses_set.add((santa_x, santa_y))
    else:
        robosanta_x += 1 if ch == '>' else -1 if ch == '<' else 0
        robosanta_y += 1 if ch == '^' else -1 if ch == 'v' else 0
        houses_set.add((robosanta_x, robosanta_y))

print(len(houses_set))
