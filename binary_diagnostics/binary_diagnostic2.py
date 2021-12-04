import sys

m = [line.strip() for line in sys.stdin.readlines()]

x = len(m[0])
y = len(m)

def calc_rate(nums, search=['1', '0']):
    i = 0
    while len(nums) > 1:
        s = 0
        new_nums = [] 

        for num in nums:
            s += int(num[i])
        
        if s >= len(nums) / 2:
            for num in nums:
                if num[i] == search[0]:
                    new_nums.append(num)
        else:
            for num in nums:
                if num[i] == search[1]:
                    new_nums.append(num)
        nums = new_nums
        i+=1
    return nums[0]

o = calc_rate(m, search=['1', '0'])
e = calc_rate(m, search=['0', '1'])

print(int(o, 2) * int(e, 2))
