from rdflib import Graph
import pprint

g = Graph()
g.parse("demo.nt", format='nt')

print("len:", len(g))  # print 2

for stmt in g:
    pprint.pprint(stmt)


















