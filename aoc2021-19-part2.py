with open('19-result1.txt', 'r') as fil:
    results = [tuple(map(int, x.split(':')[1].strip().strip('())').split(','))) for x in fil.read().strip().split('\n') if 'position' in x]

def manhattan(pos1, pos2):
    mh = sum(abs(a-b) for a,b in zip(pos1, pos2))
    return(mh)

mh = 0
for i,a in enumerate(results):
    for b in results[i:]:
        mh = max(mh, manhattan(a,b))

print('Advent of Code, day 19, part 2.')
print('The answer is:', mh)
