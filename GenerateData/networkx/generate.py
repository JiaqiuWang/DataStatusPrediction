"""
Name: Generate Graph: regular graph
Author: Jia_qiu Wang(王佳秋)
Data: December, 2016
function:
"""

import networkx as nx
import matplotlib.pyplot as plt

# regular graph
# generate a regular graph which has 20 nodes has 3 neighbour nodes
RG = nx.random_graphs.random_regular_graph(3, 20)
# the spectral layout
pos = nx.spectral_layout(RG)
# Draw the regular graph
nx.draw(RG, pos, with_labels=False, node_sieze=30)
plt.show()



