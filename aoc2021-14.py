with open('14.txt', 'r') as fil:
    lines = fil.read().strip().split('\n')

p = lines[0]
subs = {}
for l in lines[2:]:
    a, b = l.split(' -> ')
    subs[a] = b

def subb(st, su):
    newst = []
    st = list(st)
    for i, c in enumerate(st[:-1]):
        pair = st[i:i+2]
        if ''.join(pair) in su:
            new = st[i] + su[''.join(pair)]
            newst.append(new)
        else:
            newst += c
    newst += st[-1]
    return(''.join(newst))

import collections
def ans(p):
    times = [b for a,b in list(cnt(p))]
    return(max(times) - min(times))

def cnt(p):
    return(collections.Counter(list(p)).most_common())

def partone(p, subs):
    print('Advent of Code 2021, day 14 part 1.')
    for i in range(10):
        p = subb(p, subs)
    print('The answer is', ans(p))

partone(p, subs)

def translation(p, subs, times):
    if times == 20:
        return(ans(p[:-1]), cnt(p[:-1]))
    else:
        p = subb(p, subs)
        times += 1
        return(translation(p, subs, times))

twenties = {}
for pair in subs.keys():
    twenties[pair] = translation(pair, subs, 0)

def parttwo(p, subs):
    print('Advent of Code 2021, day 14 part 2.')
    for i in range(20):
        print(i)
        p = subb(p, subs)
    p = list(p)
    print(len(p))

    fourties = {}
    for c in set(p):
        fourties[c]= 0
    for i in range(len(p)):
        if i > 0:
            pair = ''.join(p[i-1:i+1])
            apa = twenties[pair][1]
            for c, nb in twenties[pair][1]:
                fourties[c] += nb
    fourties[p[-1]] += 1
    diff = max(fourties.values()) - min(fourties.values())
    print('The answer is', diff)

parttwo(p, subs)
