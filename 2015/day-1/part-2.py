with open('input', 'r') as input_file:
    input_data = input_file.read()

cur_floor = 0
for pos, ch in enumerate(input_data):
    cur_floor += 1 if ch == '(' else -1
    if cur_floor == -1:
        print(pos+1)
        break
