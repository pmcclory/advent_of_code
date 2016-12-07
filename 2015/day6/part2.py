#! /usr/bin/python

import re

matrix = None
OFF = 0
ON = 1
TOGGLE = 2

def init(state=OFF):
    global matrix
    matrix = []
    for i in range(0, 1000):
        matrix.append([])
        for j in range(0, 1000):
                matrix[i].append(0)

def count():
    global matrix
    c = 0
    for row in matrix:
        c += sum(row)
    return c

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
    for row in range(c1[1], c2[1] + 1):
        for col in range(c1[0], c2[0] + 1):
            if op == TOGGLE:
                matrix[row][col] += 2
            elif op == ON:
                matrix[row][col] += 1
            elif op == OFF:
                matrix[row][col] -= 1
            if matrix[row][col] < 0:
                matrix[row][col] = 0

init()
do_step("turn on 0,0 through 0,0")
print count()

init()
do_step("toggle 0,0 through 999,999")
print count()

with open('input.txt', 'r') as f:
    init(OFF)
    for step in f:
        do_step(step.rstrip())
    print count()
