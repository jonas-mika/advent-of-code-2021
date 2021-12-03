import sys

h = d = 0
for line in sys.stdin.readlines():
    direction, x = line.strip().split(' ')
    x = int(x)

    if direction == 'forward':
        h += x
    elif direction == 'down':
        d += x
    elif direction == 'up':
        d -= x
print(h * d)
