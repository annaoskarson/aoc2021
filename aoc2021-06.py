with open('6.txt', 'r') as fil:
    fish = ([int(f) for f in fil.read().strip().split(',')])
#    fish = ([int(f) for f in '3,4,3,1,2'.split(',')])

import copy

def partone(f1):
    def day(fs):
        newfish = []
        for i in range(len(fs)):
            if fs[i] == 0:
                fs[i] = 6
                newfish.append(8)
            else:
                fs[i] -= 1
        return(fs + newfish)

    print("Advent of Code 2021, day 6, part 1.")
    for d in range(80):
        f1 = day(f1)
    ans = (len(f1))
    print("The answer is:", ans)

def parttwo(f2):
    def fishclass(fs):
        fishC = {}
        for f in fs:
            if f not in fishC.keys():
                fishC[f] = 1
            else:
                fishC[f] += 1
        return(fishC)

    def day2(fs):
        newday = {}
        for i in range(9):
            newday[i] = 0

        for f in fs.keys():
            if f == 0:
                newday[6] += fs[f]
                newday[8] += fs[f]
            else:
                newday[f-1] += fs[f]
        return(newday)

    print("Advent of Code 2021, day 6, part 2.")
    fs = fishclass(f2)

    for d in range(256):
        fs = day2(fs)
    ans =(sum(fs.values()))
    print("The answer is:", ans)

fish2 = copy.deepcopy(fish) # Jag borde väl snart begripa hur variabler funkar ...
partone(fish)
parttwo(fish2)
