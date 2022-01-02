
# A = 1
# B = 10
# C = 100
# D = 1000

def partone():
    # Played it by hand a few times until right.

    #############
    #...........#
    ###A#D#C#A###
      #C#D#B#B#
      #########

    #############
    #.A.......A.#
    ###.#D#C#.###
      #C#D#B#B#
      #########
    ans = 2 + 2

    #############
    #.A.B.....A.#
    ###.#D#C#.###
      #C#D#B#.#
      #########
    ans += 70

    #############
    #.A.B.....A.#
    ###.#.#C#D###
      #C#.#B#D#
      #########
    ans += 7000 + 7000

    #############
    #.A.......A.#
    ###.#.#C#D###
      #C#B#B#D#
      #########
    ans += 30

    #############
    #.A.....C.A.#
    ###.#.#.#D###
      #C#B#B#D#
      #########
    ans += 200

    #############
    #.A.....C.A.#
    ###.#B#.#D###
      #C#B#.#D#
      #########
    ans += 50

    #############
    #.A.....C.A.#
    ###.#B#.#D###
      #.#B#C#D#
      #########
    ans += 800

    #############
    #.A.......A.#
    ###.#B#C#D###
      #.#B#C#D#
      #########
    ans += 200

    #############
    #...........#
    ###A#B#C#D###
      #A#B#C#D#
      #########
    ans += 3 + 8

    print('Advent of Code, day 23 part 1.')
    print('The answer is', ans)

partone()

#############
#01.2.3.4.56#
###A#D#C#A###
  #D#C#B#A#
  #D#B#A#C#
  #C#D#B#B#
  #########

# obstacle for going from 'A' to 0 is [1] and price is 3
path = {'A': {0: (3, [1]), 1: (2, []), 2: (2,[]), 3: (4, [2]), 4: (6, [2, 3]), 5: (8, [2, 3, 4]), 6: (9, [2, 3, 4, 5])},
        'B': {0: (5, [2, 1]), 1: (4, [2]), 2: (2, []), 3: (2, []), 4: (4, [3]), 5: (6, [3, 4]), 6: (7, [3, 4, 5])},
        'C': {0: (7, [3, 2, 1]), 1: (6, [3, 2]), 2: (4, [3]), 3: (2, []), 4: (2, []), 5: (4, [4]), 6: (5, [4, 5])},
        'D': {0: (9, [4, 3, 2, 1]), 1: (8, [4, 3, 2]), 2: (6, [4, 3]), 3: (4, [4]), 4: (2, []), 5: (2, []), 6: (3, [5])}
        }

import copy

def pprint(state):
    image = '\n' + '#' * 13
    image += '\n#'

    for i in range(7):
        if state[i] == None:
            image += '.'
        else:
            image += state[i]
        if i in [1, 2, 3, 4]:
            image += '.'
    image += '#\n'

    for i in range(len(state['A'])):
        if i == 0:
            image += '##'
        else:
            image += '  '
        for type in ['A', 'B', 'C', 'D']:
            image += '#'
            if state[type][i] != None:
                image += state[type][i]
            elif state['home'][type] >= len(state[type]) - i:
                image += type
            else:
                image += '.'
        if i == 0:
            image += '###\n'
        else:
            image += '#  \n'
    image += '  ' + '#' * 9 + '  \n'
    print(image)

def okToGo(fr, to, path, state): # From str to int
    if all(a == None for a in state[fr]):
        # No amph to go with.
        return(False)
    obstacles = [state[pos] for pos in path[fr][to][1]] + [state[to]]
    # Checking path and destination for obstacles
    return(all(o == None for o in obstacles))

def factor(amph):
    if amph == 'A':
        return(1)
    elif amph == 'B':
        return(10)
    elif amph == 'C':
        return(100)
    elif amph == 'D':
        return(1000)

def go(fr, to, path, state): # from str, to int
    if okToGo(fr, to, path, state):
        newstate = copy.deepcopy(state)
        i = next(newstate[fr].index(a) for a in newstate[fr] if a != None)
        # How far down the first amph is
        c = (path[fr][to][0] + i) * factor(newstate[fr][i]) # Cost to go
        newstate[to] = newstate[fr][i] # Move to destination
        newstate[fr][i] = None # Remove from origin
        return(c, newstate)
    return(0, state)

def gohome(path, state):
    for a in ['A', 'B', 'C', 'D']:
        # Check if someone is at home without going.
        if any([b == a for b in state[a]]) and not any([b != a and b != None for b in state[a]]):
            state['home'][a] += len([b for b in state[a] if a == b])
            state[a] = [None for b in state[a]]

    cs = 0
    changed = True
    while changed:
        cstart = cs
        for fr in [a for a in [0, 1, 2, 3, 4, 5, 6] if state[a] != None]:
            to = state[fr]
            if all([a == None for a in state[to]]) and all(state[a] == None for a in path[to][fr][1]):
                # OK to go home.
                cs += (path[to][fr][0] + (len(state[to])-1 - state['home'][to])) * factor(to)
                state['home'][to] += 1
                state[fr] = None
        changed = cstart != cs
    return(cs, state)

def finished(state):
    return(sum(state['home'].values()) == len(state['A'] * 4))

def play(path, state, cost):
    c, state = gohome(path, state)
    cost += c

    if finished(state):
        return(cost)

    minc = float('inf')
    for fr in ['A', 'B', 'C', 'D']:
        for to in [0, 1, 2, 3, 4, 5, 6]:
            c, newstate = go(fr, to, path, state)
            if c != 0:
                # If it was a possible move
                newc = play(path, newstate, cost + c)
                minc = min(minc, newc)
    return(minc)

def parttwo(path):
    print('Advent of Code, day 23 part 2.')
    state = {'A': ['A', 'D', 'D', 'C'],
            'B': ['D', 'C', 'B', 'D'],
            'C': ['C', 'B', 'A', 'B'],
            'D': ['A', 'A', 'C', 'B'],
            0: None, 1: None, 2: None, 3: None,
            4: None, 5: None, 6: None,
            'home': {'A': 0, 'B': 0, 'C': 0, 'D': 0}}

    cost = play(path, state, 0)
    print('The answer is', cost)

parttwo(path)
