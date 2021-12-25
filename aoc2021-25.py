with open('25.txt', 'r') as fil:
    lines = fil.read().strip().split('\n')

import copy

xmin, ymin = 0, 0
xmax = len(lines[0])
ymax = len(lines)

east = set()
south = set()
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c == '.':
            pass
        else:
            if c == '>':
                east.add((x,y))
            elif c == 'v':
                south.add((x,y))

def pprint(east, south):
    image = ''
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            if (x,y) in east:
                image += '>'
            elif (x,y) in south:
                image += 'v'
            else:
                image += '.'
        image += '\n'
    print(image)

def step(east, south):

    def next(coord, type):
        x,y = coord
        if type == '>':
            x = (x+1) % xmax
        elif type == 'v':
            y = (y+1) % ymax
        return((x,y))

    move = set()
    for c in east:
        x,y = c
        x1,y1 = next((x,y), '>')
        if (x1,y1) in east or (x1, y1) in south:
            pass
        else:
            move.add((x,y))
    east = east - move
    for g in move:
        east.add(next(g, '>'))

    move = set()
    for c in south:
        x,y = c
        x1,y1 = next((x,y), 'v')
        if (x1,y1) in east or (x1, y1) in south:
            pass
        else:
            move.add((x,y))

    south = south - move
    for g in move:
        south.add(next(g, 'v'))

    return(east, south)

def partone(east, south):
    print('Advent of Code, day 25 part 1.')
    oldeast = copy.deepcopy(east)
    oldsouth = copy.deepcopy(south)
    #pprint(east, south)
    east, south = step(east, south)
    #pprint(east, south)
    i = 1
    while oldeast != east or oldsouth != south:
        oldeast = copy.deepcopy(east)
        oldsouth = copy.deepcopy(south)
        east, south = step(east, south)
        #pprint(east, south)
        i += 1
    print('The answer is:', i)

partone(east, south)
