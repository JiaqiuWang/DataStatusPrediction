"""
Name: Generate Graph: add Edge and attributes
Author: Jia_qiu Wang(王佳秋)
Data: December, 2016
function:
"""

import networkx as nx
g = nx.Graph()
g.add_edge(1, 2)   # 添加一个1和2之间的edge
e = (2, 3)  # 定义个关系
g.add_edge(*e)  # 添加关系对象

g.add_edges_from([(1, 2), (2, 3)])  # 添加一个edge数组
h = nx.path_graph(10)
g.add_edges_from(h.edges())  # h.edges()返回的h的包含所有edge数组

# 拆除graph对象中的node和edge可以使用如下方法
# g.remove_node(1)
# g.remove_nodes_from()
# g.remove_edge()
# g.remove_edges_from()

# 删除所有的node和edge
# g.clear()

# 如果重复添加相同的node和edge， Networkx将会忽略那些重复的内容
g.add_nodes_from("span")
g.add_nodes_from("span")
g.add_nodes_from("s")

# 获取一个Graph对象中node和edge的数量
g.number_of_nodes()
g.number_of_edges()

# 获取一个Graph对象中的node数组或者edge数组
g.nodes()
g.edges()

g.neighbors(1)  # 获取与node为1相邻的node是节点
g.remove_edge(1, 2)  # 删除node1和node2之间的edge，自此node1和node2不在为相邻的node

# 设置边的属性
g.add_edge(1, 3)
g[1][1]["color"] = "blue"

