"""
Name: Generate Graph:
Author: Jia_qiu Wang(王佳秋)
Data: December, 2016
function:
"""

import numpy
import scipy.sparse as sps
from apgl.graph.GeneralVertexList import GeneralVertexList
from apgl.graph.SparseGraph import SparseGraph

numVertices = 10
vList = GeneralVertexList(numVertices)
wght = sps.csc_matrix(numVertices, numVertices)
graph = SparseGraph(vList, W=wght, undirected=False)

graph[0, 1] = 1
graph[0, 2] = 1
graph.setVertex(0, "abc")
graph.setVertex(1, 123)

print(graph)
