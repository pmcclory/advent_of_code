#! /usr/bin/python

import hashlib

#for part1/part2
ZERO_COUNT = 6

def get_index(secret):
    indx = 0
    while True:
        hsh = hashlib.md5("%s%d" % (secret, indx)).hexdigest()
        if hsh[0:ZERO_COUNT] == '0' * ZERO_COUNT:
            print "hsh = %s at indx %d" % (hsh, indx)
            return indx
        indx += 1

if ZERO_COUNT == 5:
    tests = [ ('abcdef', 609043), ('pqrstuv', 1048970) ]
    for t in tests:
        assert(get_index(t[0]) == t[1])

get_index('bgvyzdsv')
