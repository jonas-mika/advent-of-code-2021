from sys import stdin
import math

coord = set() 
inst = []

# read input
xs = ys = 0 
n = False
for line in stdin.readlines():
    if line != "\n" and n == False:
        x, y = tuple(map(int, list(line.strip().split(','))))
        coord.add((x, y))

        if x > xs:
            xs = x
        if y > ys:
            ys = y

    elif n:
        line = line.split(' ')[-1]
        axis, c = line.split('=')
        inst.append((axis, int(c)))
    else:
        n = True
xs+=1
ys+=1

# generate map
m = []
for y in range(ys):
    r = []
    for x in range(xs):
        if (x, y) in coord:
            r.append('#')
        else:
            r.append('.')
    m.append(r)

def fold(m, coord, axis='y'):
    xs, ys = len(m[0]), len(m)
    if axis=='y':
        for i in range(coord):
            for x in range(xs):
                if m[ys-1-i][x] == '#':
                    m[i][x] = m[ys-1-i][x]
        return m[:coord]
    else:
        for y in range(ys):
            for i in range(coord):
                if m[y][xs-1-i] == '#':
                    m[y][i] = m[y][xs-1-i]
        return [row[:coord] for row in m]
    
i = 0
for axis, coord in inst:
    m = fold(m, coord=coord, axis=axis)

    if i == 0:
        c = 0
        for y in range(len(m)):
            for x in range(len(m[0])):
                if m[y][x] == '#':
                    c+=1
        print(f'Part 1: {c}')
    i+=1

pm = []
for row in m:
    nrow = ''.join(row)
    pm.append(nrow.replace('.', ' '))

print('Part 2:')
print('\n'.join(pm))
