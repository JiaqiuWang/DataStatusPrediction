"""
利用serialize将数据以一定规范存储到硬盘中
"""

import rdflib

graph = rdflib.Graph()

# work with the graph:
s = rdflib.URIRef('牛膝')
p = rdflib.URIRef('功效属性')
o = rdflib.URIRef("活血")

graph.add((s, p, o))

# 以n3的格式存储
graph.serialize('zhongyaoyao.rdf', format='n3')

s = rdflib.URIRef("http://www.example.org/牛膝")
p = rdflib.URIRef("http://www.example.org/功效属性")
o = rdflib.URIRef("http://www.example.org/活血")

g1 = rdflib.Graph()
g1.add((s, p, o))
g1.serialize('zhongyaoyao1.rdf')  # 默认以'xml'格式存储

g2 = rdflib.Graph()
g2.parse('zhongyaoyao1.rdf', format='xml')  # 解析rdf文件时，需要指定格式
subject = g2.subjects(p, o)
for i in subject:
    print("i:", i)




