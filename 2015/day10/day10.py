#! /usr/bin/python

import math

"""
Hey a generator!
"""
def get_next_digit(x):
    while x > 0:
        yield (x / 10 ** int(math.log(x, 10)))
        x = x % (10 ** int(math.log(x, 10)))

def look_say(x):
    stack = []
    result = 0

    def add_to_result(result, stack):

        result *= 100
        result += len(stack) * 10
        result += stack[-1]

        return result

    for d in get_next_digit(x):
        if len(stack) == 0:
            stack.append(d)
        elif stack[-1] == d:
            stack.append(d)
        else:
            result = add_to_result(result, stack)
            stack = [d]
    result = add_to_result(result, stack)
    return result

print look_say(1)
print look_say(11)
print look_say(21)
print look_say(1211)
print look_say(111221)
assert(look_say(3113322113) == 132123222113)

def get_length(x):
    return math.log(x, 10) + 1

import look_see_table
def get_length_with_cosmo_table(x, iterations):
    if x not in look_see_table.values_to_entry:
        raise Exception
    entries = [ look_see_table.values_to_entry[x] ]
    for i in range(0, iterations):
        next_gen = []
        for entry in entries:
            next_gen += look_see_table.evolution_map[entry]
        entries = next_gen
        length = 0
        for e in entries:
            length += look_see_table.entry_lengths[e]
        print "%d: %d" % (i, length)

x = 3113322113
get_length_with_cosmo_table(x, 40)
get_length_with_cosmo_table(x, 50)
