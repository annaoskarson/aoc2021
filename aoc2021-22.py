with open('22.txt', 'r') as fil:
    lines = fil.read().strip().split('\n')

import copy

def partone(lines):
    print('Advent of Code, day 22, part 1.')
    for l in lines:
        com = l.split(' ')[0]
        xmin, xmax, ymin, ymax, zmin, zmax = [int(b) for a in l.split(' ')[1].strip().split(',') for b in a.strip().split('=')[1].split('..')]

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
test = False
def outside(c2, c1):
    xout = (c2['x'][0] > c1['x'][1]) or (c2['x'][1] < c1['x'][0])
    yout = (c2['y'][0] > c1['y'][1]) or (c2['y'][1] < c1['y'][0])
    zout = (c2['z'][0] > c1['z'][1]) or (c2['z'][1] < c1['z'][0])
    out = any([xout, yout, zout])
    return(out)

def inside(outer, inner):
    xin = (outer['x'][0] <= inner['x'][0]) and (inner['x'][1] <= outer['x'][1])
    yin = (outer['y'][0] <= inner['y'][0]) and (inner['y'][1] <= outer['y'][1])
    zin = (outer['z'][0] <= inner['z'][0]) and (inner['z'][1] <= outer['z'][1])
    allin = all([xin, yin, zin])
    return(allin)

def addcuboid(nspace, cuboid):
    if len(nspace) == 0:
        # If somehow space is empty.
        return([cuboid])

    # First, make place in space for the new cuboid.
    nspace = remcuboid(nspace, cuboid)

    # Now space is clean from the cuboid.
    # Add the cuboid to space
    nspace.append(cuboid)
    return(nspace)

def remcuboid(nspace, cuboid):
    if len(nspace) == 0:
        return(nspace)

    newcuboids = []
    for part in nspace:

        if outside(cuboid, part):
             # Add the part untouched.
             newcuboids.append(part)

        elif inside(cuboid, part):
            pass

        else:
            # Booleans for defining walls easier.
            roof, floor, left, right = False, False, False, False

            if part['y'][1] > cuboid['y'][1]:
                # There is a roof on the house.
                roof = True
                roof = {}
                roof['x'] = part['x']
                roof['z'] = part['z']
                roof['y'] = (cuboid['y'][1]+1, part['y'][1])
                newcuboids.append(roof)

            if part['y'][0] < cuboid['y'][0]:
                # There is a floor on the house.
                floor = True
                floor = {}
                floor['x'] = part['x']
                floor['z'] = part['z']
                floor['y'] = (part['y'][0], cuboid['y'][0]-1)
                newcuboids.append(floor)

            if part['x'][0] < cuboid['x'][0]:
                # There is a wall to the left.
                left = True
                wall = {}
                wall['y'] = part['y']
                if floor: wall['y'] = (cuboid['y'][0], wall['y'][1])
                if roof: wall['y'] = (wall['y'][0], cuboid['y'][1])
                wall['z'] = part['z']
                wall['x'] = (part['x'][0], cuboid['x'][0]-1)
                newcuboids.append(wall)

            if part['x'][1] > cuboid['x'][1]:
                # There is a wall to the right.
                right = True
                wall = {}
                wall['y'] = part['y']
                if floor: wall['y'] = (cuboid['y'][0], wall['y'][1])
                if roof: wall['y'] = (wall['y'][0], cuboid['y'][1])
                wall['z'] = part['z']
                wall['x'] = (cuboid['x'][1]+1, part['x'][1])
                newcuboids.append(wall)

            if part['z'][0] < cuboid['z'][0]:
                # There is a wall near.
                wall = {}
                wall['y'] = part['y']
                if floor: wall['y'] = (cuboid['y'][0], wall['y'][1])
                if roof: wall['y'] = (wall['y'][0], cuboid['y'][1])
                wall['x'] = part['x']
                if left: wall['x'] = (cuboid['x'][0], wall['x'][1])
                if right: wall['x'] = (wall['x'][0], cuboid['x'][1])
                wall['z'] = (part['z'][0], cuboid['z'][0]-1)
                newcuboids.append(wall)

            if part['z'][1] > cuboid['z'][1]:
                # There is a wall in the distance.
                wall = {}
                wall['y'] = part['y']
                if floor: wall['y'] = (cuboid['y'][0], wall['y'][1])
                if roof: wall['y'] = (wall['y'][0], cuboid['y'][1])
                wall['x'] = part['x']
                if left : wall['x'] = (cuboid['x'][0], wall['x'][1])
                if right: wall['x'] = (wall['x'][0], cuboid['x'][1])
                wall['z'] = (cuboid['z'][1]+1, part['z'][1])
                newcuboids.append(wall)

    return(newcuboids)

def spaceon(space):
    spacesize = 0
    nspace = copy.deepcopy(space)
    i = 0
    while len(nspace) > 0:
        part = nspace.pop(0)
        x = part['x'][1]-part['x'][0] +1
        y = part['y'][1]-part['y'][0] +1
        z = part['z'][1]-part['z'][0] +1
        size = x*y*z
        spacesize += size
    return(spacesize)

def parttwo(lines):
    print('Advent of Code, day 22, part 2.')

    space = [] # This is where all light cuboids are stored.

    for i,l in enumerate(lines):
        com = l.split(' ')[0]
        xmin, xmax, ymin, ymax, zmin, zmax = [int(b) for a in l.split(' ')[1].strip().split(',') for b in a.strip().split('=')[1].split('..')]
        cuboid = {'x': (xmin, xmax), 'y': (ymin, ymax), 'z': (zmin, zmax)}

        if com == 'on': # Add the light cuboid to space.
            space = addcuboid(space, cuboid)
        elif com == 'off': # Remove the dark cuboid from space.
            space = remcuboid(space, cuboid)

    ans = spaceon(space)

    print('The answer is', ans)

parttwo(lines)
