#! /usr/bin/python

from collections import Counter

def is_nice(word):
    result = True
    pairs = []
    for i in range(0, len(word) - 1):
        s = word[i:i+2]
        if pairs:
            #check for overlap
            if pairs[-1][0] == s and i == pairs[-1][1][1]:
                continue
            else:
                pairs += [ (word[i:i+2], (i,i+1)) ]
        else:
            pairs += [ (word[i:i+2], (i, i+1)) ]
    counter = Counter([ p[0] for p in pairs ])
    if counter.most_common()[0][1] == 1:
        result = False

    repeats = [ word[i] for i in range(0, len(word) - 2) if word[i] == word[i+2] ]
    if len(repeats) == 0:
        result = False
    return result

for test in [ ('qjhvhtzxzqqjkmpb', True), ('xxyxx', True), ('uurcxstgmygtbstg', False), ('ieodomkazucvgmuy', False) ]:
    assert(is_nice(test[0]) == test[1])

with open('input.txt', 'r') as f:
    print "nice count: %d" % len( [ w.rstrip() for w in f.readlines() if is_nice(w.rstrip()) ])
