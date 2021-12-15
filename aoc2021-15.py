with open('15.txt', 'r') as fil:
    lines = fil.read().strip().split('\n')

coords = {}
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        coords[(x,y)] = int(c)
    xmax = x
ymax = y

start = (0,0)
goal = (xmax, ymax)

def nbs(point, coords):
    x,y = point
    nbs = {(x-1, y-1), (x, y-1), (x, y+1), (x+1, y)}
    nbs = [pt for pt in nbs if pt in coords]
    return(nbs)

ecoords = {}
for point in coords:
    for yfactor in range(5):
        for xfactor in range(5):
            x,y = point
            value = range(1,10)[(coords[point]+(xfactor+yfactor)) - 10]
            xn = x + (xmax+1)*(xfactor)
            yn = y + (ymax+1)*(yfactor)
            ecoords[(xn, yn)] = value

def fixgrid(coords):
    grid ={}
    for c in coords:
        grid[c] = {}
        nbl = nbs(c, coords)
        for n in nbl:
            grid[c][n] = coords[n]
    return(grid)

grid = fixgrid(coords)

egrid = fixgrid(ecoords)

import heapq

def walk(grid, start):
    risks = {n: float('inf') for n in grid}
    risks[start] = 0
    prioq = [(0, start)]

    while len(prioq) > 0:
        hererisk, here = heapq.heappop(prioq)

        if hererisk > risks[here]:
            continue

        for nb, risk in grid[here].items():
            newrisk = hererisk + risk

            if newrisk < risks[nb]:
                risks[nb] = newrisk
                heapq.heappush(prioq, (newrisk, nb))
    return(risks)

def partone(grid, start, goal):
    print('Advent of Code 2021, day 14 part 1.')
    dist = walk(grid, start)
    print('The answer is', dist[goal])

partone(grid, start, goal)
# 740 too high
# 739 ...
# 731 too low
# 739 right

def parttwo(egrid, start):
    print('Advent of Code 2021, day 14 part 2.')
    egoal = max(ecoords.keys())
    dist2 = walk(egrid, start)
    print('The answer is', dist2[egoal])

parttwo(egrid, start)
# 3042 too high
# 3041 too high
# 3030 too low
# 3037 not right
# 3040 right ...
