#! /usr/bin/python

def get_count(dirs):
    positions = [ [0,0], [0,0] ]
    houses = set()
    houses.add((0,0))
    i = 0
    for c in dirs:
        p = i % 2
        i += 1
        if c == '^':
            positions[p][1] += 1
        elif c == '>':
            positions[p][0] += 1
        elif c == 'v':
            positions[p][1] -= 1
        elif c == '<':
            positions[p][0] -= 1
        houses.add((positions[p][0], positions[p][1]))
    return len(houses)

tests = [ ("^v", 3), ("^>v<", 3), ("^v^v^v^v^v", 11) ]
for t in tests:
    assert(get_count(t[0]) == t[1])

with open('input.txt', 'r') as f:
    print "count: %d" % (get_count(f.read().rstrip()))
