import rdflib

g = rdflib.Graph()
result = g.parse("http://www.w3.org/People/Berners-Lee/card")

print("graph has %s statements." % len(g))
# prints graph has 79 statements.

for subj, pred, obj in g:
    if (subj, pred, obj) not in g:
        raise Exception("It better be!")

for i in result:
    print(i, "type-i:", type(i))

s = g.serialize(format='n3')
print(s, "type-s:", type(s))







