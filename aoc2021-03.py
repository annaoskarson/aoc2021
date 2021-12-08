fil = open('03.txt', 'r')
#lines = [int(x) for x in fil.read().split('\n')[:-1]]
lines = fil.read().split('\n')[:-1]

import copy

def partone():
    print("Advent of Code 2021, day 3, part 1.")

    res = [0,0,0,0,0,0,0,0,0,0,0,0]
    for l in lines:
        i = 0
        while i < len(l):
            if l[i] == '1':
                res[i] += 1
            elif l[i] == '0':
                res[i] -= 1
            i +=1

    g = ''
    for r in res:
        if r < 0:
            g += '0'
        elif r > 0:
            g += '1'

    b = ''
    for c in g:
        if c == '0':
            b += '1'
        elif c == '1':
            b += '0'

    gb = int(g, base = 2)
    bs = int(b, base = 2)

    print("The answer is:", gb*bs)

def parttwo():
    print("Advent of Code 2021, day 3, part 2.")

    def ox(list, bit): # return the oxy value for the specific bit
        val = 0
        for l in list:
            if l[bit] == '1':
                val += 1
            elif l[bit] == '0':
                val -= 1

        if val >= 0:
            return('1')
        else:
            return('0')

    def co(list, bit): # return co2 the value for the specific bit
        return((set(['0','1']) - set([ox(list,bit)])).pop())

    i = 0
    ls = copy.deepcopy(lines)
    while len(ls) > 1:
        o = ox(ls, i)
        ls = [l for l in ls if l[i] == o]
        i += 1
    oxy = ls[0]

    i = 0
    ls = copy.deepcopy(lines)
    while len(ls) > 1:
        c = co(ls, i)
        ls = [l for l in ls if l[i] == c]
        i += 1
    co2 = ls[0]

    oxy = int(oxy, base=2)
    co2 = int(co2, base=2)

    print("The answer is:", oxy*co2)

partone()
parttwo()
