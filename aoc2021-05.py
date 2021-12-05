with open('5.txt', 'r') as fil:
    coords = ([[int(c) for c in row.split(',')] for row in fil.read().strip().replace(' -> ', ',').split('\n')])

def partone(coords):
    print("Advent of Code 2021, day 5, part 1.")
    kartan = {}
    for (x1, y1, x2, y2) in coords:
        if (x1 == x2):
            (y1, y2) = sorted((y1, y2))
            for y in range(y1, y2+1):
                if (x1, y) not in kartan:
                    kartan[x1, y] = 0
                kartan[x1, y] += 1
        if (y1 == y2):
            (x1, x2) = sorted((x1, x2))
            for x in range(x1, x2+1):
                if (x, y1) not in kartan:
                    kartan[x, y1] = 0
                kartan[x, y1] += 1

    ans = sum([1 for x in kartan.values() if x > 1])
    print("The answer is:", ans)

def parttwo(coords):
    print("Advent of Code 2021, day 5, part 2.")
    kartan = {}
    for (x1, y1, x2, y2) in coords:

        if (x1 == x2):
            (y1, y2) = sorted((y1, y2))
            for y in range(y1, y2+1):
                if (x1, y) not in kartan:
                    kartan[x1, y] = 0
                kartan[x1, y] += 1
        elif (y1 == y2):
            (x1, x2) = sorted((x1, x2))
            for x in range(x1, x2+1):
                if (x, y1) not in kartan:
                    kartan[x, y1] = 0
                kartan[x, y1] += 1
        else:
            (dx, dy) = (1,1)
            if x1 > x2:
                dx = -1
            xs = [x for x in range(x1, x2, dx)] + [x2]
            if y1 > y2:
                dy = -1
            ys = [y for y in range(y1, y2, dy)] + [y2]
            i = 0
            while i < len(xs):
                x,y = xs[i], ys[i]
                if (x, y) not in kartan:
                    kartan[x,y] = 0
                kartan[x,y] += 1
                i += 1

    ans = sum([1 for x in kartan.values() if x > 1])
    print("The answer is:", ans)

partone(coords)
parttwo(coords)
