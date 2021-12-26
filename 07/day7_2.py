from sys import stdin
import math

m = math.inf 
co = list(map(int, stdin.readline().split(',')))


"""
# hardcode
for c in tqdm(range(min(co), max(co))):
    dist = 0
    for c2 in co:
        n = abs(c-c2)
        dist += int((n * (n+1)) / 2)

    if dist < m:
        m = dist
print(m)
"""

# reduce search space through mean
mean = round(sum(co)/len(co))

for c in range(mean-5, mean+5):
    dist = 0
    for c2 in co:
        n = abs(c-c2)
        dist += int((n * (n+1)) / 2) # closed formula for sum of consecutive nums
    if dist < m:
        m = dist
print(m)
