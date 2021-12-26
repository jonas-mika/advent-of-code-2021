import sys 

m = [int(line.strip()) for line in sys.stdin.readlines()]

c1 = c2 = 0 
for i in range(1, len(m)):
    if m[i] > m[i-1]:
        c1 += 1
    if i >= 3:
        if m[i] > m[i-3]:
            c2 += 1;

print(f'Part1: {c1}')
print(f'Part2: {c2}')
