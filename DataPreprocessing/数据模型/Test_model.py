import rdflib

graph = rdflib.Graph()


s = rdflib.URIRef('牛膝')
p = rdflib.URIRef('功效属性')
o = rdflib.URIRef('活血')

s1 = rdflib.URIRef('user1')
p1 = rdflib.URIRef('commit')
o1 = rdflib.URIRef('sdong')

s2 = rdflib.URIRef('user2')
p2 = rdflib.URIRef('start')
o2 = rdflib.URIRef('ongiw')


graph.add((s, p, o))
graph.add((s1, p1, o1))
graph.add((s2, p2, o2))

# 以n3格式存储
graph.serialize('model.rdf', format='n3')












