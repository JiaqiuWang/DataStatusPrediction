from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

g = Graph()
g.load("foaf.rdf")

for s, p, o in g.triples((None, RDF.type, FOAF.Person)):
    print("%s is a person" % s)

for s, p, o in g.triples((None, RDF.type, None)):
    print("%s is a %s" % (s, o))

bobgraph = Graph()

n = Namespace("http://example.org/people/")
bob = n.bob

bobgraph += g.triples((bob, None, None))

name = g.value(bob, FOAF.name)  # get any name of bob
mbox = g.value(predicate=FOAF.name, object=bob, any=False)





























