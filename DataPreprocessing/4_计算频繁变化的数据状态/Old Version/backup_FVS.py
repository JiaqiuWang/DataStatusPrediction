
"""
选出不同数据模型版本之间时间间隔参数，然后计算临近2个数据模型变化
"""

import time
import pymongo


class PrefixSpanPos:

    # 类公有变量

    # 构造函数
    def __init__(self, ip, db, uid, min_sup_pos):
        self.ip = ip
        self.db_name = db
        self.uid = uid
        self.min_sup_pos = min_sup_pos
        # 全局变量-连接指定IP地址的数据库
        self.client = pymongo.MongoClient(self.ip, 27017)
        # 获取数据库
        self.db = self.client.get_database(self.db_name)  # 读取的数据库

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        self.client.close()
        print("!******************************************************!")
        print(class_name, "Destroy.")

# ---------------------------------------------------------------------------------------

    """
    获取自增1的_id,
    数据库：data_status
    文档：counters
    """
    def get_next_id(self, db_name):
        db = self.client.get_database(db_name)
        collection = db.get_collection("counters")
        _id_obj = collection.find_and_modify(query={'_id': self.collection_name},
                                             update={"$inc": {"no": +1}},
                                             upsert=False,
                                             full_response=True, new=True
                                             )
        # print("_id_obj:", _id_obj)
        _id = _id_obj.get("value").get("no")
        # print("_id:", _id)
        return _id

# ---------------------------------------------------------------------------------------

    """
        数据库操作
        """

    # 写入MongoDB数据库
    def insert_db(self, db_name, input_tuple):
        # 获取集合
        db = self.client.get_database(db_name)
        collection = db.get_collection(self.collection_name)
        # 添加单条记录到集合中
        collection.insert(input_tuple)

    # 批量插入数据
    def input_many_database(self, db_name, input_tuple):
        # 添加单条记录到集合中
        db = self.client.get_database(db_name)
        db.insert_many(input_tuple)

    # 查询所有collections
    def find_all(self, db_name, collection_name):
        # 查询所有
        db = self.client.get_database(db_name)
        collection = db.get_collection(collection_name)
        cursors = collection.find().sort([("timestamp", 1)])
        for data in cursors:
            print("type:", type(data), ", data:", data)
            # 更换_id
            new_id = self.get_next_id("data_status")
            data['_id'] = new_id
            print("new_data:", data)
        print("总记录数为：", cursors.count())
        self.client.close()
        return cursors.count()

    # 更新数据库
    def update_database(self, db_name, collection_name):
        db = self.client.get_database(db_name)
        collection = db.get_collection(collection_name)
        collection.update({"_id": 1, "pPer_id": "p2"}, {"$set": {"pName": "卫国"}})
        self.client.close()

    # 查找一个文档
    def find_one(self, db_name, collection_name):
        count = 0
        db = self.client.get_database(db_name)
        collection = db.get_collection(collection_name)
        for u in collection.find({"timestamp": '', "时间": ''}):
            print("符合条件的记录: ", u)
            print("timestamp:", u.get("timestamp"), ", type:", type(u.get("timestamp")))
            count += 1
            print()
            self.client.close()
        print("count:", count)

    # 删除一个数据
    def delete_one(self, db_name, collection_name):
        db = self.client.get_database(db_name)
        collection = db.get_collection(collection_name)
        for u in collection.find({"timestamp": '', "时间": ''}):
            print("符合条件的记录(_id): ", u.get("_id"))
            collection.remove({"_id": u.get("_id")})
            self.client.close()

    # 删除所有数据
    @classmethod
    def delete_one_collection(cls, col):
        col.remove()
        # self.client.close()
