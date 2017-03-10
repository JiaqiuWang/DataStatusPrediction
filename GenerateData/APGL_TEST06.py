"""
Name: Generate Graph:
Author: Jia_qiu Wang(王佳秋)
Data: December, 2016
function:
"""

from apgl.graph.DenseGraph import DenseGraph
from apgl.graph.GeneralVertexList import GeneralVertexList
from apgl.generator.ErdosRenyiGenerator import *

numVertices = 20
graph = DenseGraph(GeneralVertexList(numVertices))
p = 0.2
generator = ErdosRenyiGenerator(p)
graph = generator.generate(graph)


