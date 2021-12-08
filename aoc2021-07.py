with open('7.txt', 'r') as fil:
    crabs = [int(f) for f in fil.read().strip().split(',')]

#crabs = [16,1,2,0,4,2,7,1,2,14]

def partone(c):
    def position(crabs, p):
        cost = 0
        for cr in crabs:
            cost += abs(cr-p)
        return(cost, p)

    print("Advent of Code 2021, day 7, part 1.")
    cheapest = (max(c) - min(c)) * len(c)
    goal = 0
    for p in range(min(c), max(c)):
        cost, pos = position(c, p)
        #print(pos, cost, cheapest)
        if cost < cheapest:
            cheapest = cost
            goal = pos
            #print('saved ', goal, cheapest)
    ans = cheapest
    print("The answer is:", ans)

def parttwo(c):
    def position(crabs, p):
        cost = 0
        for cr in crabs:
            dist = abs(cr-p)
            cost += (dist*(dist+1))//2
            #cost += sum(range(0, abs(cr-p)+1))
        return(cost, p)

    print("Advent of Code 2021, day 7, part 2.")
    cheapest = (max(c) - min(c)) * sum(range(len(c)))
    goal = 0
    for p in range(min(c), max(c)):
        cost, pos = position(c, p)
        #print(pos, cost, cheapest)
        if cost < cheapest:
            cheapest = cost
            goal = pos
            #print('saved ', goal, cheapest)
    ans = cheapest
    print("The answer is:", ans)

partone(crabs)
parttwo(crabs)
