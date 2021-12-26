from sys import stdin
from math import ceil, floor

#in_ = list(map(lambda x: x.strip(), stdin.readlines()))
#print(in_)

def add(x, y):
    return f'[{x},{y}]'

def reduce(x):
    # 1. If any pair is nested inside four pairs, the leftmost such pair explodes.
    # 2. If any regular number is 10 or greater, the leftmost such regular number splits.
    while True:
        print(x)
        i = can_explode(x)
        if i:
            print('explode on ', i, x[i:i+5])
            x = explode(x, i)
            continue
        i = can_split(x)
        if i:
            print('split on ', i, x[i:i+2])
            x = split(x, i)
            continue
        break

    return x

def can_explode(x):
    s = 0
    for i in range(len(x)):
        if x[i] == '[':
            s+=1
        elif x[i] == ']':
            s-=1
        if s == 5:
            return i
    return False

def can_split(x):
    prev = None
    for i in range(len(x)):
        try: 
            if int(x[i]):
                curr = True
        except: 
            curr = False
        if curr and prev:
            return i-1
        prev = curr

    return False

def explode(x, i):
    left_num = int(x[i+1])
    right_num = int(x[i+3])

    # cut out
    x = x[:i] + '0' + x[i+5:]

    # add to the left 
    for j in range(i-1, -1, -1):
        try: 
            insert = str(int(x[j]) + left_num)
            x = x[:j] + insert + x[j+1:]
            break
        except: None

    # add to the right
    for j in range(i+2, len(x)):
        try:
            insert = str(int(x[j]) + right_num)
            x = x[:j] + insert + x[j+1:]
            break
        except: None

    return x


def split(x, i):
    to_split = int(x[i:i+2])
    left, right = floor(to_split / 2), ceil(to_split / 2)

    return x[:i] + f'[{left},{right}]' + x[i+2:]


def magnitude(x): 
    s = []

    for c in x:
        if c == '[':
            continue
         
        
    pass


# print(split('[[1, 2], 21]', 9))

test = '[[1,2],[[3,4],5]]'

print(magnitude(test))

"""
num1 = stdin.readline().strip()
for num2 in map(lambda x:x.strip(), stdin.readlines()):
    print(num1)
    tmp = add(num1, num2)
    print(tmp)
    num1 = reduce(tmp)
    print(num1)
    print()
    break

print(num1)
"""
