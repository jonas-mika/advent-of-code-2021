import sys
import functools
import copy

infile = sys.argv[1] if len(sys.argv) > 1 else '24.in'
ops = list(map(lambda x:x.split(' '), open(infile).read().strip().split('\n')))

@functools.lru_cache(maxsize=None)
def search(op_index, w, x, y, z):
    if z > 10**7:
        return (False, '')

    if op_index >= len(ops):
        return (z == 0, '')


    values = {'x': x, 'y': y, 'z': z, 'w': w}

    def evaluate(var):
        if var in values:
            return values[var]
        return int(var)

    op = ops[op_index]
    
    if op[0] == 'inp':
        #for d in range(9, 0, -1):
        for d in range(1, 10):
            values[op[1]] = d
            res = search(op_index+1, values['w'], values['x'], values['y'], values['z'])
            
            if res[0]:
                return (True, str(d) + res[1])

        return (False, 0)
    
    second = evaluate(op[2])

    if op[0] == 'add':
        values[op[1]] += second
    elif op[0] == 'mul':
        values[op[1]] *= second
    elif op[0] == 'div':
        if second == 0:
            return (False, 0)
        values[op[1]] //= second
    elif op[0] == 'mod':
        values[op[1]] %= second
    elif op[0] == 'eql':
        values[op[1]] = 1 if values[op[1]] == second else 0
    else: 
        assert False

    return search(op_index+1, values['w'], values['x'], values['y'], values['z'])

print(search(0, 0, 0, 0, 0))

"""
def works(num):
    digits = str(num)
    idx = 0
    values = {x: 0 for x in 'xyzw'}

    def evaluate(var):
        if var in values:
            return values[var]
        return int(var)

    for op in data:
        if op[0] == 'inp':
            values[op[1]] = ord(digits[idx]) - ord('0') 
            idx += 1
            continue

        second = evaluate(op[2])

        if op[0] == 'add':
            values[op[1]] += second
        elif op[0] == 'mul':
            values[op[1]] *= second
        elif op[0] == 'div':
            if second == 0:
                return False
            values[op[1]] //= second
        elif op[0] == 'mod':
            values[op[1]] %= second
        elif op[0] == 'eql':
            values[op[1]] = 1 if values[op[1]] == second else 0
        else: 
            assert False

    return values['z'] == 0


num = 10**14 - 1
while not works(num):
    num -= 1
print(num)
"""
