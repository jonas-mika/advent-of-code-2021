import sys

enc, img = open(sys.argv[1]).read().strip().split('\n\n')
enc = enc.strip().replace('\n', '')
img = img.strip().split('\n')
assert len(enc) == 512

def show_img(img):
    print('\n'.join(img) + '\n')

def to_binary(img, x, y, outside_on=False):
    s = ''
    for j in range(-1, 2):
        for i in range(-1, 2):
            if y+j >= 0 and y+j < len(img) and x+i >= 0 and x+i < len(img[0]):
                s += '1' if img[y+j][x+i] == '#' else '0'
            else:
                s += '1' if outside_on else '0'

    return int(s, 2)

def convert_img(img, outside_on):
    conv_img = []
    for y in range(-1, len(img)+1):
        row = '' 
        for x in range(-1, len(img[0])+1):
            idx = to_binary(img, x, y, outside_on)
            new_pixel = enc[idx]

            row += new_pixel
        conv_img.append(row)

    return conv_img

def count_lit(img):
    c = 0
    for y in range(len(img)):
        for x in range(len(img[0])):
            if img[y][x] == '#':
                c+=1
    return c

outside_on = False
for i in range(50):
    if i == 2:
        print(count_lit(img))
    img = convert_img(img, outside_on)

    if enc[0] == '#':
        outside_on = not outside_on

print(count_lit(img))
