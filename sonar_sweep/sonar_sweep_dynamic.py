import sys

a, b, c, d = int(sys.stdin.readline()), int(sys.stdin.readline()), int(sys.stdin.readline()), int(sys.stdin.readline())
co, i  = int(d > a), 4

for num in sys.stdin.readlines():
    a, b, c = b, c, d
    d = int(num)
    if d > a:
        co += 1
    i+=1
print(co)
