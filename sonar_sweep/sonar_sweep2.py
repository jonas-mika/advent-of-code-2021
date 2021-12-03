import sys 

m = [int(line.strip()) for line in sys.stdin.readlines()]

c = 0 
for i in range(3, len(m)):
    if m[i]+m[i-1]+m[i-2] > m[i-1] + m[i-2] + m[i-3]:
        c+=1
print(c)
