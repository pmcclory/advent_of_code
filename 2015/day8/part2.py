#! /usr/bin/python

def encoded_length(word):
    length = 0
    for c in word:
        if c == '"' or c == '\\':
            length += 2
        else:
            length += 1
    return (length + 2, len(word))

print encoded_length('""')
print encoded_length('"abc"')
print encoded_length('"aaa\\"aaa"')
print encoded_length('"\\x27"')

with open('input.txt', 'r') as f:
    results = []
    for line in f:
        results.append(encoded_length(line.rstrip()))
    total_chars = sum([ x[0] for x in results ])
    orig_chars =  sum([ x[1] for x in results ])
    print total_chars - orig_chars
