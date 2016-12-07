#! /usr/bin/python

import re

def get_abas(word):
    return [ word[i:i+3] for i in range(0, len(word) - 2) if word[i] == word[i + 2] and word[i] != word[i + 1] ]

def support_ssl(addr):
    regex = re.compile('.*\[([a-z]+)\].*')
    hypernets = []
    while True:
        m = regex.match(addr)
        if not m:
            break
        inner = m.groups()[0]
        hypernets.append(inner)
        addr = addr.replace(inner, '')
    abas = get_abas(addr)
    for a in abas:
        bab = ''.join( [ a[1], a[0], a[1] ] )
        for h in hypernets:
            if bab in h:
                return True
    return False
   
print support_ssl('aba[bab]xyz')
print support_ssl('xyx[xyx]xyx')
print support_ssl('aaa[kek]eke')
print support_ssl('zazbz[bzb]cdb')

with open('input.txt', 'r') as f:
    print sum((support_ssl(line.rstrip()) for line in f))