# ---------------------------------------------------------------------------------------

    """
    获取自增1的_id,
    数据库：data_status
    文档：counters
    """
    def iterate_cursor(self):
        # 获取集合
        collection = self.db.get_collection(self.uid)
        cursors = collection.find()
        count = 0
        list_varied = []  # 存放所有变化的pos字典的队列
        list_i = []  # 存放变化的每个文档，用户提取出service
        dict_type = {}  # 第一层type存储数据结构
        list_ft = []  # 第一层频繁的type,每个元素是字典结构
        dict_dep = {}  # 第二层department存储数据结构
        list_fd = []  # 第二层频繁的department存储结构
        dict_pot = {}  # 第三城position职位的存储结构
        """第一层支持度计数"""
        for i in cursors:
            if i.get("varied_pos"):
                print("i:", i)
                count += 1  # 计数器
                print("count:", count)
                dict_item = i.get("varied_pos")[0]
                list_varied.append(dict_item)
                list_i.append(i)
                print("type:", dict_item.get("type"))
                # 支持度计数，第一层 type种类:
                if dict_item.get("type") in dict_type:
                    dict_type[dict_item.get("type")] += 1
                else:
                    dict_type[dict_item.get("type")] = 1

        """第二层支持度计数"""
        print("First Layer-Type:", dict_type)
        count_sec = 0  # 第二层计数器
        for i in dict_type.keys():
            print(i, ":", dict_type.get(i)/count)
            if dict_type.get(i)/count >= self.min_sup_pos:
                list_ft.append(i)  # 频繁的type
                for j in list_varied:
                    if j.get("type") == i:
                        # 支持度计数，第2层 department单位:
                        count_sec += 1  # 计数器+1
                        if j.get("department") in dict_dep:
                            dict_dep[j.get("department")] += 1
                        else:
                            dict_dep[j.get("department")] = 1
        print("second Layer:", dict_dep)

        """第三层支持度计数"""
        count_thd = 0
        for k in dict_dep.keys():
            print(k, ":", dict_dep.get(k)/count_sec)
            if dict_dep.get(k)/count_sec >= self.min_sup_pos:
                list_fd.append(k)
                for j in list_varied:
                    if j.get("department") == k:
                        count_thd += 1  # 计数器+1
                        # 支持度计数，第3层 position职位：
                        if j.get("position") in dict_pot:
                            dict_pot[j.get("position")] += 1
                        else:
                            dict_pot[j.get("position")] = 1

        print("third layer:", dict_pot)
        for k in dict_pot.keys():
            print(k, ";", dict_pot.get(k)/count_thd)
        print()

        # 根据频繁的1层type寻找频繁的服务序列
        for i in list_ft:  # 每一个频繁的type， 第一层
            print("ft:", i)
            # if i.get("varied_pos")[0].get("type")
            for j in list_i:  # 对于每一个频繁的type对象找到其对应的所有频繁服务
                if j.get("varied_pos")[0].get("type") == i:
                    print("1-service:", j.get("service"))
                    # 写入数据库表格
                    service = self.de_multi_element(j.get("service"))
                    text = {"_id": self.get_next_id("CS"), "layer": 1, "type": i, "service": service}
                    print("text:", text)
                    self.insert_db(db_name="CS", input_tuple=text)
                    # 第二层频繁
                    for w in list_fd:
                        if j.get("varied_pos")[0].get("department") == w:
                            print("fd:", w)
                            print("2-service:", j.get("service"))
                            service = self.de_multi_element(j.get("service"))
                            text = {"_id": self.get_next_id("CS"), "layer": 2, "type": i, "department": w,
                                    "service": service}
                            print("text:", text)
                            self.insert_db(db_name="CS", input_tuple=text)

        print("size:", cursors.count())

# ----------------------------------------------------------------------------------------------------------

    """
    list[4, 4, 5, 4, 2, 2] -> [4, 5, 4, 2]
    """
    @classmethod
    def de_multi_element(cls, sequence):
        if len(sequence) == 0:
            return None
        de_multi_sequence = [sequence[0]]
        for i in range(len(sequence)):
            if i < len(sequence)-1:
                if sequence[i] != sequence[i+1]:
                    de_multi_sequence.append(sequence[i+1])
            if i == len(sequence) - 1:
                if sequence[i] != sequence[i-1]:
                    de_multi_sequence.append(sequence[i])
        return de_multi_sequence

# ----------------------------------------------------------------------------------------------------------

    """
    清空数据表格
    """
    def clear_all(self, db_name):
        # 1.删除varied_net数据库中的U0X用户的集合
        db = self.client.get_database(db_name)  # 读取的数据库
        collection = db.get_collection(self.collection_name)
        self.delete_one_collection(collection)
        # 2.将auto_incre 1数据表格归零
        count_col = db.get_collection("counters")
        count_col.update({"_id": self.collection_name}, {"$set": {"no": 0}})


# ----------------------------------------------------------------------------------------------------------


def main_operation():
    """Part1: 初始化参数"""
    ip_address = "127.0.0.1"  # 主机IP地址
    db_name = "CS"  # 读取数据库名字
    uid = "U06"  # 用户标识
    min_sup_pos = 0.4  # 数据状态varied_pos的支持度阈值
    psp = PrefixSpanPos(ip_address, db_name, uid, min_sup_pos)
    """Part2: """
    # 清空数据表格
    # fvs.clear_all(db_candidate_sequence)
    # fvs.iterate_cursor()


if __name__ == "__main__":
    # 记录算法运行开始时间
    start_time = time.clock()
    # main_operation
    main_operation()
    # 记录算法运行结束时间
    end_time = time.clock()
    print("Running time: %s Seconds" % (end_time - start_time))  # 输出运行时间(包括最后输出所有结果)
