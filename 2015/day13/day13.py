#! /usr/bin/python

"""
There are n! arrangements
So a bruteforce algorithm is O(n!).
But there's only 8 people, 8! = 40320.
This is fine, but would look for a more optimal solution if the input was larger
"""

from itertools import permutations
import re

test = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

def gen_key(name1, name2):
    return "{0}:{1}".format(name1, name2)

def load_table(contents):
    happy_table = {}
    names = set()
    regex = re.compile("^([A-Z,a-z]+) would (gain|lose) ([0-9]+) .* ([A-Z,a-z]+)\.$")
    for line in contents.splitlines():
        m = regex.match(line)
        if m == None:
            raise Exception("Bad line: %s" % line)
        m = m.groups()
        value = int(m[2]) if m[1] == 'gain' else -int(m[2])
        happy_table[gen_key(m[0], m[3])] = value
        names.add(m[0])
        names.add(m[3])

    return happy_table, names

def get_optimal(table, names):
    happyness = []
    for p in permutations(names):
        h = []
        for i in range(0, len(p)):
            n1 = p[i]
            n2 = p[(i+1) % len(names)]
            key = gen_key(n1, n2)
            h.append(table[key])
            key = gen_key(n2, n1)
            h.append(table[key])

        happyness.append(h)
    return max([sum(h) for h in happyness ])

table,names = load_table(test)
print get_optimal(table, names)

with open('input.txt', 'r') as f:
    table, names = load_table(f.read())
    print get_optimal(table, names)
