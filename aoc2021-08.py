with open('8.txt', 'r') as fil:
    ls = [[s.strip().split(' ') for s in r.split('|')] for r in fil.read().strip().split('\n') ]

def partone(ls):
    print("Advent of Code 2021, day 8, part 1.")
    count = 0
    for defs, digits in ls:
        count += len([d for d in digits if len(d) in [2, 3, 4, 7]])
    print("The answer is:", count)

def parttwo(ls):

    def numbers(ns): # Returns a translation dict for the digits.
        nums = {}
        # First add the digits we already know the segments for.
        nums[[('').join(sorted(n)) for n in ns if len(n) == 2][0]] = 1
        nums[[('').join(sorted(n)) for n in ns if len(n) == 3][0]] = 7
        nums[[('').join(sorted(n)) for n in ns if len(n) == 4][0]] = 4
        nums[[('').join(sorted(n)) for n in ns if len(n) == 7][0]] = 8

        # Try to distinguish each segment separated form the rest.
        # First, the four digits we know the segments for.
        ABCDEFG = set([n for n in ns if len(n) == 7][0])
        ACF = set([n for n in ns if len(n) == 3][0])
        CF = set([n for n in ns if len(n) == 2][0])
        BCDF = set([n for n in ns if len(n) == 4][0])
        # From these we get:
        A = ACF - CF
        BD = BCDF - CF

        # 2, 3, 5 have five digits, segments in common: A, D, G
        temp = [set(n) for n in ns if len(n) == 5]
        ADG = temp[0] & temp[1] & temp[2]

        # 6, 9, 0 have six digits, segments in common: B, D, E, F, G
        temp = [set(n) for n in ns if len(n) == 6]
        BDEFG = temp[0] & temp[1] & temp[2]

        # And now we can separate all segments.
        B = BD - ADG
        D = BD - B

        DG = BDEFG & ADG
        C = CF - BDEFG
        F = BDEFG & CF

        EG = ABCDEFG - ACF - BCDF
        G = EG & DG
        E = EG - G

        # Now we have all segments separated and can build the rest of the digits manually.
        nums[('').join(sorted(list(A | C | D | E | G)))] = 2
        nums[('').join(sorted(list(A | C | D | F | G)))] = 3
        nums[('').join(sorted(list(A | B | D | F | G)))] = 5
        nums[('').join(sorted(list(A | B | D | E | F | G)))] = 6
        nums[('').join(sorted(list(A | B | C | D | F | G)))] = 9
        nums[('').join(sorted(list(A | B | C | E | F | G)))] = 0
        return(nums)

    print("Advent of Code 2021, day 8, part 2.")
    sum = 0
    for defs, digits in ls:
        defs = [('').join(sorted(list(n))) for n in defs]
        digits = [('').join(sorted(list(n))) for n in digits]
        ns = numbers(defs)
        this = ''
        for t in digits:
            t = ('').join(sorted(t))
            if t in ns:
                this += str(ns[t])
            else:
                print(t, ' not in dict ---------') # Felsökningen. :)
        sum += int(this)

    print("The answer is:", sum)
    # 834562 too low

partone(ls)
parttwo(ls)
