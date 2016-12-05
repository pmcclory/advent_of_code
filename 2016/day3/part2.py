#! /usr/bin/python

with open("input.txt", "r") as f:

    count = 0
    line_number = 1
    tri = [[], [], []]
    for line in f:
        d = [ int(x) for x in line.strip().split(" ") if len(x) > 0 ]
        tri[0].append(d[0])
        tri[1].append(d[1])
        tri[2].append(d[2])

        if len(tri[0]) == 3:
            for t in tri:
                t = sorted(t)
                if t[0] + t[1] > t[2]:
                    count += 1
            tri = [[], [], []]
    print count
