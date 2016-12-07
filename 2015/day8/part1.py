#! /usr/bin/python

def length(x):
    code_len = len(x)
    # starting / ending quotes don't start
    memory_len = len(x) - 2
    i = 1
    count = 0
    while i < len(x) - 1:
        count += 1
        if x[i] == '\\':
            if x[i + 1] == 'x':
                i += 4
            elif x[i + 1] == '\\':
                i += 2
            elif x[i + 1] == '"':
                i += 2
        else:
            i += 1
    return (code_len, count)

test = [ '""', '"abc"', '"aaa\\"aaa"', '"\\x27"' ]
result = []
for t in test:
    result.append(length(t))

code_len = sum([ x[0] for x in result ])
mem_len = sum([ x[1] for x in result ])
print code_len - mem_len

with open('input.txt', 'r') as f:
    result = []
    for line in f:
        result.append(length(line.rstrip()))
    code_len = sum([ x[0] for x in result ])
    mem_len = sum([ x[1] for x in result ])
    print code_len - mem_len
