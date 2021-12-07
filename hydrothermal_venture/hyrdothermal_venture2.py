import sys
from collections import Counter

coordinates = [[tuple(map(int, coord.split(','))) for coord in line.strip().split(' -> ')] 
                for line in sys.stdin.readlines()]

def points(x1, y1, x2, y2):
    p = []
    if x2 < x1:
        x_range = list(range(x1, x2-1, -1))
    else:
        x_range = list(range(x1, x2+1))
    if y2 < y1:
        y_range = list(range(y1, y2-1, -1))
    else: 
        y_range = list(range(y1, y2+1))

    if len(x_range) < len(y_range):
        x_range *= len(y_range)
    elif len(y_range) < len(x_range):
        y_range *= len(x_range)

    for x, y in zip(x_range, y_range):
        p.append((x, y))

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
