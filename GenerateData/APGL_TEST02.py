"""
Name: Generate Graph:
Author: Jia_qiu Wang(王佳秋)
Data: December, 2016
function:
"""

import numpy

from apgl.graph.VertexList import VertexList
from apgl.graph.SparseGraph import SparseGraph

numVertex = 5
numFeature = 2  # vector labels of size 2
graph = SparseGraph(VertexList(numVertex, numFeature))

# Add some edges to the graph(method 1)
# Vertices are indexed starting from 0
# graph[0, 1] = 0.1
# graph[1, 2] = 1

# Add some edges to the graph(method 2 is identity to method 1)
edges = numpy.array([[0, 1], [1, 2]], numpy.int)
edgeValues = numpy.array([0.1, 1])
graph.addEdges(edges, edgeValues)

# Set the label of 0th vertex to [2, 3]
graph.setVertex(0, numpy.array([2, 3]))

# Displays edge weights
print(graph[1, 2])
print(graph[1, 3])

