import sys 


m = [int(line.strip()) for line in sys.stdin.readlines()]

c = 0 
for i in range(1, len(m)):
    if m[i] > m[i-1]:
        c+=1
print(c)
