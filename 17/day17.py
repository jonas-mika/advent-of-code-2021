from sys import stdin

line = str(stdin.readline().strip().split(': ')[1:][0])

xr, yr = list(map(lambda x: list(map(int, x)),
              map(lambda x: x.split('..'), 
              map(lambda x: x.split('=')[1], line.split(', ')))))

xr = set(range(xr[0], xr[1]+1))
yr = set(range(yr[0], yr[1]+1))
min_y = min(yr)

def shoot(x, y):    
    cx = cy = 0

    max_y = 0
    while cy > min_y:
        cx += x
        cy += y 

        if cy > max_y:
            max_y = cy

        if cx in xr and cy in yr:
            return True, max_y

        # update x velocity and y velocity
        y -= 1
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1

    return False, 0 


test_x = range(-200, 200)
test_y = range(-200, 200)
max_height = 0
c = 0
for x in test_x:
    for y in test_y:
        hit, max_y = shoot(x, y)
        if max_y > max_height:
            max_height = max_y
        if hit:
            c+=1

print(f'Part 1: {max_height}')
print(f'Part 2: {c}')
