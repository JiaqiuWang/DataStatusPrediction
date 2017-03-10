# reading graphs from the net is just as easy:

from rdflib import Graph
import pprint

g = Graph()
g.parse("http://bigasterisk.com/foaf.rdf")
print("len-g:", len(g))
for stmt in g:
    pprint.pprint(stmt)

