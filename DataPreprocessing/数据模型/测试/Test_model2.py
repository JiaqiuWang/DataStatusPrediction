
import rdflib

s = rdflib.URIRef('http://www.example.org/牛膝')
p = rdflib.URIRef('http://www.example.org/功效属性')
o = rdflib.URIRef('http://www.example.org/活血')

s1 = rdflib.URIRef('http://www.example.org/user1')
p1 = rdflib.URIRef('http://www.example.org/commit')
o1 = rdflib.URIRef('http://www.example.org/coding')

s2 = rdflib.URIRef('http://www.example.org/user2')
p2 = rdflib.URIRef('http://www.example.org/pull_request')
o2 = rdflib.URIRef('http://www.example.org/poke')

g1 = rdflib.Graph()
g1.add((s, p, o))
g1.add((s1, p1, o1))
g1.add((s2, p2, o2))

g1.serialize('model2.rdf')  # 默认以'xml'格式存储

g1.close()


















