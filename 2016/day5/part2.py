#! /usr/bin/python

    import hashlib
    import string
    
    def gen_passwd(door_id):
        passwd = ''
        pass_d = {}
        indx = -1
    
        while len(pass_d) != 8:
            indx += 1
            hsh = hashlib.md5("%s%d" % (door_id, indx)).hexdigest()
            if hsh[0:5] == "00000":
                if hsh[5] not in string.digits:
                    continue
                pos = int(hsh[5])
                if pos > 7 or pos < 0:
                    continue
                if pos in pass_d:
                    continue
                pass_d[pos] = hsh[6]
    
        for i in range(0, 8):
            passwd += pass_d[i]
        return passwd

#print "password is: %s" % gen_passwd('abc')
print "password is: %s" % gen_passwd('ffykfhsq')

