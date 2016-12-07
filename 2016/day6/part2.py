#! /usr/bin/python

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
lines = test_input.test.splitlines()
print lines[0]
column_count = len(lines[0])

chars = []
for i in range(column_count):
    chars.append([])

print column_count

for line in test_input.test.splitlines():
    print len(line)
    chars.append([])
    for i in range(len(line)):
        chars[i].append(line[i])

word = []
for i in range(0, column_count):
    counter = Counter(chars[i])
    print counter.most_common()
    word.append(counter.most_common()[-1][0])

print ''.join(word)
