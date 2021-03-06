#! /usr/bin/python

def sum_doc(doc):
    if isinstance(doc, list):
        return sum((sum_doc(x) for x in doc))
    if isinstance(doc, dict):
        #it wasn't specified if we need to count numbers
        # as keys so I'm assuming yes
        if 'red' in doc.values():
            return 0
        else:
            return sum((sum_doc(x) + sum_doc(doc[x]) for x in doc))
    elif isinstance(doc, int):
        return doc
    else:
        return 0

print sum_doc([1,2,3])
print sum_doc([1,{"c":"red","b":2},3])

with open('input.txt', 'r') as f:
    import json
    doc = json.load(f)
    print sum_doc(doc)
