with open('19.txt', 'r') as fil:
    parts = [x.split('\n') for x in fil.read().strip().split('\n\n')]

scans = {}

for scanner in parts:
    for s in scanner:
        if 'scanner' in s:
            no = int(s.split(' ')[2])
            scans[no] = []
        else:
            x,y,z = [int(a) for a in s.split(',')]
            scans[no].append((x,y,z))
    scans[no] = tuple(scans[no])

# xr, yr, zr can be 0-4, for rotation.
def rotate(scanner, rotations): # Rotate in any direction ...
    xr, yr, zr = rotations
    rotated = []
    for coord in scanner:
        x, y, z = coord

        if xr > 0:
            # Don't touch the x.
            if xr == 1:
                y1 = z
                z1 = -y
            elif xr == 2:
                y1 = -y
                z1 = -z
            elif xr == 3:
                y1 = -z
                z1 = y
            y = y1
            z = z1

        if yr > 0:
            # Don't touch the y.
            if yr == 1:
                x1 = z
                z1 = -x
            elif yr == 2:
                x1 = -x
                z1 = -z
            elif yr == 3:
                x1 = -z
                z1 = x
            x = x1
            z = z1

        if zr > 0:
            # Don't touch the z.
            if zr == 1:
                x1 = y
                y1 = -x
            elif zr == 2:
                x1 = -x
                y1 = -y
            elif zr == 3:
                x1 = -y
                y1 = x
            x = x1
            y = y1

        rotated.append((x, y, z))
    rotated = tuple(rotated)
    return(rotated)


def rotations(scanner): # Returns a set of all rotations for that scanner.
    rotations = set()
    for xr in range(4):
        for yr in range(4):
            for zr in range(4):
                rotations.add(rotate(scanner, (xr, yr, zr)))
    return(rotations)

def overlap(scannerA, scannerB):
    for beaconA in scannerA:

        for altscannerB in rotations(scannerB):

            for beaconB0 in altscannerB:
                scanBpos = tuple((p - p2) for p,p2 in zip(beaconA, beaconB0))
                count = 0

                news = set()

                for btest in altscannerB:
                    btest = tuple((p + b) for p,b in zip(scanBpos, btest))

                    for atest in scannerA:
                        if btest == atest:
                            count += 1
                            if count == 12:
                                print('position:', scanBpos)
                                for beaconB in altscannerB:
                                    newB = tuple((p + b) for p,b in zip(scanBpos, beaconB))
                                    news.add(newB)
                                return(news)
    return(set())

# Förbättring: Räkna hur många det är kvar att testa,
# jämfört med hur många fler träffar
# det behövs. Sluta testa när det är kört.

ref = 0
beaconset = set(scans[ref])
ans = 0
totest = {b for b in scans} - {ref}
while len(totest) > 0:
    for b in list(totest):
        news = overlap(beaconset, scans[b])
        if len(news) > 0:
            print('match:', b, 'antal:', len(news))
            totest.remove(b)
        print('tested:', b, '(', len(totest), ')', len(beaconset), '+', len(news), '=', len(beaconset.union(news)))
        beaconset = beaconset.union(news)
ans = len(beaconset)

print('Advent of Code, day 19, part 1.')
print('The answer is:', ans)

exit()
print('Advent of Code, day 19, part 2.')
print('The answer is:', 0)
