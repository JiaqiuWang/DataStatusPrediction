"""
Name: Generate Graph:
Author: Jia_qiu Wang(王佳秋)
Data: December, 2016
function:
"""

from apgl.graph.GeneralVertexList import GeneralVertexList
from apgl.graph.SparseGraph import SparseGraph

numVertices = 10
graph = SparseGraph(GeneralVertexList(numVertices))

graph[0, 1] = 1
graph[0, 2] = 1

P = graph.floydWarshall()
print("geodesicDistance:", graph.geodesicDistance(P=P))
print("harmonicGeodesicDistance:", graph.harmonicGeodesicDistance(P=P))

