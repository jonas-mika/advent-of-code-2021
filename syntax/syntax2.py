from sys import stdin

p = {'(': 1,
     '[': 2,
     '{': 3,
     '<': 4 
    }

pairs = {')': '(', 
        ']': '[',
        '}': '{',
        '>': '<'}
scores = [] 
for line in stdin.readlines():
    s = []
    corrupted = False
    for c in line.strip():
        if c in pairs.values():
            s.append(c)
        else:
            if s[-1] != pairs[c]:
                corrupted = True
                break
            else:
                s.pop()

    if not corrupted:
        so = 0
        for c2 in reversed(s):
            so *= 5
            so += p[c2]
        scores.append(so)

print(sorted(scores)[len(scores)//2])
