from sys import stdin

p = {')': 3,
     ']': 57,
     '}': 1197,
     '>': 25137
    }

pairs = {')': '(', 
        ']': '[',
        '}': '{',
        '>': '<'}
ans = 0 
for line in stdin.readlines():
    s = []
    for c in line.strip():
        if c in pairs.values():
            s.append(c)
        else:
            if s[-1] != pairs[c]:
                ans += p[c]
                break
            else:
                s.pop()
print(ans)
