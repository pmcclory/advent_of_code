#! /usr/bin/python

"""
This is just traveling salesman
which we know there is known polynomial solution for
Looking at all possible paths is O(n!) - but there's
only 7 cities == 5040 combinations.  That's fine
"""

import re
import itertools

PART2 = True 
m = -1 if PART2 else 1

def gen_key(city1, city2):
    return "{0}->{1}".format(*sorted([city1, city2]))

def get_best_route(cities, distance_table):
    best = None
    print distance_table
    for p in itertools.permutations(cities):
        score = 0
        for i in range(0, len(p) - 1):
            src = p[i]
            dst = p[(i+1)]
            score += distance_table[gen_key(src, dst)] * m
        if not best or score < best[0]:
            best = (score, p)
    return (best[0] * m, best[1])

def load_table(lines):
    distances = {}
    cities = set()
    regex = re.compile('(.*) to (.*) = ([0-9]+)')
    for l in lines:
        m = regex.match(l)
        if m == None:
            raise Exception("Bad input line: %s" % l)
        src,dst,distance = m.groups()
        cities.add(src)
        cities.add(dst)
        distances[gen_key(src,dst)] = int(distance)
    return cities, distances

tbl = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

cities, table = load_table(tbl.splitlines())
print get_best_route(cities, table)

with open('input.txt', 'r') as f:
    cities, table = load_table(f.readlines())
    print get_best_route(cities, table)
