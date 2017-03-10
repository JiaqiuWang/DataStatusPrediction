"""
Name: Generate Graph:
Author: Jia_qiu Wang(王佳秋)
Data: December, 2016
function:
"""

from apgl.graph.DictGraph import DictGraph
from apgl.graph.SparseGraph import SparseGraph
from apgl.graph.GeneralVertexList import GeneralVertexList

graph = DictGraph()
graph.addEdge("a", "b")
graph.addEdge("a", "c")
graph.addEdge("a", "d")

edgeIndices = graph.getAllEdgeIndices()
graph2 = SparseGraph(GeneralVertexList(graph.getNumVertices()))
graph2.addEdges(edgeIndices)

