with open('22.txt', 'r') as fil:
    lines = fil.read().strip().split('\n')

#print(lines)

coords = set()

def partone(lines):
    print('Advent of Code, day 22, part 1.')
    coords = set()
    for l in lines:
        com = l.split(' ')[0]
        xmin, xmax, ymin, ymax, zmin, zmax = [int(b) for a in l.split(' ')[1].strip().split(',') for b in a.strip().split('=')[1].split('..')]
        #print(com, (xmin, xmax, ymin, ymax, zmin, zmax))

        if xmin > -50 and xmax < 50 and ymin > -50 and ymax < 50 and zmin > -50 and zmax < 50:

            if com == 'on':
                for z in range(zmin, zmax+1):
                    for y in range(ymin, ymax+1):
                        for x in range(xmin, xmax+1):
                            coords.add((x,y,z))

            elif com == 'off':
                rem = set()
                for z in range(zmin, zmax+1):
                    for y in range(ymin, ymax+1):
                        for x in range(xmin, xmax+1):
                            rem.add((x,y,z))

                coords = coords - rem

    print('The answer is', len(coords))

partone(lines)

def parttwo(lines):
    print('Advent of Code, day 22, part 2.')


    print('The answer is', 0)

parttwo(lines)
