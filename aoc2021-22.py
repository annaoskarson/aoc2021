with open('22-t1.txt', 'r') as fil:
    lines = fil.read().strip().split('\n')

#print(lines)

coords = set()

def partone(lines):
    print('Advent of Code, day 22, part 1.')
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

#partone(lines)

def parttwo(lines):

    def outside(c2, c1):
        #print('apa', c2, c1)
        #print(list((a2[1] < a1[0]) or (a2[0] > a1[1]) for a2 in c2.values() for a1 in c1.values()))
        xout = (c2['x'][0] > c1['x'][1]) or (c2['x'][1] < c1['x'][0])
        yout = (c2['y'][0] > c1['y'][1]) or (c2['y'][1] < c1['y'][0])
        zout = (c2['z'][0] > c1['z'][1]) or (c2['z'][1] < c1['z'][0])
        out = any([xout, yout, zout])
        #out = any((a2[1] < a1[0]) or (a2[0] > a1[1]) for a2 in c2.values() for a1 in c1.values())
        return(out)

    def addcuboid(space, cuboid):
        print('adding', len(space), cuboid)
        if len(space) == 0:
            # If somehow space is empty.
            print('empty space, returning only the cuboid added.')
            return([cuboid])

        print('before rem in add', spaceon(space), space)
        space = remcuboid(space, cuboid)
        print('after rem in add', spaceon(space), space)

        # Now space is clean from the cuboid.
        # Add the cuboid to space
        space.append(cuboid)
        print('after adding in add', spaceon(space))

        return(space)

    def remcuboid(space, cuboid):

        if len(space) == 0:
            print('space is empty')
            return(space)

        newcuboids = []
        for i, part in enumerate(space):

            if outside(cuboid, part):
                print('outside!')
                break

            if part['y'][1] > cuboid['y'][1]:
                # There is a roof on the house.
                roof = {}
                roof['x'] = part['x']
                roof['z'] = part['z']
                roof['y'] = (cuboid['y'][1], part['y'][1])
                print('roof', roof)
                newcuboids.append(roof)

            if part['y'][0] < cuboid['y'][0]:
                # There is a floor on the house.
                floor = {}
                floor['x'] = part['x']
                floor['z'] = part['z']
                floor['y'] = (part['y'][0], cuboid['y'][0])
                print('floor', floor)
                newcuboids.append(floor)

            if part['x'][0] < cuboid['x'][0]:
                # There is a wall to the left.
                wall = {}
                wall['y'] = cuboid['y']
                wall['z'] = part['z']
                wall['x'] = (part['x'][0], cuboid['x'][0])
                print('leftwall', wall)
                newcuboids.append(wall)

            if part['x'][1] > cuboid['x'][1]:
                # There is a wall to the right.
                wall = {}
                wall['y'] = cuboid['y']
                wall['z'] = part['z']
                wall['x'] = (part['x'][0], cuboid['x'][0])
                print('rightwall', wall)
                newcuboids.append(wall)

            if part['z'][0] < cuboid['z'][0]:
                # There is a wall near.
                wall = {}
                wall['x'] = cuboid['x']
                wall['y'] = cuboid['y']
                wall['z'] = (part['z'][0], cuboid['z'][0])
                print('nearwall', wall)
                newcuboids.append(wall)

            if part['z'][1] > cuboid['z'][1]:
                # There is a wall in the distance.
                wall = {}
                wall['x'] = cuboid['x']
                wall['y'] = cuboid['y']
                wall['z'] = (cuboid['z'][1], part['z'][1])
                print('farwall', wall)
                newcuboids.append(wall)

            print('newcuboids', len(newcuboids))

        return(newcuboids)

    def spaceon(space):
        spacesize = 0
        for part in space:
            x = part['x'][1]-part['x'][0]
            y = part['y'][1]-part['y'][0]
            z = part['z'][1]-part['z'][0]
            size = x*y*z
            spacesize += size
        return(spacesize)

    print('Advent of Code, day 22, part 2.')
    space = []

    #a = {'x': (0, 10), 'y': (0, 10), 'z': (0, 10)}
    #b = {'x': (2, 10), 'y': (0, 10), 'z': (0, 10)}
    #c = {'x': (-2, 10), 'y': (0, 10), 'z': (0, 10)}

    # print()
    # #print(spaceon([a]))
    # space = addcuboid([a], b)
    # print(spaceon(space))
    # print(len(space), space)
    # print()
    #
    # space = addcuboid([a], c)
    # print(spaceon(space))
    # print(len(space), space)
    # print()
    #
    # print(spaceon([a]))
    # space = remcuboid([a], b)
    # print(spaceon(space))
    # print(len(space), space)
    # space = addcuboid(space, c)
    # print(spaceon(space))
    # print(len(space), space)
    #
    # exit()

    for l in lines:
        com = l.split(' ')[0]
        xmin, xmax, ymin, ymax, zmin, zmax = [int(b) for a in l.split(' ')[1].strip().split(',') for b in a.strip().split('=')[1].split('..')]
        cuboid = {'x': (xmin, xmax), 'y': (ymin, ymax), 'z': (zmin, zmax)}
        #print(cuboid)
        if com == 'on':
            print('on', cuboid)
            space = addcuboid(space, cuboid)
        elif com == 'off':
            print('off', cuboid)
            space = remcuboid(space, cuboid)
        print('space', len(space))
        print()
        #if l == lines[5]:
        #    exit()
    #print(len(space))
    ans = spaceon(space)

    print('The answer is', ans)

#    testcuboid = {'x': (0, 10), 'y': (11, 21), 'z': (12, 22)}
#    print(spaceon([testcuboid]))
#    corners = []
#    for z in testcuboid['z']:
#        for y in testcuboid['y']:
#            for x in testcuboid['x']:
#                corners.append((x,y,z))
#    print(corners)
#    testcuboid = {'x': (0, 10), 'y': (1, 11), 'z': (2, 12)}
#    print(spaceon([testcuboid]))

parttwo(lines)

# 11012440225185 too low
