import sys

data = []
for l in sys.stdin.readlines():
    cmd, val = l[:-1].split(' ')
    data.append((cmd, int(val)))

def calculate_part_1(data):
    x, y = 0, 0
    for cmd, val in data:
        if cmd == 'forward':
            x += val
        if cmd == 'down':
            y += val
        if cmd == 'up':
            y -= val
    return x*y

def calculate_part_2(data):
    aim, depth, horizontal = 0, 0, 0
    for cmd, val in data:
        if cmd == 'forward':
            horizontal += val
            depth += aim*val
        if cmd == 'down':
            aim += val
        if cmd == 'up':
            aim -= val
    return depth*horizontal    

print(calculate_part_1(data))
print(calculate_part_2(data))


