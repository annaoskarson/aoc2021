with open('20.txt', 'r') as fil:
    parts = [x.split('\n') for x in fil.read().strip().split('\n\n')]

pen = {}
for i,c in enumerate(parts[0][0]):
    if c is '#':
        pen[i] = True
    else:
        pen[i] = False

image = {}
for y,l in enumerate(parts[1]):
    for x,c in enumerate(l):
        if c is '#':
            image[(x,y)] = True
        else:
            image[(x,y)] = False

def dot(coord, image, pen, light):
    x,y = coord
    nbs =[(a,b) for b in range(y-1, y+2) for a in range(x-1, x+2)]
    bits = ''
    for d in nbs:
        if d not in image:
            if light:
                bits += '1'
            else:
                bits += '0'
        elif image[d]:
            bits += '1'
        else:
            bits += '0'
    bits = ''.join(bits)
    num = int(bits, 2)
    return(pen[num])

def pprint(image):
    paper = ''
    (xmin, ymin) = min(image)
    (xmax, ymax) = max(image)
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            if image[(x,y)]:
                paper += '#'
            else:
                paper += ' '
        paper += '\n'
    print(paper)

def enhance(image, pen, light):
    newimage = {}
    (xmin, ymin) = min(image)
    xmin +=1
    ymin +=1
    (xmax, ymax) = max(image)
    xmax -=1
    ymax -=1
    for y in range(ymin-2, ymax+3):
        for x in range(xmin-2, xmax+3):
            if dot((x,y), image, pen, light):
                newimage[(x,y)] = True
            else:
                newimage[(x,y)] = False
    return(newimage)

def partone(image, pen):
    print('Advent of Code, day 20, part 1.')
    for i in range(2):
        image = enhance(image, pen, i%2)
        #pprint(image)
    ans = sum([a for a in image.values()])
    print('The answer is:', ans)

partone(image, pen)
def parttwo(image, pen):
    print('Advent of Code, day 19, part 2.')
    for i in range(50):
        image = enhance(image, pen, i%2)
        #pprint(image)
    ans = sum([a for a in image.values()])
    print('The answer is:', ans)

parttwo(image, pen)
