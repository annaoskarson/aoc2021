with open('11.txt', 'r') as fil:
    lights =[list(map(int, list(r))) for r in fil.read().strip().split('\n')]

lts = {}
for y in range(len(lights)):
    for x in range(len(lights[y])):
        lts[(x,y)] = lights[y][x]

import os, time
clear = lambda: os.system('clear')

import copy
lts2 = copy.deepcopy(lts)

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

import termcolor, playsound
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
        9: termcolor.colored('Ø', 'grey'),
        10: termcolor.colored('֍', 'yellow')}
    rows = '\n'
    (x1,y1) = max(grid.keys())
    for y in range(y1+1):
        for x in range(x1+1):
            this = grid[(x,y)]
            if this > 9: this = 10
            this = t[this]
            rows += this
        rows += '\n'
    if c: clear()
    print(rows + text)
    #time.sleep(0.01)
    times = len([x for x in rows if x == '֍'])
    times = times // 5  + (times > 0)
    for t in range(times):
        playsound.playsound('fl3.mp3', False)
        time.sleep(0.0003)
    time.sleep(s)

def flash(grid, flashed):
    high = set([oct for oct in grid.keys() if grid[oct] > 9])
    if len(high - flashed) > 0: # There are still some to flash.
        f = high - flashed # All in f will be flashed.
        for oct in f:
            flashed.add(oct)
            nbs = neighbors(oct, grid)
            grid = load(grid, nbs)
        return(flash(grid, flashed))
    else: # Flashing is done for this time.
        #pprint(grid) # Uncomment if you want flash and pop.
        return(grid, flashed)

def reset(grid, flashed):
    for oct in flashed:
        grid[oct] = 0
    return(grid)

def partone(grid):
    print("Advent of Code 2021, day 11, part 1.")
    totflash = 0
    for step in range(100):
        #pprint(grid) # Uncomment if you want flash and pop.
        grid = load(grid, {'all'})
        grid, flashed = flash(grid, set())
        grid = reset(grid, flashed)
        totflash += len(flashed)
    print("The answer is:", totflash)

def parttwo(grid):
    print("Advent of Code 2021, day 9, part 2.")
    step = 0
    while True:
        #pprint(grid) # Uncomment if you want flash and pop.
        grid = load(grid, {'all'})
        grid, flashed = flash(grid, set())
        if len(flashed) == len(grid):
            break
        grid = reset(grid, flashed)
        step += 1
    print("The answer is:", step+1)

partone(lts)
#_ = input('Press enter to continue to part 2.') # uncomment if printing.
parttwo(lts2)
