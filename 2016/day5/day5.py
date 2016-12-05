#! /usr/bin/python

import hashlib
#hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()

def gen_passwd(door_id):
    indx = 0
    passwd = ''
    while len(passwd) != 8:
        hsh = hashlib.md5("%s%d" % (door_id, indx)).hexdigest()
        if hsh[0:5] == "00000":
            passwd += hsh[5]
            print passwd
        indx += 1
    return passwd

#print "password is: %s" % gen_passwd('abc')
print "password is: %s" % gen_passwd('ffykfhsq')

