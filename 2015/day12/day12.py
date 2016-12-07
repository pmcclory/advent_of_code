#! /usr/bin/python

def sum_doc(doc):
    if isinstance(doc, list):
        return sum((sum_doc(x) for x in doc))
    if isinstance(doc, dict):
        #it wasn't specified if we need to count numbers
        # as keys so I'm assuming yes
        return sum((sum_doc(x) + sum_doc(doc[x]) for x in doc))
    elif isinstance(doc, int):
        return doc
    else:
        return 0

print sum_doc([1,2,3])
print sum_doc({"a":2,"b":4})
print sum_doc([[[3]]])
print sum_doc({"a":{"b":4},"c":-1})
print sum_doc([-1,{"a":1}])
print sum_doc({"a":[-1,1]})
print sum_doc([])
print sum_doc({})
print sum_doc([1,2,3,[4,5]])

with open('input.txt', 'r') as f:
    import json
    doc = json.load(f)
    print sum_doc(doc)
