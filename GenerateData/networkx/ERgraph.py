"""
Name: Generate Graph: ER随即图
Author: Jia_qiu Wang(王佳秋)
Data: December, 2016
function:
"""

import networkx as nx
import matplotlib.pyplot as plt

# erdos renyi graph
# generate a graph which has n = 20 nodes, probability p = 0.2
ER = nx.random_graphs.erdos_renyi_graph(20, 0.2)
# the shell layout
pos = nx.shell_layout(ER)
nx.draw(ER, pos, with_labels=False, node_size=30)
plt.show()




