#! /usr/bin/python

import re
import copy
import string

"""
class BaseComponent(object):
    def __init__(self, name, *args):
        self.name = name
        self.set_input(*args)

    def __repr__(self):
        return "%s: %d" % (self.name, self.signal)

    def __and__(self, other):
        return self.signal & other.signal

    def __or__(self, other):
        return self.signal | other.signal

    def __invert__(self):
        return (~ self.signal & 65535)

    def __lshift__(self, count):
        return (self.signal << count & 65535)

    def __rshift__(self, count):
        return (self.signal >> count & 65535)

class Signal(BaseComponent):

    def set_input(self, value):
        self.signal = value

class AndGate(BaseComponent):
    def set_input(self, signal1, signal2):
        self.input1 = signal1
        self.input2 = signal2

    @property
    def signal(self):
        return self.input1.signal & self.input2.signal

class LeftShiftGate(BaseComponent):
    def set_input(self, input_signal, shift_size):
        self.input_signal = input_signal
        self.shift_size = shift_size

    @property
    def signal(self):
        return self.input_signal << self.shift_size

class RightShiftGate(BaseComponent):
    def set_input(self, input_signal, shift_size):
        self.input_signal = input_signal
        self.shift_size = shift_size

    @property
    def signal(self):
        return self.input_signal >> self.shift_size

class NotGate(BaseComponent):
    def set_input(self, input_signal):
        self.input_signal = input_signal

    @property
    def signal(self):
        return ~ self.input_signal

class OrGate(BaseComponent):
    def set_input(self, input_signal1, input_signal2):
        self.input_signal1 = input_signal1
        self.input_signal2 = input_signal2

    @property
    def signal(self):
        return self.input_signal1 | self.input_signal2
"""

def is_signal(x):
    for c in x:
        if c not in string.digits:
            return False
    return True

def parse_instructions(instr):
    i = 0
    components = {}
    last_count = len(components)
    while instr:
        inp,out = instr[i].split("->")
        out = out.strip()
        if "AND" in inp or "OR" in inp:
            regex = re.compile('(.*) (AND|OR) (.*) ')
            x,op,y = regex.match(inp).groups()
            in_component = None
            out_component = None
            if is_signal(x):
                in_component = int(x)
            elif x in components:
                in_component = components[x]
            if is_signal(y):
                out_component = int(y)
            elif y in components:
                out_component = components[y]
            if in_component != None and out_component != None:
                if op == "AND":
                    components[out] = (in_component & out_component) & 65535
                else:
                    components[out] = (in_component | out_component) & 65535
        elif "LSHIFT" in inp or "RSHIFT" in inp:
            regex = re.compile('(.*) ([L,R]SHIFT) (.*) ')
            x,op,shift = regex.match(inp).groups()
            in_component = None
            if is_signal(x):
                in_component = int(x)
            elif x in components:
                in_component = components[x]
            if x == 'he':
                print "he shift: " + instr[i].rstrip()
            else:
                print "shift: %s (%s)" % (x, instr[i].rstrip())

            if in_component != None:
                print "doing shift of %s" % out
                if op == "LSHIFT":
                    components[out] = (in_component << int(shift)) & 65535
                else:
                    components[out] = (in_component >> int(shift)) & 65535
        elif "NOT" in inp:
            x = inp.split("NOT ")[1].strip()
            in_component = None
            if is_signal(x):
                in_component = x
            elif x in components:
                in_component = components[x]
            if in_component != None:
                components[out] = (~ in_component & 65535)
        else:
            inp = inp.strip()
            if is_signal(inp):
                components[out] = int(inp) 
            elif inp in components:
                components[out] = components[inp]

        if out in components:
            print "added %s to components, resetting last_count to %d" % (out, len(components))
            print components
            del instr[i]
            i = 0
            last_count = len(components)
        else:
            print "didn't find %s (%d)" % (out, i)
            i = (i + 1) % len(instr)
#            if i == len(instr) - 1:
#                if last_count == len(components):
#                    print "DEADLOCK"
#                    print components
#                    for l in sorted(instr):
#                        print l.strip()
#                    exit(-1)

    return components

instructions = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""

components = parse_instructions(instructions.split("\n"))
#for c in sorted(components.keys()):
#    print "%s: %s" % (c, components[c])

with open('input.txt', 'r') as f:
    lines = f.readlines()
    regex = re.compile("[0-9]+ (-> b)$")
    for i in range(0, len(lines)):
        # hack
        m = regex.match(lines[i].strip())
        if m:
            prefix = m.groups()[0]
            lines[i] = "%d -> b" % (3176)

    components = parse_instructions(lines)
    print components['a']
