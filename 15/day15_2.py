# clean solution using standard lib heapq (without building graph object)
from sys import stdin
import heapq
from collections import defaultdict

map = [[int(x) for x in line.strip()] for line in stdin.readlines()]

N = len(map)
M = len(map[0])

rows = N * 5
cols = M * 5


def get(r, c):
    x = (map[r % N][c % M] +
         (r // N) + (c // M))
    return (x - 1) % 9 + 1


cost = defaultdict(int)

pq = [(0, 0, 0)]
heapq.heapify(pq)
visited = set()

while len(pq) > 0:
    c, row, col = heapq.heappop(pq)

    if (row, col) in visited:
        continue
    visited.add((row, col))

    cost[(row, col)] = c

    if row == rows - 1 and col == cols - 1:
        break

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        rr = row + dr
        cc = col + dc
        if not (0 <= rr < rows and 0 <= cc < cols):
            continue

        heapq.heappush(pq, (c + get(rr, cc), rr, cc))


print(cost[(rows - 1, cols - 1)])
