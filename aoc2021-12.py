map = {}
with open('12.txt', 'r') as fil:
    m = ([l.strip().split('-') for l in fil ])

for [t, n] in m:
    if t not in map:
        map[t] = set([n])
    else:
        map[t].add(n)
    if n not in map:
        map[n] = set([t])
    else:
        map[n].add(t)

def partone(map):
    print("Advent of Code 2021, day 12, part 1.")
    ways = []
    def wayout(map, way):
        this = way[-1]
        if this == 'end':
            ways.append(way)
        else:
            nbs = map[this] # neighbours to visit
            nbs = nbs - set([n for n in nbs if n.islower() and n in way])
            # Man får inte gå tillbaka till start(?) eller till någon liten grotta man redan besökt.
            for n in nbs:
                wayout(map, way + [n])

    wayout(map, ['start'])
    print("The answer is:", len(ways))

def parttwo(map):
    print("Advent of Code 2021, day 9, part 2.")
    ways = []
    def wayout(map, way, twice):
        # twice == True om den är utnyttjad redan
        this = way[-1]
        if this == 'end':
            ways.append(way)
        else:
            nbs = map[this] # neighbours to visit
            nbs = nbs - set(['start'])
            if twice:
                nbs = nbs - set([n for n in nbs if n.islower() and n in way])
                # Ta bort små grottor om twice är utnyttjad.
            for n in nbs:
                if n.islower() and n in way and not twice:
                    #OK att besöka n, men sätt twice till True.
                    wayout(map, way + [n], True)
                else:
                    wayout(map, way + [n], twice)

    wayout(map, ['start'], False)
    print("The answer is:", len(ways))

partone(map)
parttwo(map)
