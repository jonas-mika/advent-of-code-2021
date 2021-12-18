from sys import stdin

T = {'0': '0000',
     '1': '0001',
     '2': '0010',
     '3': '0011',
     '4': '0100',
     '5': '0101',
     '6': '0110',
     '7': '0111',
     '8': '1000',
     '9': '1001',
     'A': '1010',
     'B': '1011',
     'C': '1100',
     'D': '1101',
     'E': '1110',
     'F': '1111'}

VN = 0

def to_binary(s):
    ans = ''
    for c in s:
        ans += T[c]
    return ans

def decode_packet(s):
    print(s)
    version = int(s[:3], 2)
    tid = int(s[3:6], 2)
    print(version, tid)

    global VN 
    VN += version 
    
    # literal packet
    if tid == 4:
        return decode_literal(s)
    # operator packet
    else:
        return decode_operator(s)


def decode_literal(s):
    print('literal')
    nums = []
    i = 0
    b = ''
    end = False
    t = 0
    for c in s[6:]:
        t+=1
        if i==0 and c=='1':
            i += 1
            continue

        elif i==0 and c=='0':
            end = True
            i += 1
            continue

        b += c
        i += 1
        if i == 5:
            nums.append(b)
            b = ''
            i=0

            if end:
                break

    return int(''.join(nums), 2), s[6+t:]

def decode_operator(s):
    print('operator')
    if s[6] == '0':
        tb = int(s[7: 22], 2) 
        s = s[22:]
        print('total bits', tb)

        i = 0
        while i < tb:
            ls = len(s)
            res = decode_packet(s)
            if res:
                num, s = res 
                i += ls - len(s)

    else:
        tp = int(s[7:18], 2)
        print('total packages: ', tp)
        s = s[18:]

        for t in range(tp):
            res = decode_packet(s)
            print(res)
            if res:
                num, s = res 
        

s = stdin.readline().strip()
#s = 'EE00D40C823060'
#s = '38006F45291200'
#s = '8A004A801A8002F478'
s = '620080001611562C8802118E34'
#s = 'C0015000016115A2E0802F182340'
#s = 'A0016C880162017C3686B18A3D4780'
s = to_binary(s)

decode_packet(s)

print(VN)
