
from rdflib.namespace import FOAF
from rdflib import Graph
import pprint

g = Graph()
g.parse("dbpedia_2016-04.nt", format='nt')
print("len-g:", len(g))
# for stmt in g:
#     pprint.pprint(stmt)

for s, p, o in g:
    print((s, p, o))

for s, _, n in g.triples((None, FOAF['member_name'], None)):
    g.add((s, FOAF['name'], n))
