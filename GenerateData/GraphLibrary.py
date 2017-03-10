"""
Name: Generate Graph:
Author: Jia_qiu Wang(王佳秋)
Data: December, 2016
function:
"""

from apgl.graph import GeneralVertexList, SparseGraph
import numpy


numVertices = 5  # 顶点个数
graph = SparseGraph(numVertices)  # 具有5个顶点个数的图数据结构
graph[0, 1] = 1
graph[0, 2] = 3
graph[1, 2] = 0.1
graph[3, 4] = 2
graph.setVertex(0, "abc")
graph.setVertex(1, 123)
print(graph.findConnectedComponents())  # 输出联通分量

print(graph.getWeightMatrix())  # 输出图的邻接矩阵

# print(graph.degreeDistribution())

print(graph.neighbours(0))

print(graph)
