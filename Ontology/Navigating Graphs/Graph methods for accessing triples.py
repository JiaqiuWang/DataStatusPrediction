from rdflib import ConjunctiveGraph, URIRef, RDFS, Literal
from rdflib.namespace import SKOS
from pprint import pprint

g = ConjunctiveGraph()
u = URIRef(u'http://example.com/foo')
g.add([u, RDFS.label, Literal('foo')])  # 给u添加标签
g.add([u, RDFS.label, Literal('bar')])  # 给u添加标签
pprint(sorted(g.preferredLabel(u)))

g.add([u, SKOS.prefLabel, Literal('bla')])
pprint(g.preferredLabel(u))

g.add([u, SKOS.prefLabel, Literal('blubb', lang='en')])
sorted(g.preferredLabel(u))

g.preferredLabel(u, lang='')

pprint(g.preferredLabel(u, lang='en'))






















