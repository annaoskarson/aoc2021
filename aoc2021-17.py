with open('17.txt', 'r') as fil:
    line = fil.read().strip()

#line = 'target area: x=20..30, y=-10..-5'
#line = 'target area: x=236..262, y=-78..-58'
xmin, xmax, ymin, ymax = [int(b) for a in line.split(':')[1].strip().split(',') for b in a.strip().split('=')[1].split('..')]
#print(type(xmin))
def stepx(x, vx):
    x += vx
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    return(x, vx)

def stepy(y, vy):
    y += vy
    vy -= 1
    return(y, vy)

def hit(x,y, xmin, xmax, ymin, ymax):
    return((xmin <= x <= xmax) and (ymin <= y <= ymax))

#y = 0
# vy + 1 > 0 - ymin


def part(xmin, xmax, ymin, ymax):
    #print(xmin, xmax, ymin, ymax, '\n')
    ans = set()
    hits = []
    for svy in range(ymin, 500, 1):
        for svx in range(1, xmax+1, 1):
            #print(svx)
            vx, vy = svx, svy
            x, y = 0, 0
            ygoal = -float('inf')
            while x <= xmax and y >= ymin:
                x, vx = stepx(x, vx)
                y, vy = stepy(y, vy)
                ygoal = max(ygoal, y)
                if hit(x,y, xmin, xmax, ymin, ymax):
                    ans.add(ygoal)
                    hits.append('träff')
                    #hits.add((svx, svy))
                    break
    return(ans, hits)
print('Advent of Code, day 17, part 1.')
p1, p2 = part(xmin,xmax,ymin,ymax)
print(max(p1))
#print(p1)
print('Advent of Code, day 17, part 2.')
print(len(p2))
#print(sorted(p2))

# 1582 too low
# 1528 too low
