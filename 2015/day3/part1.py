#! /usr/bin/python

def get_count(dirs):
    pos = [0,0]
    houses = set()
    houses.add((0,0))
    for c in dirs:
        if c == '^':
            pos[1] += 1
        elif c == '>':
            pos[0] += 1
        elif c == 'v':
            pos[1] -= 1
        elif c == '<':
            pos[0] -= 1
        houses.add((pos[0], pos[1]))
    return len(houses)

tests = [ (">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2) ]
for t in tests:
    assert(get_count(t[0]) == t[1])

with open('input.txt', 'r') as f:
    print "count: %d" % (get_count(f.read().rstrip()))
