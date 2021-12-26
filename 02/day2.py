import sys

lines = list(map(lambda x:x.strip().split(' '), sys.stdin.readlines()))

h = d = 0
for line in lines:
    direction, x = line 
    x = int(x)

    if direction == 'forward':
        h += x
    elif direction == 'down':
        d += x
    elif direction == 'up':
        d -= x
print(f'Part 1: {h * d}')

h = d = aim = 0
for line in lines:
    direction, x = line 
    x = int(x)

    if direction == 'forward':
        h += x
        d += aim * x
    elif direction == 'down':
        aim += x
    elif direction == 'up':
        aim -= x

print(f'Part 2: {h * d}')
