import sys

h = d = aim = 0
for line in sys.stdin.readlines():
    direction, x = line.strip().split(' ')
    x = int(x)

    if direction == 'forward':
        h += x
        d += aim * x
    elif direction == 'down':
        aim += x
    elif direction == 'up':
        aim -= x

print(h * d)
