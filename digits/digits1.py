from sys import stdin

c = 0
one = set('a b'.split())
two = set('g c d f a'.split())
three = set('f b c a d'.split())
four = set('e a f b'.split())
five = set('c d f b e'.split())
six = set('c d f g e b'.split())
seven = set('d a b'.split())
eight = set('a c e d g f b'.split())

def decode(pattern):
    zero = one = two = three = four = five = six = seven = eight = nine = set()
    for digit in pattern:
        d = set(digit)
        if len(digit) == 2:
            one = d 
        elif len(digit) == 3:
            seven = d 
        elif len(digit) == 4:
            four = d
        elif len(digit) == 7:
            eight = d

    # len 6 digits
    for digit in pattern:
        if len(digit) == 6:
            d = set(digit)
            if len(d & one) == 2:
                # either a nine or zero (but no six)
                if len(d & four) == 4:
                    nine = d 
                elif len(d & four) == 3:
                    zero = d 
            else:
                six = d 

    # len 5 digits
    for digit in pattern:
        if len(digit) == 5:
            d = set(digit)
            if len(d & one) == 2:
                three = d
            else:
                if len(d & four) == 2:
                    two = d
                else:
                    five = d


    return [zero, one, two, three, four, five, six, seven, eight, nine]

    


nums = []
for line in stdin.readlines():
    num = ''
    pattern, output = line.strip().split('|')
    pattern = pattern.strip().split(' ')
    output = output.strip().split(' ')
    
    encoding = decode(pattern + output)

    for digit in output:
        d = set(digit)
        if d == encoding[0]:
            num += '0'
        elif len(d) == 2:
            num += '1'
        elif d == encoding[2]:
            num += '2'
        elif d == encoding[3]:
            num += '3'
        elif len(d) == 4:
            num += '4' 
        elif d == encoding[5]:
            num += '5' 
        elif d == encoding[6]:
            num += '6' 
        elif len(d) == 3:
            num += '7' 
        elif len(d) == 7:
            num += '8' 
        elif d == encoding[9]:
            num += '9' 
    nums.append(int(num))


print(sum(nums))
