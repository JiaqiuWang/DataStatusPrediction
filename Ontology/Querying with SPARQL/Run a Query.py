import rdflib


g = rdflib.Graph()

# ... and some triples to a somehow ...
g.parse("http://bigasterisk.com/foaf.rdf")


qres = g.query(
    """SELECT DISTINCT ?aname ?bname
       WHERE {
          ?a foaf:knows ?b.
          ?a foaf:name ?aname.
          ?b foaf:name ?bname.
       }""")

for row in qres:
    print("%s knows %s" % row)










