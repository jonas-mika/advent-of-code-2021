import sys

infile = sys.argv[1] if len(sys.argv) > 1 else '25.in'
m = list(map(list, open(infile).read().strip().split('\n')))

def show(m):
    return '\n'.join(map(lambda x: ''.join(x), m)) + '\n'

def step(m):
    moved = False
    ys = len(m)
    xs = len(m[0])
    # copy map
    m2 = [[m[y][x] for x in range(xs)] for y in range(ys)]
    
    # east movement
    for y in range(ys):
        for x in range(xs):
            if m[y][x] == '>' and m[y][(x+1)%xs] == '.':
                m2[y][(x+1)%xs] = '>'
                m2[y][x] = '.'
                moved = True

    # copy back
    m = [[m2[y][x] for x in range(xs)] for y in range(ys)]

    # south movement
    for y in range(ys):
        for x in range(xs):
            if m2[y][x] == 'v' and m2[(y+1)%ys][x] == '.':
                m[(y+1)%ys][x] = 'v'
                m[y][x] = '.'
                moved = True

    return m, moved

i = 0
while True:
    m, moved = step(m)
    i+=1
    if not moved:
        print(i)
        break
