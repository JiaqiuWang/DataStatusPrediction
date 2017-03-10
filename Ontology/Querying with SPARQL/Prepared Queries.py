import rdflib.plugins.sparql
from rdflib.namespace import FOAF


# g = rdflib.Graph()
#
# # ... and some triples to a somehow ...
# g.parse("http://bigasterisk.com/foaf.rdf")

q = rdflib.plugins.sparql.prepareQuery(
    'SELECT ?s WHERE { ?person foaf:knows ?s .}',
    initNs={"foaf": FOAF})

g = rdflib.Graph()
g.load("foaf.rdf")

tim = rdflib.URIRef("http://www.w3.org/People/Berners-Lee/card#i")

for row in g.query(q, initBindings={'person': tim}):
    print("row:", row)







