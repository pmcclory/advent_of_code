#! /usr/bin/python

import re

def has_abba(word):
    return len( [ word[i:i+4] for i in range(0, len(word) - 3) if word[i] == word[i+3] and word[i+1] == word[i+2] and word[i] != word[i+1] ]) > 0

def support_tls(addr):
    regex = re.compile('.*\[([a-z]+)\].*')
    while True:
        m = regex.match(addr)
        if not m:
            break
        inner = m.groups()[0]
        if has_abba(inner):
            return False
        addr = addr.replace(m.groups()[0], '')
    return has_abba(addr)

print support_tls('abba[mnop]qrst')
print support_tls('abcd[bddb]xyyx')
print support_tls('aaaa[qwer]tyui')
print support_tls('ioxxoj[asdfgh]zxcvbn')

with open('input.txt', 'r') as f:
    print sum((support_tls(line.rstrip()) for line in f))
