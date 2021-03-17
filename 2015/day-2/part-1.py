with open('input', 'r') as input_file:
    input_data = input_file.read()

print(sum([2*(l*w + w*h + h*l) + min(l*w, w*h, h*l) for l, w, h in [list(map(int, line.split('x'))) for line in input_data.splitlines()]]))
