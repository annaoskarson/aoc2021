with open('18.txt', 'r') as fil:
    lines = fil.read().strip().split('\n')

import json

def magnitude(ls): # Calculates the magnitude of a task.
    left, right = ls[0], ls[1]
    if type(left) is int and type(right) is int:
        return(3 * left + 2 * right)
    elif type(left) is int:
        return(3 * left + 2 * magnitude(right))
    elif type(right) is int:
        return(3 * magnitude(left) + 2 * right)
    else:
        return(magnitude([magnitude(ls[0]), magnitude(ls[1])]))

def dpt(ls): # Returns the depth of a list.
    if isinstance(ls, list):
        return(1 + max(dpt(item) for item in ls))
    else:
        return(0)

def split(n): # Splits a number into a list.
    if type(n) is str:
        n = int(n)
    left = n // 2
    right = n // 2 + (n % 2 > 0)
    return([left, right])

def explode(ls): # Exploads a task, if it needs to be exploded.
    if dpt(ls) <= 4:
        return(ls)
    else:
        ls = estring(ls)
        depth = 0
        lleft = 0
        rright = 0
        i = 0
        while i < len(ls):
            if ls[i] == '[':
                depth += 1
            elif ls[i] == ']':
                depth -= 1
            elif type(ls[i]) is int:
                lleft = i
            else:
                pass
            i += 1

            if depth == 5:
                lefti = i
                righti = i+2
                i += 3
                while i < len(ls) and rright == 0:
                    if type(ls[i]) is int:
                        rright = i
                    i += 1
                if rright > 0:
                    newright = ls[rright] + ls[righti]
                    ls[rright] = newright
                if lleft > 0:
                    newleft = ls[lleft] + ls[lefti]
                    ls[lleft] = newleft
                ls[lefti-1] = 0
                for j in range(4):
                    ls.pop(lefti)
                return(destring(ls))

def estring(ls): # Makes a special list type with strings and ints from a list.
    ls = list(str(ls).replace(' ', ''))
    new = []
    i = 0
    while i < len(ls):
        if ls[i] == '[':
            new += ls[i]
        elif ls[i] == ']':
            new += ls[i]
        elif ls[i] == ',':
            new += ls[i]
        else:
            digit = ls[i]
            while ls[i+1].isdigit():
                digit += ls[i+1]
                i += 1
            digit = int(digit)
            new.append(digit)
        i += 1
    return(new)

def destring(ls): # Takes back from estring to a list.
    new = ''
    for l in ls:
        if type(l) == int:
            l = str(l)
        new += l
    new = json.loads(new)
    return(new)

def splitt(ls): # Makes a split on a string.
    ls = list(str(ls).replace(' ', ''))
    i = 0
    while i < len(ls):
        if ls[i].isdigit() and ls[i+1].isdigit():
            new = split(''.join(ls[i:i+2]))
            new = list(str(new))
            for _ in range(2):
                _ = ls.pop(i)
            for pos in range(len(new)):
                ls.insert(i + pos, new[pos])
            ls = ''.join(ls)
            ls = json.loads(ls)
            return(ls)
        i += 1
    ls = ''.join(ls)
    ls = json.loads(ls)
    return(ls)

def maths(task): # Does the maths on a task.
    done = False
    while not done:
        task = explode(task)
        if dpt(task) < 5:
            task2 = splitt(task)
            if task2 == task:
                done = True
            else:
                task = task2
    return(task)

def partone(lines):
    task = json.loads(lines[0])
    for l in lines[1:]:
        l = json.loads(l)
        task = [task, l]
        task = maths(task)
    task = magnitude(task)
    return(task)

def parttwo(lines):
    sum = 0
    for k in range(len(lines)):
        for m in range(k+1, len(lines)):
            taskk = json.loads(lines[k])
            taskm = json.loads(lines[m])
            task1 = [taskk, taskm]
            task2 = [taskm, taskk]
            ans1 = magnitude(maths(task1))
            ans2 = magnitude(maths(task2))
            sum = max(sum, ans1, ans2)
    return(sum)

print('Advent of Code, day 18, part 1.')
print('The answer is:', partone(lines))

print('Advent of Code, day 18, part 2.')
print('The answer is:', parttwo(lines))
