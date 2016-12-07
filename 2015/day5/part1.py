#! /usr/bin/python

def is_nice(word):
    vowels = [ c for c in word if c in [ 'a', 'e', 'i', 'o', 'u' ]]
    if len(vowels) < 3:
        return False
    repeats = [ word[i] for i in range(0, len(word) - 1) if word[i] == word[i+1] ]
    if len(repeats) == 0:
        return False
    for bw in [ "ab", "cd", "pq", "xy" ]:
        if bw in word:
            return False

    return True

for test in [ ('ugknbfddgicrmopn', True), ('aaa', True), ('jchzalrnumimnmhp', False), ('haegwjzuvuyypxyu', False), ('dvszwmarrgswjxmb', False) ]:
    assert(is_nice(test[0]) == test[1])

with open('input.txt', 'r') as f:
    print "nice count: %d" % len( [ w.rstrip() for w in f.readlines() if is_nice(w.rstrip()) ])
