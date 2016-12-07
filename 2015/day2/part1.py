#! /usr/bin/python

def parse_line(line):
    return [ int(x) for x in line.split("x") ]

def paper_needed(line):
    dimens = parse_line(line)
    h,w,l = dimens
    smallest = sorted(dimens)[0:2]

    return (2 * h * l) + (2 * w * h) + (2 * w * l) + (smallest[0] * smallest[1])

assert(paper_needed("2x3x4") == 58)
assert(paper_needed("1x1x10") == 43)

with open('input.txt', 'r') as f:
    needed = 0
    for line in f:
        needed += paper_needed(line.rstrip())
    print "paper needed: %d" % needed 
