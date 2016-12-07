#! /usr/bin/python

# a more elegant solution using zip

from collections import Counter

test = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""

import test_input
#test = test_input.test
lines = test.splitlines()

z = zip(*lines)
#part 1
#word = [ Counter(col).most_common()[0][0] for col in z ]
#part 2
word = [ Counter(col).most_common()[-1][0] for col in z ]
print ''.join(word)

