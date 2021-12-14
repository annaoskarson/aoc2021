with open('14.txt', 'r') as fil:
    lines = fil.read().strip().split('\n')

p = lines[0]
subs = {}
for l in lines[2:]:
    a, b = l.split(' -> ')
    subs[a] = b

def subb(st, su):
    newst = ''
    for i, c in enumerate(st[:-1]):
        pair = c+st[i+1]
        if pair in su:
            newst += c + su[pair]
        else:
            #print('cut', pair)
            newst += c
    newst += st[-1]
    return(newst)

def ans(p):
    times = []
    for c in set(p):
        times += [p.count(c)]
    return(max(times) - min(times))

def partone(p, subs):
    print('Advent of Code 2021, day 14 part 1.')
    for i in range(10):
        #print(i,p)
        p = subb(p, subs)
    print('The answer is', ans(p))

def parttwo(p, subs):
    pass

partone(p, subs)
parttwo(p, subs)
