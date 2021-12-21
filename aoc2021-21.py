with open('21.txt', 'r') as fil:
    start = ([l.split(' ') for l in fil.read().strip().split('\n')])
    state = {int(a):int(b) for (_,a,_,_,b) in start}

def walk(spot, num):
    spot = spot + num
    spot = ((spot-1) % 10) + 1
    return(spot)

def roll(last):
    steps = ((last-1) % 100 + 1, (last) % 100 + 1, (last+1) % 100 + 1)
    last = (last + 2) % 100 + 1
    return(sum(steps), last)

def partone(state):
    print('Advent of Code, day 21, part 1.')
    points = {1:0, 2:0}
    i = 0
    die = 1
    player = 2
    while all(a < 1000 for a in points.values()):
        player = (player + 2) % 2 + 1
        (steps, die) = roll(die)
        state[player] = walk(state[player], steps)
        points[player] += state[player]
        #print('turn:', player, 'steg', steps, 'landar på', state[player], 'total poäng', points[player])
        i += 3
    ans = (min(points.values()) * i)
    print('The answer is:', ans)

partone(state)
