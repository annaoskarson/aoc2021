with open('8.txt', 'r') as fil:
    ls = [[s.strip().split(' ') for s in r.split('|')] for r in fil.read().strip().split('\n') ]

def partone(ls):
    print("Advent of Code 2021, day 8, part 1.")
    count = 0
    for l in ls:
        count += sum(1 for d in l[1] if len(d) in [2, 3, 4, 7])
    print("The answer is:", count)

def parttwo(ls):

    def numbers(ns):
        #print(ns)
        nums = {}
        nums[[('').join(sorted(n)) for n in ns if len(n) == 2][0]] = 1
        nums[[('').join(sorted(list(n))) for n in ns if len(n) == 3][0]] = 7
        nums[[('').join(sorted(n)) for n in ns if len(n) == 4][0]] = 4
        nums[[('').join(sorted(n)) for n in ns if len(n) == 7][0]] = 8

        ABCDEFG = set([n for n in ns if len(n) == 7][0])
        ACF = set([n for n in ns if len(n) == 3][0])
        CF = set([n for n in ns if len(n) == 2][0])
        BCDF = set([n for n in ns if len(n) == 4][0])
        A = ACF - CF
        BD = BCDF - CF
        # 2, 3, 5 have five digits, segments in common: A, D, G
        temp = [set(n) for n in ns if len(n) == 5]
        ADG = temp[0] & temp[1] & temp[2]
        # 9, 6, 0 have six digits, segments in common: B, D, E, F, G
        temp = [set(n) for n in ns if len(n) == 6]
        BDEFG = temp[0] & temp[1] & temp[2]

        C = CF - BDEFG
        F = CF - C
        EFG = ABCDEFG - A - BCDF
        EG = EFG - F
        DG = BDEFG & ADG
        G = EG & DG
        B = BD - ADG
        D = BD - B
        E = EG - G

        nums[('').join(sorted(list(A | C | D | E | G)))] = 2
        nums[('').join(sorted(list(A | C | D | F | G)))] = 3
        nums[('').join(sorted(list(A | B | D | F | G)))] = 5
        nums[('').join(sorted(list(A | B | D | E |F | G)))] = 6
        nums[('').join(sorted(list(A | B | C | D | F | G)))] = 9
        nums[('').join(sorted(list(A | B | C | E | F | G)))] = 0
        return(nums)

    print("Advent of Code 2021, day 8, part 2.")
    sum = 0
    for l in ls:
        defs = [('').join(sorted(list(n))) for n in l[0]]
        digits = [('').join(sorted(list(n))) for n in l[1]]
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