from sys import stdin

i = sorted(list(map(int, stdin.readline().split(',')))) 
d = i[len(i)//2] # median

s = 0
for num in i:
    s+= abs(num - d)
print(s)
