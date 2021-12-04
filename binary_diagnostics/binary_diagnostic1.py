import sys

g = e = ''
m = [line.strip() for line in sys.stdin.readlines()]

x = len(m[0])
y = len(m)

for i in range(x):
    s = 0
    for j in range(y):
        s += int(m[j][i])

    if s > y // 2:
        g += '1'
        e += '0'
    else: 
        g += '0'
        e += '1'

print(int(g, 2) * int(e, 2))
