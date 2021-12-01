fil = open('aoc2021-01-input.txt', 'r')
lines = [int(x) for x in fil.read().split('\n')[:-1]]

def partone():
    print("Advent of Code 2021, day 1, part 1.")
    i = 1
    no = 0

    while i < len(lines):
        if lines[i] > lines[i-1]:
            no += 1
        i +=1
    print("The answer is:", no)

def parttwo():
    print("Advent of Code 2021, day 1, part 2.")
    i = 3
    no = 0

    while i < len(lines):
        A = lines[i-1:i-4]
        B = lines[i:i-2]
        if B > A:
            no +=1
        i += 1
    print("The answer is:", no)

partone()
parttwo()
