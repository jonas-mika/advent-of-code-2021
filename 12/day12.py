from sys import stdin
from collections import defaultdict

am = defaultdict(list) 
for line in stdin.readlines():
    u, v = line.strip().split('-')
    if v != 'start':
        am[u].append(v)
    if u != 'start':
        am[v].append(u)

def dfs(curr, seen, am, repeats):
    if curr == 'end':
        return 1

    c = 0
    for n in am[curr]:
        # big cave or small cave that hasnt been seen
        if n.isupper() or n not in seen:
            c += dfs(n, seen | {n}, am, repeats)
        # part2: small cave can be visited twice
        elif n.islower() and n in seen and repeats:
            c += dfs(n, seen | {n}, am, False)
    return c

print(f"Part 1: {dfs('start', set(), am, False)}")
print(f"Part 2: {dfs('start', set(), am, True)}")
