"""
RDFLib graphs override __iter__()
in order to support iteration over the contained triples:
"""

from rdflib import Graph
from rdflib import Namespace
from rdflib import BNode, Literal
from rdflib.namespace import RDF, FOAF

g1 = Graph()
g2 = Graph()

n = Namespace("http://example.org/people/")
bob = n.bob
linda = BNode()
leiyu = BNode()
name = Literal('Bob')  # passing a string
age = Literal(24)  # passing a python int
height = Literal(76.5)  # passing a python float

g1.add((bob, RDF.type, FOAF.Person))
g1.add((bob, FOAF.name, name))
g1.add((bob, FOAF.know, linda))
g1.add((linda, RDF.type, FOAF.Person))
g1.add((linda, FOAF.name, Literal('Linda')))

g2.add((bob, RDF.type, FOAF.Person))
g2.add((bob, FOAF.name, name))
g2.add((bob, FOAF.know, leiyu))
g2.add((linda, RDF.type, FOAF.Person))
g2.add((linda, FOAF.name, Literal('Linda')))

# g3 = g1 + g2  # return new graph with union
# for s, p, o in g3:
#     print((s, p, o))

# g1 += g1  # in place union / addition
# for s, p, o in g1:
#     print((s, p, o))

# g4 = g2 - g1  # in place difference / subtraction
# for s, p, o in g4:
#     print((s, p, o))

# g5 = g1 & g2  # intersection (triples in both graphs)
# for s, p, o in g5:
#     print((s, p, o))

g6 = g1 ^ g2
for s, p, o in g6:
    print((s, p, o))


















