fil = open('aoc2021-01-input.txt', 'r')
lines = [int(x) for x in fil.read().split('\n')[:-1]]

def partone():
    print("Advent of Code 2021, day 1, part 1.")
    ans = len([1 for i in range(len(lines)) if lines[i] > lines[i-1]])
    print("The answer is:", ans)

def parttwo():
    print("Advent of Code 2021, day 1, part 2.")
    ans = len([1 for i in range(3, len(lines)) if sum(lines[i:i-3:-1]) > sum(lines[i-1:i-4:-1])])
    print("The answer is:", ans)

partone()
parttwo()
