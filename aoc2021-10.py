with open('10.txt', 'r') as f:
	rows = f.read().split('\n')

scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}
endscoring = {'(': 1, '[': 2, '{':3, '<': 4}

starts = ['(', '[', '{', '<']
ends = [')', ']', '}', '>']

score = 0
endscr = []
def points(r):
	stack = []
	for c in r:
		if c in starts:
			stack.append(c)
		elif c in ends:
			s = stack[-1]
			if starts.index(s) != ends.index(c):
				return(scoring[c],[])
			else:
				stack.pop()
	return(0, stack)

def endscore(l):
	scr = 0
	l.reverse()
	for c in l:
		scr = scr * 5
		scr += endscoring[c]
	return(scr)

for r in rows:
	scr, ending = points(r)
	score += scr
	if len(ending) > 0:
		endscr.append(endscore(ending))

print('1:', score)
endscr.sort()
print('2:', endscr[len(endscr)//2])
