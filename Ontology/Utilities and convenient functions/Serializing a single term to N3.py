from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import FOAF, NamespaceManager

person = URIRef('http://xmlns.com/foaf/0.1/Person')
print(person.n3())

g = Graph()
g.bind("foaf", FOAF)

print(person.n3(g.namespace_manager))

l = Literal(2)
print(l.n3())

print(l.n3(g.namespace_manager))


g.parse(data='<urn:a> <urn:p> <urn:b>.', format='n3')
for s, p, o in g:
    print((s, p, o))
