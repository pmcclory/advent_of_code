#! /usr/bin/python

from collections import defaultdict
import re

def gen_csum(counts):
    s = [ (counts[key], key) for key in counts ]
    s = sorted(s, key = lambda x: (x[0], -ord(x[1])))
    s.reverse()
    return ''.join([ s[i][1] for i in range(0, 5) ])

def real_room(room):
    room_re = re.compile("(.*)-([0-9]+)\[(.*)]$")
    m = room_re.match(room)
    if m == None:
        raise Exception("bad input")
    room_def = m.group(1)
    sector_num = int(m.group(2))
    csum = m.group(3)

    counts = defaultdict(int)
    for c in room_def:
        if c != '-':
            counts[c] += 1

    if gen_csum(counts) != csum:
        return (False, None, None)
    else:
        return (True, sector_num, room_def)

def decrypt(cipher_text, shift):
    clear = ''
    for c in cipher_text:
        if c == '-':
            clear += ' '
            continue
        if c.islower():
            a = ord(c) - 97
            a = (a + shift) % 26
            a += 97
        else:
            a = ord(c) - 65
            a = (a + shift) % 26
            a -= 65
        clear += chr(a)
    return clear

sector_sum = 0
rooms = [ 'aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]' ]
for r in rooms:
    real, sector, _ = real_room(r)
    if real:
        sector_sum += sector
assert(sector_sum == 1514)

sector_sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        real, sector, cipher_text = real_room(line.rstrip())
        if real:
            sector_sum += sector
            print "decrypted (%d): %s -> %s" % (sector, cipher_text, decrypt(cipher_text, sector))
print sector_sum
