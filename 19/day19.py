import sys
import itertools

in_ = open(sys.argv[1]).read().split('\n\n')

data = list(map(lambda x:x.strip().split('\n')[1:], in_))
data = [set(tuple(map(int, pos.split(','))) for pos in scanner) for scanner in data]
print(data)

def orientation(coord):
    # 48 possible coordinates: 6 permutations and any of the three positions 
    # can be negative

     


print(orientation((-1, 2, 3)).shape)

def overlap(X, Y):
    tries = set() 
    for x in X:
        for y in Y:
            tries.add((x[0]-y[0], x[1]-y[1]))

    success = []
    for t in tries:
        print(f'trying: {t}')
        c = 0
        for coord in Y:
            abs_coord = (t[0]+coord[0], t[1]+coord[1])
            if abs_coord in X:
                c+=1

        if c >= 3:
            success.append(t)

    print(success)

#overlap(data[0], data[1])

# gets scanners and list of beacons 
# at each loop consider all pairs of scanners that have not yet been matched
# try to map relative beacon pos of both a pair of beacons, in 
