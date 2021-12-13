import timeit

start = timeit.default_timer()

with open('13.txt', 'r') as fil:
    lines = fil.read().strip().split('\n')

m = set()
instr = []
for l in lines:
    if ',' in l:
        x, y = map(int, l.split(','))
        m.add((x,y))
    elif '=' in l:
        f, n = l.split(' ')[2].split('=')
        instr += [(f, int(n))]

def pprint(k):
    text = ''
    xmax = max(k, key = lambda t: t[0])[0]
    ymax = max(k, key = lambda t: t[1])[1]
    for y in range(ymax+1):
        for x in range(xmax+1):
            if (x,y) in k:
                text += '█'
            else:
                text += ' '
        text += '\n'
    print(text)

def parts(m, instr):
    print("Advent of Code 2021, day 13, part 1.")
    ans1 = False
    for (f, n) in instr:
        for (x,y) in list(m):
            if f is 'x' and x > n:
                (x1, y1) = (2*n-x, y)
                m.remove((x,y))
                m.add((x1,y1))
            elif f is 'y' and y > n:
                (x1, y1) = (x, 2*n-y)
                m.remove((x,y))
                m.add((x1,y1))
        if ans1 is False:
            ans1 = len(m)

    print("The answer is:", ans1)
    print("Advent of Code 2021, day 13, part 2.")
    print("The answer is:")
    pprint(m)
parts(m, instr)

stop = timeit.default_timer()

print('Time: ', stop - start)
