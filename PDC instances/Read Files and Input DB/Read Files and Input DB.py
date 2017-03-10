"""
1.读取applog文本记录到数据库中
"""
import pymongo
import codecs


class FindDifferentEdges:

    # 类公有变量；IP地址或者写127.0.0.1
    client = pymongo.MongoClient("192.168.1.228", 27017)
    # 字典数据结构，存放基本数据结构的
    dict_vertex = {}
    # 用于排序的队列
    list_after = []
    # 开始结点
    start_node = 0
    # 存放两个图异构的结构（队列嵌套数组数据结构）
    list_diff = []

    # 构造函数
    def __init__(self, db, col):
        self.db_name = db
        self.collection_name = col

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")
        self.client.close()

    # 读取文本中每行的节点队
    def read_lines_from_file(self, filename):
        f = codecs.open(filename, "r+", "utf-8")  # 读取中文
        line = f.readline()  # 读取一行
        # line.replace('\r\n', ' ')
        line.strip()  # 删除字符串左右的空格
        # 先删除数据库中的数据集合（表）
        self.drop_collection()
        while line:
            # print("字符串长度：", len(line))
            line = line.strip('\r\n')  # 去掉每个字符的'\r\n'
            # print(line, end=" ")
            list_line = line.split('\t', 1)
            # print(list_line)
            self.transform_ds(list_line)
            line = f.readline()
        f.close()
        print(self.dict_vertex)

    # 读取文本中每行的节点队
    def read_lines_from_file_g2(self, filename):
        f = codecs.open(filename, "r+", "utf-8")  # 读取中文
        line = f.readline()  # 读取一行
        # line.replace('\r\n', ' ')
        line.strip()  # 删除字符串左右的空格
        while line:
            # print("字符串长度：", len(line))
            line = line.strip('\r\n')  # 去掉每个字符的'\r\n'
            # print(line, end=" ")
            list_line = line.split('\t', 1)
            print(list_line)
            self.transform_ds_g2(list_line)
            line = f.readline()
        f.close()
        # print(self.dict_vertex)
        print("Find all different structure：", self.list_diff)

    # 将每一行队列转换新数据结构后；写入数据库中
    def transform_ds(self, list_line):
        f_el = list_line[0]
        sec_el = list_line[1]
        print("first ele:", f_el, "; second ele:", sec_el)
        if f_el not in self.dict_vertex.keys():
            if self.start_node is not 0:
                # 存入数据库，start_node != 0
                text = {"_id": self.start_node, "back": self.list_after}
                self.insert_database_time_flow(text)
            self.dict_vertex.clear()
            self.list_after.clear()
            self.list_after.append(sec_el)
            self.dict_vertex.setdefault(f_el, self.list_after)
            self.start_node = f_el
            print(self.dict_vertex)
        else:
            self.list_after.append(sec_el)
            self.dict_vertex.setdefault(f_el, self.list_after)
            # print(self.dict_vertex)

    # 将每一行队列转换新数据结构后；写入数据库中
    def transform_ds_g2(self, list_line):
        f_el = list_line[0]
        sec_el = list_line[1]
        print("first ele:", f_el, "; second ele:", sec_el)
        # 查找数据库中是否有初始节点，查询数据库游标
        db = self.client.get_database(self.db_name)
        collection = db.get_collection(self.collection_name)
        var_cursor = collection.find_one({"_id": f_el})  # 查找对应的初始结点
        if var_cursor:
            if list_line[1] not in var_cursor.get("back"):
                self.list_diff.append(list_line)
        else:
            self.list_diff.append(list_line)

    # 插入数据流数据库
    def insert_database_time_flow(self, data):
        db = self.client.get_database(self.db_name)
        collection = db.get_collection(self.collection_name)
        collection.insert(data)

    # 删除数据库中的集合
    def drop_collection(self):
        db = self.client.get_database(self.db_name)
        collection = db.get_collection(self.collection_name)
        collection.drop()


if __name__ == '__main__':
    db_name = "yanglao"
    collection_name = "graphPre"
    fde = FindDifferentEdges(db_name, collection_name)
    fde.read_lines_from_file("G1.txt")
    fde.read_lines_from_file_g2("G2.txt")  # 读取第二个图，然后比较不同
