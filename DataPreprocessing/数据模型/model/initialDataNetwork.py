"""
选出不同数据模型版本之间时间间隔参数，然后计算临近2个数据模型变化
"""

import time
import pymongo
from rdflib import Graph
from rdflib import Literal


class CreateModel:

    # 类公有变量
    nan_list = []  # 存放空值行的队列

    # 构造函数
    def __init__(self, db_name, collection_name, ip_address,
                 flag_insert, interval_s, k_no):
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
        # 版本时间间隔
        self.interval_s = interval_s
        self.first_stamp = 0  # 初始时间戳
        self.k_no = k_no  # 初始数据网络包含的文档数

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        self.client.close()
        print(class_name, "Destroy.")

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
    获取第一条记录和对应的时间戳
    """
    def get_first_stamp(self):
        # 查询所有
        cursors = self.collection.find_one({"_id": 1})
        print("cursor:", cursors)
        print("first_timestamp:", cursors.get("timestamp"))
        self.first_stamp = cursors.get("timestamp")
        self.client.close()

# ---------------------------------------------------------------------------------------

    """
    Part2: 创建初始个人数据网络,选取时间序列中前k条记录作为构建网络的基础结构
    """
    def initial_data_status(self):
        graph = Graph()  # 初始化的记录用一个图
        # 空节点
        _uid = Literal("uid")
        _user = Literal("user")
        _sn = Literal("service")
        _datetime = Literal("datetime")
        _timestamp = Literal("timestamp")
        _activity = Literal("activity")
        _content = Literal("content")
        _keywords = Literal("keywords")
        _is = Literal("_is")
        counter = 0  # 计数器
        # 查询所有
        cursors = self.collection.find()
        for data in cursors:
            uid = ""
            user = ""
            service_name = ""
            datetime = ""
            timestamp = 0
            activity = ""
            content = ""
            keywords = []
            counter += 1
            if counter > self.k_no:
                return
            # 调用创建RDF个人数据网络的函数
            print("type:", type(data))
            for key in data:
                value = data[key]
                print("key:", key, ":", value)
                if key == "uid":
                    uid = Literal(value)
                if key == '用户ID':
                    user = Literal(value)
                    print("user:", user)
                if key == "服务ID":
                    service_name = Literal(value)
                if key == "时间":
                    datetime = Literal(value)
                if key == "timestamp":
                    timestamp = Literal(value)
                if key == "activity":
                    activity = Literal(value)
                if key == "内容":
                    content = Literal(value)
                if key == "keywords":
                    keywords = Literal(value)
            if service_name == Literal("blogs"):
                graph.add((_uid, _is, uid))
                graph.add((_user, _is, user))
                graph.add((_sn, _is, service_name))
                graph.add((_datetime, _is, datetime))
                graph.add((_timestamp, _is, timestamp))
                if activity == "":
                    activity = Literal("Post")
                graph.add((_activity, _is, activity))
                graph.add((_content, _is, content))
                graph.add((_keywords, _is, keywords))
                print("turtle:", graph.serialize(format='n3'))














        print("counter:", counter)


# ---------------------------------------------------------------------------------------

    """
    生成一个数据模型的版本
    """
    def generate_RDF(self):
        if self.first_stamp == 0:
            print("没获取到第一个时间戳！")
        else:
            print("first_stamp:", self.first_stamp, ", one_interval:",
                  self.interval_s + self.first_stamp)
            print("first_date:", self.get_datetime(self.first_stamp),
                  ", one_interval_date:", self.get_datetime((self.interval_s +
                                                             self.first_stamp)))
            # 查询所有
            cursors = self.collection.find()
            for data in cursors:
                if data.get("timestamp") <= (self.interval_s + self.first_stamp):
                    print("date:", data.get('时间'))

# ---------------------------------------------------------------------------------------

    """
    将时间戳转换成时间
    """
    @classmethod
    def get_datetime(cls, timestamp):
        # 将时间戳timestamp转换成格式化的字符串Datetime
        l_time = time.localtime(timestamp)
        date_time = time.strftime("%Y-%m-%d %H:%M:%S", l_time)
        return date_time


# ---------------------------------------------------------------------------------------

    """
    数据库操作
    """
    # 写入MongoDB数据库
    def input_database(self, input_tuple):
        # 添加单条记录到集合中
        self.collection.insert(input_tuple)

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
    db_name = "data_status"  # 数据库名字
    collection_name = "U01"  # 读取数据集合的名字
    flag_insert = "0"  # 标志位，1代表写入数据库, 其他代表不输入数据库
    # 模型版本的间隔时间单位，day：一天
    day = 100  # 天数，可以是1/2, 1/3等
    interval_s = 24*60*60*day  # 以秒计数
    # Part2: 创建初始个人数据网络,选取时间序列中前k条记录作为构建网络的基础结构
    k_no = 50
    # 所有的参数初始化，并建立类的对象
    cm1 = CreateModel(db_name, collection_name, ip_address,
                      flag_insert, interval_s, k_no)
    cm1.initial_data_status()
    # cm1.get_first_stamp()  # 获取第一条时间戳
    # cm1.generate_RDF()  # 产生一个RDF模型


if __name__ == "__main__":
    # 记录算法运行开始时间
    start_time = time.clock()
    # main_operation
    main_operation()
    # 记录算法运行结束时间
    end_time = time.clock()
    print("Running time: %s Seconds" % (end_time - start_time))  # 输出运行时间(包括最后输出所有结果)






















