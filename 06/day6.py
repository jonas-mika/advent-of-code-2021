import sys
from collections import Counter

curr = list(map(int, sys.stdin.readline().split(',')))

states = {i: 0 for i in range(9)}
init_c = Counter(curr)
states.update(init_c)

def next_day(states):
    for key in states.keys():
        if key > 0:
            states[key-1] = states[key]
        if key == 0:
            new_cycle = states[key]
    states[6] += new_cycle
    states[8] = new_cycle
    return states

for _ in range(256):
    states = next_day(states)
print(sum(states.values()))
