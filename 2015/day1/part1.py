#! /usr/bin/python

def get_floor(dirs):
    floor = 0 
    for c in dirs:
        step = 1 if c == '(' else -1
        floor += step
    return floor

assert(get_floor("(())") == 0)
assert(get_floor("()()") == 0)
assert(get_floor("(((") == 3)
assert(get_floor("(()(()(") == 3)
assert(get_floor("))(((((") == 3)
assert(get_floor("())") == -1)
assert(get_floor("))(") == -1)
assert(get_floor(")))") == -3)
assert(get_floor(")())())") == -3)

with open('input.txt', 'r') as f:
    print get_floor(f.read().rstrip())
