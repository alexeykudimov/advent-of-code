with open('input', 'r') as input_file:
    input_data = input_file.read()

print(sum([min(2*(l+w), 2*(w+h), 2*(h+l)) + l*w*h for l, w, h in [list(map(int, line.split('x'))) for line in input_data.splitlines()]]))
