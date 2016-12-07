#! /usr/bin/python

"""
Use matrix + matrix addition rather than these loops
"""

import re
import np

OFF = -1
ON = 1
TOGGLE = 2

matrix = None

def init(state=OFF):
    global matrix
    matrix = np.empty((1000,1000))
    matrix.fill(OFF)

def count():
    global matrix
    return matrix.sum()

def parse_step(step):
    if step.startswith("turn on"):
        op = ON
    elif step.startswith("turn off"):
        op = OFF
    else:
        op = TOGGLE
    regex = re.compile('.* ([0-9]+,[0-9]+) through ([0-9]+,[0-9]+)')
    c1,c2 = regex.match(step).groups()
    c1 = [ int(x) for x in c1.split(",") ]
    c2 = [ int(x) for x in c2.split(",") ]
    return (op, c1, c2)

def do_step(step):
    op,c1,c2 = parse_step(step)
    m2 = np.empty((1000,1000))
    m2.fill(0)
    for row in range(c1[1], c2[1] + 1):
        for col in range(c1[0], c2[0] + 1):
            if op == TOGGLE:
                m2[row][col] = (matrix[row][col] + 1) % 2
            else:
                m2[row][col] = op

init()
do_step("turn on 0,0 through 999,999")
print count()

init()
do_step("toggle 0,0 through 999,0")
print count()

init(ON)
do_step("turn off 499,499 through 500,500")
print count()

with open('input.txt', 'r') as f:
    init(OFF)
    for step in f:
        do_step(step.rstrip())
    print count()
