#! /usr/bin/python

def get_position(dirs):
    floor = 0
    p = 1
    for c in dirs:
        step = 1 if c == '(' else -1
        floor += step
        if floor == -1:
            return p
        p += 1
    return floor

assert(get_position(")") == 1)
assert(get_position("()())") == 5)

with open('input.txt', 'r') as f:
    print get_position(f.read().rstrip())
