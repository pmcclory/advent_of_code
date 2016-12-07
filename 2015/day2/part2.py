#! /usr/bin/python

def parse_line(line):
    return [ int(x) for x in line.split("x") ]

def paper_needed(line):
    dimens = parse_line(line)
    h,w,l = dimens
    smallest = sorted(dimens)[0:2]
    return (h * w * l) + (2 * sum(smallest))

assert(paper_needed("2x3x4") == 34)
assert(paper_needed("1x1x10") == 14)

with open('input.txt', 'r') as f:
    needed = 0
    for line in f:
        needed += paper_needed(line.rstrip())
    print "paper needed: %d" % needed 
