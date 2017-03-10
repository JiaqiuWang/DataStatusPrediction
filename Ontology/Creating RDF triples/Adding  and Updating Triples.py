"""
We already saw in Loading and saving RDF, how triples can be added with
with the parse() function.
Triples can also be added with the add() function:
Graph.add((s, p, o))[source]
Add a triple with self as context
"""

from rdflib import Graph
from rdflib import Namespace
from rdflib import BNode, Literal
from rdflib.namespace import RDF, FOAF

g = Graph()

n = Namespace("http://example.org/people/")
bob = n.bob
linda = BNode()
name = Literal('Bob')  # passing a string
age = Literal(24)  # passing a python int
height = Literal(76.5)  # passing a python float

g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, name))
g.add((bob, FOAF.know, linda))
g.add((linda, RDF.type, FOAF.Person))
g.add((linda, FOAF.name, Literal('Linda')))

print("turtle:", g.serialize(format='turtle'))

# For some properties, only one value per resource makes sense (i.e they are
# functional properties, or have max-cardinality of 1). The set() method is useful for this:
g.add((bob, FOAF.age, Literal(42)))
print("Bob is ", g.value(bob, FOAF.age))
# prints: Bob is 42
g.set((bob, FOAF.age, Literal(43)))  # replaces 42 set above
print("Bob is now ", g.value(bob, FOAF.age))

"""
Graph.remove((s, p, o))
Remove a triple from the graph

If the triple does not provide a context attribute,
removes the triple from all contexts.
"""
# g.remove((bob, None, None))

"""
Contains check
Graphs implement __contains__(), so you can
check if a triple is in a graph with triple in graph syntax:
"""
if (bob, RDF.type, FOAF.Person) in g:
    print("This graph knows that Bob is a person!")

"""
Note that this triple does not have to be completely bound:
"""
if (bob, None, None) in g:
   print("This graph contains triples about Bob!")




