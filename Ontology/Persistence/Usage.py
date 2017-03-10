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
# when done!
graph.close()
