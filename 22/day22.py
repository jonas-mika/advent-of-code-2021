import sys

infile = sys.argv[1] if len(sys.argv) > 1 else '22.in'
data = open(infile).read().strip().split('\n')
data = list(map(lambda x: x.split(' '), data))

on = set()
for com, rng in data:
    xr, yr, zr = map(lambda x: list(map(int, x)), map(lambda x: x.split('=')[-1].split('..'), 
                    rng.split(',')))

    for x in range(max(-50, xr[0]), min(51, xr[1]+1)):
        for y in range(max(-50, yr[0]), min(51, yr[1]+1)):
            for z in range(max(-50, zr[0]), min(51, zr[1]+1)):
                if com == 'on':
                    on.add((x, y, z))
                else:
                    on.discard((x, y, z))
print(len(on))

# solve part 2 with coordinate compression
# instead of keeping track of all cubes individually keep track of the ranges in 
# which changes occur
