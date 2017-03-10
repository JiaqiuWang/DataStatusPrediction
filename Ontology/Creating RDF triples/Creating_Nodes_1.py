"""
Nodes can be created by the constructors of the node classes:
"""

from rdflib import URIRef, BNode, Literal
from rdflib import Namespace

bob = URIRef("http://example.org/people/Bob")
linda = BNode()  # a GUID is generated GUID:全局统一标识符

name = Literal('Bob')  # passing a string
age = Literal(24)  # passing a python int
height = Literal(76.5)  # passing a python float

n = Namespace("http://example.org/people/")  # rdflib.term.URIRef(u'http://example.org/people/bob')

print(n.bob, n.eve)

temp = URIRef("http://example.org/people/Bob")
print("temp:", temp)

from rdflib.namespace import RDF, FOAF

print("RDF.type:", RDF.type)  # rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type')

print("FOAF.knows:", FOAF.knows)  # URIRef(u'http://xmlns.com/foaf/0.1/knows')





















