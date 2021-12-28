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
    print('Advent of Code, day 21 part 1.')
    points = {1:0, 2:0}
    i = 0
    die = 1
    player = 2
    while all(a < 1000 for a in points.values()):
        player = (player + 2) % 2 + 1
        (steps, die) = roll(die)
        state[player] = walk(state[player], steps)
        points[player] += state[player]
        i += 3
    ans = (min(points.values()) * i)
    print('The answer is:', ans)

def playgame(pturn, scores, positions):
    global book

    if (pturn, scores, positions) in book.keys():
        return(book[(pturn,scores, positions)])
    result = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                steps = sum([d1, d2, d3])
                thispos = walk(positions[pturn], steps)
                thisscore = scores[pturn] + thispos

                if thisscore >= 21: # win
                    if pturn == 0:
                        result = (result[0] + 1, result[1])
                    else:
                        result = (result[0], result[1] + 1)
                else:
                    newturn = 1 - pturn
                    if pturn == 0:
                        newscore = (thisscore, scores[1])
                        newpos = (thispos, positions[1])
                    else:
                        newscore = (scores[0], thisscore)
                        newpos = (positions[0], thispos)

                    newresult = playgame(newturn, newscore, newpos)
                    result = (result[0] + newresult[0], result[1] + newresult[1])

    book[(pturn, scores, positions)] = result
    return(result)

def parttwo(state):
    global cnt
    print('Advent of Code, day 21 part 2.')
    positions = (state[1], state[2])
    results = playgame(0, (0, 0), positions)
    ans = max(results)
    print('The answer is:', ans)

partone(state)
book = {}
parttwo(state)
