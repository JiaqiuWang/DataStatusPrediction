"""
Name: Generate Graph: add Node and attributes
Author: Jia_qiu Wang(王佳秋)
Data: December, 2016
function:
"""

import networkx as nx
g = nx.Graph()
h = nx.Graph(g)  # 可以在构建Graph对象时指定值来构造一个新的Graph对象
f = nx.Graph([(1, 2), (2, 3), (1, 3)])

# 1.graph对象添加节点node
g.add_node(1)
g.add_nodes_from([(4, 5), (7, 9)])  # 添加一个节点列表
w = nx.path_graph(10)
# list_var = ["1", "sga", 654]
g.add_nodes_from(w)  # 添加一个能够迭代的集合（例如：list, set, graph, file等），这样g中包含了w中的元素
g.add_node(w)  # 这是讲w作为一个node添加到g中
g.add_nodes_from("span")  # 将span拆分为一个字符数组，然后添加node

# 2.Node节点属性  Note:向node添加属性并不会想graph添加属性，
g.add_node(1, time="5pm")
g.add_nodes_from([3], time="2pm")
print(g.node[1])
g.node[1]["room"] = 714  # 添加结点属性
print(g.nodes(data=True))  # 输出所有节点的属性


