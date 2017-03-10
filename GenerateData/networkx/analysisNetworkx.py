"""
Name: Generate Graph: regular graph
Author: Jia_qiu Wang(王佳秋)
Data: December, 2016
function:
"""

import networkx as nx

g = nx.Graph()
g.add_edges_from([(1, 2), (1, 3)])
g.add_node("spam")
nx.connected_components(g)  # 将node有关联的显示一个数组中。返回的为一个数组
# sorted(nx.degree(g).values())


print(sorted(nx.degree(g).values()))
# 聚合
print(nx.clustering(g))
# 显示等级
print(nx.degree(g))

nx.draw(g)
nx.draw_random(g)
nx.draw_circular(g)




