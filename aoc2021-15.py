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
    nbs = {(x-1, y), (x, y-1), (x, y+1), (x+1, y)}
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

def walk2(Graph, Start, Goal):
    visited = set()
    tovisit = [(0, Start)]
    while True:
        hrisk, hpos = tovisit.pop(0)
        if hpos in visited:
            continue
        visited.add(hpos)
        if hpos == Goal:
            return(hrisk)
        tovisit.extend([(hrisk + nrisk, npos) for npos, nrisk in Graph[hpos].items() if npos not in visited])
        tovisit = sorted(tovisit)

def partone(grid, start, goal):
    print('Advent of Code 2021, day 15 part 1.')
    ans = walk2(grid, start, goal)
    print('The answer is', ans)

partone(grid, start, goal)

def parttwo(grid, start, goal):
    print('Advent of Code 2021, day 15 part 2.')
    ans = walk2(grid, start, goal)
    print('The answer is', ans)

egoal = max(ecoords.keys())
parttwo(egrid, start, egoal)
