with open('16-t1.txt', 'r') as fil:
    code = fil.read().strip()

print(code)
h_size = len(code) * 4
bincode = str((bin(int(code, 16))[2:]).zfill(h_size))

print(bincode)

def run(code, i=0):
    print(code)
    while i < len(code):
        print(i, len(code), code)
        print(int(code[i:], 2))
        if int(code[i:], 2) == 0:
            break
        v = int(code[i:i+3], 2)
        i += 3
        t_id = int(code[i:i+3], 2)
        i += 3
        print('V', v, 'T', t_id)
        if t_id == 4: # Literal packet
            more, bits = int(code[i], 2), code[i+1:i+5]
            i += 5
            print(more, bits)
            while more:
                more, nbit = int(code[i], 2), code[i+1:i+5]
                print(more, nbit)
                bits += nbit
                i += 5
            lit = int(bits, 2)
            print(lit)
        else: # Operator packet
            lt_id = int(code[i])
            i += 1
            if lt_id: # Number of sub packets
                l = int(code[i:i+11], 2)
                i += 11
                # och nu då?
            else: # length of subpackets
                l = int(code[i:i+15], 2)
                i += 15
                # och nu då?



run(bincode)
#print('version sum', versum)
print()
#interpret('01010000001')
#interpret('10010000010')
#interpret('0011000001100000')

#interpret('110100010100101001000100100')
exit()

def partone():
    print("Advent of Code 2021, day 16, part 1.")
    print("The answer is:")
    #pprint(m)
#partone()
