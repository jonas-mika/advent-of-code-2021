from sys import stdin

m = [list(map(int, list(line.strip()))) for line in stdin.readlines()]
xs, ys = len(m[0]), len(m)
tc = 0

def neighbors(x, y):
    ns = []
    # gets all nonzero neighbors
    for ny in range(y-1, y+2):
        for nx in range(x-1, x+2):
            if not(nx == x and ny == y):
                if nx >= 0 and nx < xs and ny >= 0 and ny < ys and m[ny][nx]:
                    ns.append((nx, ny))
    return ns

def flash(x, y, to_flash):
    flashed = set() 
    q = []
    q.insert(0, (x,y))
    c = 1 # number of flashes from this start
    # to_flash.remove((x, y))
    m[y][x] = 0

    while len(q) > 0:
        curr = q.pop()
        x, y = curr

        for n in neighbors(x, y):
            nx, ny = n
            curr = m
            m[ny][nx] += 1

            if m[ny][nx] > 9 and (nx, ny) not in flashed:
                q.insert(0, (nx, ny))
                c += 1
                try:
                    to_flash.remove((nx, ny))
                except: None
                m[ny][nx] = 0

    return c

def step():
    to_flash = set()
    for y in range(ys):
        for x in range (xs):
            m[y][x] += 1
            if m[y][x] > 9:
                to_flash.add((x, y))

    # flash all to be flashed
    c = 0
    while len(to_flash) > 0:
        x, y = to_flash.pop()
        c += flash(x, y, to_flash)

    if c == xs * ys:
        print(c, xs*ys)
        return c, True
    return c, False



for i in range(100):
    tc += step()[0]
print(f"Part 1: {tc}")

all_flash = False
i = 100 
while not all_flash:
    all_flash = step()[1]
    i+=1
print(f"Part 2: {i}")
