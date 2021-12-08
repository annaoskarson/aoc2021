
with open('02.txt', 'r') as f:
	coms = f.read().split('\n')

(x,y) = (0,0)
for com in coms:
	[d, v] = com.split(' ')
	if d == 'forward':
		x += int(v)
	elif d == 'up':
		y -= int(v)
	elif d == 'down':
		y += int(v)

print('1: ', x*y)


(x,y,a) = (0,0,0)
for com in coms:
	[d, v] = com.split(' ')
	if d == 'forward':
		x += int(v)
		y += a*int(v)
	elif d == 'up':
		a -= int(v)
	elif d == 'down':
		a += int(v)

print('2: ', x*y)
