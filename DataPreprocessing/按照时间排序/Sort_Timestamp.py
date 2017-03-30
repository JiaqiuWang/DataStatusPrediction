"""
读入csv数据，到内存中
"""
import time
import pymongo


class SortTimestamp:

    # 类公有变量
    nan_list = []  # 存放空值行的队列

    # 构造函数
    def __init__(self, db_name, collection_name, ip_address,
                 flag_insert, piece, new_db):
        self.db_name = db_name
        self.collection_name = collection_name
        self.ip_address = ip_address
        # 全局变量-连接指定IP地址的数据库
        self.client = pymongo.MongoClient(self.ip_address, 27017)
        # 获取数据库
        self.db = self.client.get_database(self.db_name)
        # 获取集合
        self.collection = self.db.get_collection(self.collection_name)
        # 是否插入数据库标识位
        self.flag_insert = flag_insert
        # 一份多少个记录
        self.piece = piece
        # 待插入数据的新数据库
        self.new_db = self.client.get_database(new_db)

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        self.client.close()
        print(class_name, "Destroy.")

# ---------------------------------------------------------------------------------------

    # 读取文本中每行的节点队
    def find_all_records(self):
        sum_count = self.find_all()
        print("sum_count:", sum_count)

# ---------------------------------------------------------------------------------------

    """
    获取自增1的_id,
    数据库：data_status
    文档：counters
    """
    def get_next_counter(self, db_name):
        new_db = self.client.get_database(db_name)
        collection = new_db.get_collection("counters")
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
    def input_database(self, input_tuple):
        # 添加单条记录到集合中
        self.collection.insert(input_tuple)

    # 写入MongoDB数据库
    def input_status_data(self, input_tuple):
        # 添加单条记录到集合中
        collection = self.new_db.get_collection(self.collection_name)
        collection.insert(input_tuple)

    # 批量插入数据
    def input_many_database(self, input_tuple):
            # 添加单条记录到集合中
            self.collection.insert_many(input_tuple)

    # 查询所有collections
    def find_all(self):
        # 查询所有
        cursors = self.collection.find().sort([("timestamp", 1)])
        for data in cursors:
            print("type:", type(data), ", data:", data)
            # 更换_id
            new_id = self.get_next_counter("data_status")
            data['_id'] = new_id
            print("new_data:", data)

            # 插入新的数据库
            self.input_status_data(data)
        print("总记录数为：", cursors.count())
        self.client.close()
        return cursors.count()

    # 更新数据库
    def update_database(self):
        self.collection.update({"_id": 1, "pPer_id": "p2"},
                               {"$set": {"pName": "卫国"}})
        self.client.close()

    # 查找一个文档
    def find_one(self):
        count = 0
        for u in self.collection.find({"timestamp": '', "时间": ''}):
            print("符合条件的记录: ", u)
            print("timestamp:", u.get("timestamp"), ", type:", type(u.get("timestamp")))
            count += 1
            print()
            self.client.close()
        print("count:", count)

    # 删除一个数据
    def delete_one(self):
        for u in self.collection.find({"timestamp": '', "时间": ''}):
            print("符合条件的记录(_id): ", u.get("_id"))
            self.collection.remove({"_id": u.get("_id")})
            self.client.close()

    # 删除所有数据
    def delete_all(self):
        self.collection.remove()
        self.client.close()

# ----------------------------------------------------------------------------------------------------------


def main_operation():
    """Part1: 初始化参数"""
    ip_address = "127.0.0.1"  # 主机IP地址
    db_name = "predictionData"  # 数据库名字
    collection_name = "U05"  # 读取数据集合的名字
    flag_insert = "0"  # 1代表写入数据库, 其他代表不输入数据库
    piece = 1000  # 每份多少个记录
    new_db = "data_status"  # 待插入的新数据库
    dp1 = SortTimestamp(db_name, collection_name,
                        ip_address, flag_insert, piece, new_db)
    dp1.delete_one()   # 删除时间为空值的行
    dp1.find_all_records()  # 先从数据库中读取全部数据，每一份只有一千个数据。
    # 读取一条记录, 参数_id
    # dp1.find_one()


if __name__ == "__main__":
    # 记录算法运行开始时间
    start_time = time.clock()
    # main_operation
    main_operation()
    # 记录算法运行结束时间
    end_time = time.clock()
    print("Running time: %s Seconds" % (end_time - start_time))  # 输出运行时间(包括最后输出所有结果)

