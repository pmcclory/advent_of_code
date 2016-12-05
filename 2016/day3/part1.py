#! /usr/bin/python

with open("input.txt", "r") as f:
    count = 0
    for l in f.readlines():
        d = sorted([ int(x) for x in l.strip().split(" ") if len(x) > 0 ])
        if d[0] + d[1] > d[2]:
            count += 1

    print count
