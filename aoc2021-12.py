with open('12.txt', 'r') as fil:
    m = ([l.strip().split('-') for l in fil ])

map = {} # Map is a dict with cave containing set of neigbhours.
for [t, n] in m:
    for (a,b) in [(t,n), (n,t)]: # Neighbours works both ways.
        if a not in map:
            map[a] = set([b])
        else:
            map[a].add(b)

def part(map, part1):
    print('Advent of Code 2021, day 9, part ' + str(int(not part1) +1) +'.')

    def wayout(map, way, twice):
        # twice is True if the twice rule is used.
        this = way[-1] # Where we are now.
        if this == 'end':
            ways.append(way) # A way is completed.
        else:
            nbs = map[this] - set(['start']) # Neighbours to probably visit.
            if twice:
                nbs = nbs - set([n for n in nbs if n.islower() and n in way ])
                # Remove small caves if twice is used.
            for n in nbs:
                if n.islower() and n in way and not twice:
                    # OK to visit, but then twice is used.
                    wayout(map, way + [n], True)
                else:
                    # Ordinary visit, pass twice through.
                    wayout(map, way + [n], twice)

    ways = []
    wayout(map, ['start'], part1) # Start from 'start' without twice used.
    print("The answer is:", len(ways))

part(map, True) # Same as part 2 but without going twice any time.
part(map, False)
