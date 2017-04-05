from rdflib import Graph
from rdflib import URIRef

graph = Graph('Sleepycat')

# first time create the store:
graph.open('/', create=True)
#
# work with the graph:
a = URIRef("ASDF")
b = URIRef("ASsdDF")
c = URIRef("SDF")
graph.add((a, b, c))
#
graph.serialize('model2.rdf', format='n3')  # 默认以'xml'格式存储
# when done!
graph.close()
