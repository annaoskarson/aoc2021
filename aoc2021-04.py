fil = open('4.txt', 'r')
lines = fil.read().strip()

loket = [int(x) for x in lines.split('\n\n')[:1][0].split(',')]

bricks = [rows.split('\n') for rows in lines.split('\n\n')[1:]]
# Det borde gå att få till någon svår harang ...
#print([[int(x) for x in r.split(' ') if x != ''] for rows in lines.split('\n\n')[1:] for r in rows.split('\n')])

brickor = []
for b in bricks:
    newbrick = []
    for r in b:
        newbrick.append([int(x) for x in r.split(' ') if x != ''])
    brickor.append(newbrick)

def partone(brickor, loket):
    print("Advent of Code 2021, day 4, part 1.")

    def bingotal(brickor):
        for bricka in brickor:
            cols = list(map(list, zip(*bricka)))
            testbrick = bricka + cols

            for rad in testbrick:
                if all([r < 0 for r in rad]): # Bingo!
                    #returnera summan av alla tal som inte är negativa på brickan
                    return(sum([x for rs in bricka for x in rs if x > 0]))
        return(0)

    for tal in loket:
        for bricka in brickor:
            for i, row in enumerate(bricka):
                bricka[i] = [-3 if x == tal else x for x in row]

        b = bingotal(brickor)

        if b != 0:
            ans = b*tal
            print("The answer is:", ans)
            break

def parttwo(brs2, loket):
    print("Advent of Code 2021, day 4, part 2.")

    def harbingo(bricka):
        cols = list(map(list, zip(*bricka)))
        testbrick = bricka + cols
        for rad in testbrick:
            if all([r < 0 for r in rad]):
                return(True)
        return(False)

    def bingotal(bricka):
        return(sum([x for rs in bricka for x in rs if x > 0]))

    def utrop(talet, brs):
        for br in brs:
            for i, row in enumerate(br):
                br[i] = [-3 if x == talet else x for x in row]
        return(brs)

    def check(brs):
        bt = 0
        rem = []
        for brick in brs:
            if harbingo(brick):
                bt = bingotal(brick)
                rem.append(brick)
        for j in rem:
            brs.remove(j)
        return(bt, brs)

    for tal in loket:
        brs2 = utrop(tal, brs2)
        bt, brs2 = check(brs2)
        if bt != 0:
            ans = bt*tal
        if len(brs2) < 1:
            break
    print("The answer is:", ans)

partone(brickor, loket)
# Fortsätt med samma brickor, så har de redan spelats ett tag.
# Man skulle kunna räkna fram loket också om man vill
parttwo(brickor, loket)
