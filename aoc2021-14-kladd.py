with open('14-test.txt', 'r') as fil:
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

def howmany(p, cp):
    #times =[]
    for c in set(p):
        times = p.count(c)
        #print(times)
        if c not in cp:
            cp[c] = 0
        cp[c] += times
    return(cp)

def subba(su, old, new, times, cp):
    if times == 40:
        cp = howmany(old[-1], cp)
        return(cp)
    else:
        times += 1
        new = subb(old, su)
        cp = howmany(new[:2], cp)
        cp = subba(su, new[:2], '', times, cp)
        #cp = howmany(new, cp)

def sub2(st, su):
    newst = ''
    for i, c in enumerate(st[:-1]):
        pair = c+st[i+1]
        print(pair, su[pair])
        if pair in su:
            if su[pair] == pair[0]:
                newst += st[:+1] + su[pair] * 40 + sub2(st[2:], su)
            elif su[pair] == pair[1]:
                newst += ''
            else:
                newst += c + su[pair] + sub2(st[2:], su)
        else:
            #print('cut', pair)
            newst += c
    newst += st[-1]
    return(newst)

def partone(p, subs):
    print('Advent of Code 2021, day 14 part 1.')
    for i in range(10):
        #print(i,p)
        p = subb(p, subs)
    print('The answer is', ans(p))

def parttwo(p, subs):
    cp = {}
    print(p)
    print('test', sub2(p, subs))
#    cp = subba(subs, p, '', 0, cp)
#    for i in range(len(p)-1):
#        this = p[i:i+2]
#        print(this)
#        cp = subba(subs, this, '', 0, cp)
        # ta bort p[i+2] från cp
#        cp = howmany(this[:-1], cp)

    print(cp)

    #print(subba(subs, p, ''))

partone(p, subs)
parttwo(p, subs)
