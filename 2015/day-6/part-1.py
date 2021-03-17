import re

with open('input', 'r') as input_file:
    input_data = input_file.read()

n = 1000
lights = [0] * n
for i in range(n):
    lights[i] = [0] * n

for line in input_data.splitlines():
    action, x1, y1, x2, y2 = re.findall('(turn on|turn off|toggle) (\d+),(\d+) \w+ (\d+),(\d+)', line)[0]
    for x in range(int(x1), int(x2)+1):
        for y in range(int(y1), int(y2)+1):
            if lights[x][y] == 0:
                if action in ['turn on', 'toggle']:
                    lights[x][y] = 1
            else:
                if action in ['turn off', 'toggle']:
                    lights[x][y] = 0

print(sum([sum(row) for row in lights]))
