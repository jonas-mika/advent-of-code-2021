from sys import stdin
from collections import Counter
from tqdm import tqdm

curr = stdin.readline().strip()
stdin.readline()
ins = {key: val for key, val in [line.strip().split(' -> ') for line in stdin.readlines()]}

# count pairs
c1 = Counter()
for i in range(len(curr)-1):
    c1[curr[i]+curr[i+1]] += 1

for t in range(41):
    if t == 10 or t == 40:
        c = Counter()

        for k in c1:
            c[k[0]]  += c1[k] # just first letter, because second is first of another pair
        c[curr[-1]] += 1 # also count last letter
        c = c.most_common()
        print(c[0][1] - c[-1][1])

    # update counts of pairs
    c2 = Counter()
    for k in c1:
        c2[k[0]+ins[k]] += c1[k]
        c2[ins[k]+k[1]] += c1[k]
    c1 = c2
