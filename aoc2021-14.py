with open('14.txt', 'r') as fil:
    lines = fil.read().strip().split('\n')

p = lines[0]
#print(p)
subs = {}
for l in lines[2:]:
    a, b = l.split(' -> ')
    subs[a] = b

def generate(old, su):
    newcontent = {}
    for pair in old:
        newpairs = [pair[0] + su[pair], su[pair] + pair[1]]
        for p in newpairs:
            if p not in newcontent:
                newcontent[p] = 0
            newcontent[p] += old[pair]
    return(newcontent)

def part(p, subs, times):
    content = {}
    for i in range(len(p)-1):
        pair = p[i:i+2]
        if pair not in content:
            content[pair] = 0
        content[pair] += 1
    for i in range(times):
        content = generate(content, subs)
    results = {}
    for pair in content:
        c = pair[0]
        if c not in results:
            results[c] = 0
        results[c] += content[pair]
    c = p[-1]
    if c not in results:
        results[c] = 0
    results[c] += 1
    ans = max(results.values())- min(results.values())
    return(ans)

print('Advent of Code 2021, day 14 part 1.')
ans = part(p, subs, 10)
print('The answer is:', ans)
print('Advent of Code 2021, day 14 part 2.')
ans = part(p, subs, 40)
print('The answer is:', ans)
