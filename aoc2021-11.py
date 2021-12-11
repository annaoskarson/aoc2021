with open('11.txt', 'r') as fil:
    lights =[list(map(int, list(r))) for r in fil.read().strip().split('\n')]

import os, time
clear = lambda: os.system('clear')

lts = {}
for y in range(len(lights)):
    for x in range(len(lights[y])):
        lts[(x,y)] = lights[y][x]

def neighbors(point, grid):
    x,y = point
    nbs = set()
    for b in range(y-1, y+2):
        for a in range(x-1, x+2):
            if (a,b) in grid.keys() and (a,b) != (x,y):
                nbs.add((a,b))
    return(nbs)

def load(grid, octs = {'all'}):
    for g in grid.keys():
        if octs == {'all'}: # Alla ska laddas
            grid[g] += 1
        elif g in octs: # Endast de i octs ska laddas.
            grid[g] += 1
    return(grid)

import termcolor
def pprint(grid, text = '', c = 'True', s = 0.1):
    t = {0: termcolor.colored(' ', 'grey'),
        1: termcolor.colored('·', 'grey'),
        2: termcolor.colored('∙', 'grey'),
        3: termcolor.colored('°', 'grey'),
        4: termcolor.colored('×', 'grey'),
        5: termcolor.colored('*', 'grey'),
        6: termcolor.colored('¤', 'grey'),
        7: termcolor.colored('o', 'grey'),
        8: termcolor.colored('O', 'grey'),
        9: termcolor.colored('֍', 'yellow')}
    rows = '\n'
    (x1,y1) = max(grid.keys())
    for y in range(y1+1):
        for x in range(x1+1):
            this = grid[(x,y)]
            if this > 9: this = 9
            this = t[this]
            rows += this
        rows += '\n'
    if c: clear()
    print(rows + '\n' + text)
    time.sleep(s)

def flash(grid, flashed):
    high = set([oct for oct in grid.keys() if grid[oct] > 9])
    if len(high - flashed) > 0: # There are still some to flash.
        f = high - flashed # All in f will be flashed
        for oct in f:
            flashed.add(oct)
            nbs = neighbors(oct, grid)
            grid = load(grid, nbs)
        return(flash(grid, flashed))
    else: # Flashing is done
        pprint(grid)
        return(grid, flashed)

def reset(grid, flashed):
    for oct in flashed:
        grid[oct] = 0
    return(grid)

def partone(grid):
    print("Advent of Code 2021, day 11, part 1.")
    totflash = 0
    pprint(grid, '0')
    for step in range(100):
        grid = load(grid, {'all'})
        grid, flashed = flash(grid, set())
        grid = reset(grid, flashed)
        totflash += len(flashed)
        #pprint(grid, str(step+1))
    print("The answer is:", totflash)


def parttwo(grid):

    print("Advent of Code 2021, day 9, part 2.")
    pprint(grid, '0')
    step = 0
    while True:
        grid = load(grid, {'all'})
        grid, flashed = flash(grid, set())
        if len(flashed) == len(grid):
            break
        #pprint(grid, str(step+1))
        grid = reset(grid, flashed)
        #pprint(grid, str(step+1))
        step += 1

    print("The answer is:", step+1)

partone(lts)
_ = input('Press enter to continue to part 2.')
parttwo(lts)
