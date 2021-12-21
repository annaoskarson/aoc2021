with open('16.txt', 'r') as fil:
    code = fil.read().strip()

h_size = len(code) * 4
bincode = str((bin(int(code, 16))[2:]).zfill(h_size))

def decode(code, i):
    while i < len(code):

        V = int(code[i:i+3], 2)
        i += 3
        ID = int(code[i:i+3], 2)
        i += 3

        if ID == 4: # literal

            lit = ''
            more = 1
            while more:
                more = int(code[i], 2)
                i += 1
                lit += code[i:i+4]
                i += 4
            lit = int(lit, 2)

            if i >= len(code) or int(code[i:], 2) == 0:
                return({'Version': V, 'ID': ID, 'Content': lit}, len(code))
            else:
                return({'Version': V, 'ID': ID, 'Content': lit}, i)

        else: # operator packet
            l = code[i]
            l = int(l, 2)
            i += 1

            if l:
                num = code[i:i+11]
                i += 11
                num = int(num, 2)

                packages = []
                for _ in range(num):
                    pak, i = decode(code, i)
                    packages.append(pak)
                return({'Version': V, 'ID': ID, 'Content': packages}, i)

            else:
                length = code[i:i+15]
                i += 15
                length = int(length, 2)
                packages = []
                stop = i + length
                now = i
                while i < stop:
                    pak, i = decode(code, i)
                    packages.append(pak)
                return({'Version': V, 'ID': ID, 'Content': packages}, i)

def versionsum(packets):
    if type(packets['Content']) is int:
        return(packets['Version'])
    else:
        return(packets['Version'] + sum([versionsum(a) for a in packets['Content']]))

def evaluate(packets):
    id = packets['ID']
    content = packets['Content']

    if id == 0:
        result = sum(evaluate(p) for p in content)
    elif id == 1:
        result = 1
        for p in content:
            result = result * evaluate(p)
    elif id == 2:
        result = min(evaluate(p) for p in content)
    elif id == 3:
        result = max(evaluate(p) for p in content)
    elif id == 4:
        return(content)
    elif id == 5:
        result = evaluate(content[0]) > evaluate(content[1])
    elif id == 6:
        result = evaluate(content[0]) < evaluate(content[1])
    elif id == 7:
        result = evaluate(content[0]) == evaluate(content[1])
    return(result)

def partone(code):
    print('Advent of Code, day 16 part 1.')
    packets, _ = decode(bincode, 0)
    vsum = versionsum(packets)
    print('The answer is', vsum)

partone(bincode)

def parttwo(code):
    print('Advent of Code, day 16, part 2.')
    packets, _ = decode(bincode, 0)
    ans = evaluate(packets)
    print('The answer is', ans)

parttwo(bincode)
