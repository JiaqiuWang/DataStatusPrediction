"""
Name: Generate Graph;
description：It is a labeled, undirected and connected graphs. The data sets generated
can be used for the performance evaluation of frequent subgraph mining algorithms and
graph query processing algorithms.
Author: Jia_qiu Wang(王佳秋)
Date: December, 2016
function:
"""
import random
import pymongo


class GenerateGraph:

    # 全局变量
    varString = "admin你好！"
    count_id = 1
    # 类公有变量；IP地址或者写127.0.0.1
    client = pymongo.MongoClient("192.168.1.228", 27017)

# ----------------------------------------------------------------------------------------------#

    # 构造函数
    def __init__(self, uid, count_graph, count_vertex, db, collection):
        self.uid = uid
        self.count_graph = count_graph
        self.count_vertex = count_vertex
        self.db = db
        self.collection = collection

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")

# ----------------------------------------------------------------------------------------------#

    """最后的输入数据库的text
    每次生成新图_id从0开始计数"""
    def generate_text(self):
        # 先删除数据库中的数据集合（表）
        self.drop_collection(self.collection)
        # 循环生成图数据
        for i in range(1, self.count_graph + 1):
            dict_edges = self.get_edges_property()  # 字典数据结构
            text = {"_id": self.count_id, "uid": self.uid, "vertex": self.get_vertices_property(),
                    "edges": dict_edges}
            self.count_id += 1
            print("text:",  text)
            # 插入数据库
            self.insert_database_time_flow(text)

# ----------------------------------------------------------------------------------------------#

    """随机生成节点和对应的属性"""
    def get_edges_property(self):
        dict_edges = {}
        # 1~20 循环迭代，20个节点
        if self.count_vertex > 5:
            # num是随机边的个数, n是结点个数   4n < num < n*(n-1)/2
            num = random.randint(4*self.count_vertex, self.count_vertex*(self.count_vertex-1)/2)
            count = 0  # 计数器
            list_var = []

            for i in range(1, self.count_vertex + 1):
                list_var.append(i)
            while count < num:
                slice_var = random.sample(list_var, 2)
                # 如果后面的结点比前面的结点，把数字小的几点放到前面
                if slice_var[0] > slice_var[1]:
                    t = slice_var[1]
                    slice_var[1] = slice_var[0]
                    slice_var[0] = t
                list_aft = []
                # 将slice放入到新的数据结构里面：pre:vi, aft:[v2, v5,...vn]
                if slice_var[0] not in dict_edges.keys():
                    # 新存入字典
                    list_aft.append(slice_var[1])
                    dict_edges.setdefault(slice_var[0], list_aft)
                else:
                    # 判断新产生的边(2, 5)的aft是不是已经存在aft队列中了，如果存在则重新执行for循环：continue
                    if slice_var[1] in dict_edges[slice_var[0]]:
                        continue
                    else:
                        # 存入老字典的键值
                        dict_edges[slice_var[0]].append(slice_var[1])
                        dict_edges[slice_var[0]].sort()
                # print("slice:", slice_var)
                count += 1
                # print("dict_edges:", dict_edges)
            # print("count:", count, " num:", num)
        else:
            print("The number of Vertex is too small!")
            exit()  # 退出所有程序
        # 转换成key为字符串的形式：
        transform_dict = {}
        for i in dict_edges.keys():
            transform_dict.setdefault(str(i), dict_edges[i])
        dict_edges = transform_dict.copy()
        return dict_edges

# ----------------------------------------------------------------------------------------------#

    """随机生成边和对应的属性"""
    def get_vertices_property(self):
        list_vertices = []
        # 1~15 循环迭代，15个节点
        for i in range(1, self.count_vertex + 1):
            pl = 5*i-random.randint(0, 4)  # property label
            dict_vertex = {"vertex": i, "pl": pl}
            # print("dict_vertex:", dict_vertex)
            list_vertices.append(dict_vertex)
        # print("list_vertices:", list_vertices)
        return list_vertices

# ----------------------------------------------------------------------------------------------#

    """插入数据库"""
    def insert_database_time_flow(self, graph_i):
        db = self.client.get_database(self.db)
        collection = db.get_collection(self.collection)
        collection.insert(graph_i)

# ----------------------------------------------------------------------------------------------#

    """删除数据库中的集合，参数：collection名字"""
    def drop_collection(self, collection_name):
        db = self.client.get_database(self.db)
        collection = db.get_collection(collection_name)
        collection.drop()

# ----------------------------------------------------------------------------------------------#


def main_operation():
    """Part1: initialize parameters"""
    uid = "u1"  # 用户标识
    count_graph = 30000  # 需要生成图的个数
    count_vertex = 15  # 节点个数，代表了不同的类 n= 21 - 1
    db_name = "yanglao"  # 数据库名字
    collection_name = "graphSets"  # 集合名字
    # initialize constructor 初始化构造函数
    gr = GenerateGraph(uid, count_graph, count_vertex, db_name, collection_name)
    gr.generate_text()


if __name__ == '__main__':
    main_operation()



