

from rdflib import Graph

g = Graph()
g.parse("musicontology.rdfs", format='application/rdf+xml')
# g.add()
print("len-g:", len(g))

for items in g:
    print("(%s, %s, %s)" % items)






















