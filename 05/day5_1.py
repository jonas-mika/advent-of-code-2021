import sys
from collections import Counter

coordinates = [[tuple(map(int, coord.split(','))) for coord in line.strip().split(' -> ')] 
                for line in sys.stdin.readlines()]

def points(x1, y1, x2, y2):
    p = []
    if x1 == x2:
        ys = [y1, y2]
        for y in range(min(ys), max(ys)+1):
            p.append((x1, y))
    elif y1 == y2:
        xs = [x1, x2]
        for x in range(min(xs), max(xs)+1):
            p.append((x, y1))
    return p


all_points = []
for coordinate in coordinates:
    p1, p2 = coordinate
    x1, y1 = p1
    x2, y2 = p2
    for point in points(x1, y1, x2, y2):
        all_points.append(point)


c = Counter(all_points)
print(len([key for key, val in c.items() if val >= 2]))
