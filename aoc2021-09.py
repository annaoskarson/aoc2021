with open('09.txt', 'r') as fil:
    depths =[list(map(int, list(r))) for r in fil.read().strip().split('\n')]
    #prinxt([[int(s) for s in r] for r in fil.read().strip().split('\n')])
    #ls = [[s.strip().split(' ') for s in r] for r in fil.read().strip().split('\n') ]
#print(ls)

def partone(ds):
    def localmin(ds, coords):
        x,y = coords
        nbc = []
        if y < len(ds)-1:
            nbc.append(ds[y+1][x])
        if y > 0:
            nbc.append(ds[y-1][x])
        if x < len(ds[y])-1:
            nbc.append(ds[y][x+1])
        if x > 0:
            nbc.append(ds[y][x-1])
        return(all([ds[y][x] < n for n in nbc]))

    print("Advent of Code 2021, day 9, part 1.")
    risk = 0
    localmins = []
    for y in range(len(ds)):
        for x in range(len(ds[y])):
            if localmin(ds, (x,y)):
                localmins.append((x,y))
                risk += ds[y][x]+1
    #print('antal', len(localmins))
    print("The answer is:", risk)
    return(localmins)

def parttwo(ds, lms):

    def wholebasin(ds, coord, basin):
        (x,y) = coord
        nbsinbas = set()
        if y < len(ds)-1 and ds[y+1][x] != 9 and (x, y+1) not in basin:
            #print(coord, 'v', (x, y+1))
            nbsinbas.add((x, y+1))
        if y > 0 and ds[y-1][x] != 9 and (x, y-1) not in basin:
            #print(coord, '^', (x, y-1))
            nbsinbas.add((x, y-1))
        if x < len(ds[y])-1 and ds[y][x+1] != 9 and (x+1, y) not in basin:
            #print(coord, '>', (x+1, y))
            nbsinbas.add((x+1, y))
        if x > 0 and ds[y][x-1] != 9 and (x-1, y) not in basin:
            #print(coord, '<', (x-1, y))
            nbsinbas.add((x-1, y))

        for (a, b) in nbsinbas:
            basin.add((a,b))
            basin = wholebasin(ds, (a,b), basin)

        return(basin)

    print("Advent of Code 2021, day 9, part 2.")
    basinsizes = []
    for (x,y) in lms:
        # Find how big that basin is and put in list.
        basinsizes.append(len(wholebasin(ds, (x,y), {(x,y)})))

    three = sorted(basinsizes)[-3:]
    ans = three[0] * three[1] * three[2]
    print("The answer is:", ans)

print(len([p for row in depths for p in row if p == 0 ] ))

lmins = partone(depths)

print(max([depths[y][x] for (x,y) in lmins]))

parttwo(depths, lmins)
