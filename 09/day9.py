from sys import stdin
import numpy as np 

m = [line.strip() for line in stdin.readlines()]
xs, ys = len(m[0]), len(m)

def lowpoint(x, y):
    curr = m[y][x]
    n = 4

    l = 0
    ns = neighbors(x, y)
    for n in ns:
        x2, y2 = n
        
        if curr < m[y2][x2]:
            l+=1

    if len(ns) == l:
        return curr
    return None

def neighbors(x, y):
    ns = []
    if y>0:
        ns.append((x,y-1))
    if y<ys-1:
        ns.append((x,y+1))
    if x>0:
        ns.append((x-1,y))
    if x<xs-1:
        ns.append((x+1,y))
    return ns


def bfs(p):
    q = []
    q.insert(0, p)
    marked = set()
    marked.add(p)
    
    c  = 0
    while len(q) > 0:
        curr = q.pop()
        x, y = curr

        for n in neighbors(x, y):
            x2, y2 = n 
            val = int(m[y2][x2])

            if not (n in marked) and val != 9:
                q.insert(0, n)
                marked.add(n)

    return len(marked)


sz = []
for y in range(ys):
    for x in range(xs):
        res = lowpoint(x, y)
        if res:
            size = bfs((x, y))
            sz.append(size)

print(np.prod(sorted(sz, reverse=True)[:3]))
