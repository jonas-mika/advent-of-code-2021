import sys

init = list(map(int, sys.stdin.readline().split(',')))

states = [0 for _ in range(9)]
for i in init:
    states[i] += 1

def next_day(states, d=0, stop_at=2):
    if d >= stop_at:
        return sum(states)
    states = states[1:] + states[:1]
    states[6] += states[-1]

    return next_day(states, d=d+1)

print(next_day(states))
