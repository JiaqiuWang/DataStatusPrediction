"""
Name: Generate Graph: regular graph
Author: Jia_qiu Wang(王佳秋)
Data: December, 2016
function:
"""

import networkx as nx
import matplotlib.pyplot as plt

red = nx.random_lobster(20, 0.9, 0.9)
pos = nx.shell_layout(red)
nx.draw(red, pos, with_labels=False, node_size=30)
plt.show()










