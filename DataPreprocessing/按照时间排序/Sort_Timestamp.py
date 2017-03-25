"""
读入csv数据，到内存中
"""
import time
import pymongo
from datetime import datetime
import datetime
import math


class SortTimestamp:

    # 类公有变量
    nan_list = []  # 存放空值行的队列

    # 构造函数
    def __init__(self, db_name, collection_name, ip_address,
                 flag_insert, piece):
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
        shares = math.ceil(sum_count / self.piece)
        print("shares:", shares)

# ---------------------------------------------------------------------------------------

    # 批量插入数据
    @classmethod
    def format_datetime(cls, element):
        element = element.replace("January", "01")
        element = element.replace("February", "02")
        element = element.replace("March", "03")
        element = element.replace("April", "04")
        element = element.replace("May", "05")
        element = element.replace("June", "06")
        element = element.replace("July", "07")
        element = element.replace("August", "08")
        element = element.replace("September", "09")
        element = element.replace("October", "10")
        element = element.replace("November", "11")
        element = element.replace("December", "12")
        element = element.replace("Jan", "01")
        element = element.replace("Feb", "02")
        element = element.replace("Mar", "03")
        element = element.replace("Apr", "04")
        element = element.replace("May", "05")
        element = element.replace("Jun", "06")
        element = element.replace("Jul", "07")
        element = element.replace("Aug", "08")
        element = element.replace("Sep", "09")
        element = element.replace("Oct", "10")
        element = element.replace("Nov", "11")
        element = element.replace("Dec", "12")
        print("new element:", element)
        # 格式化的字符串转换成Datetime, 具体看字符串的格式 "%d %m %Y %H:%M:%S"
        dt = datetime.datetime.strptime(element, "%m %d, %Y")
        date_time = str(dt)
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
        cursors = self.collection.find()
        # for data in cursors:
        #     print(data)
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
        for u in self.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            self.client.close()

    # 删除一个数据
    def delete_one(self):
        for u in self.collection.find({"_id": 1}):
            print("符合条件的记录(_id:1 ): ", u)
            self.collection.remove({"_id": 1})
            self.client.close()

    # 删除所有数据
    def delete_all(self):
        self.collection.remove()
        self.client.close()

# ----------------------------------------------------------------------------------------------------------


"""
switch功能
"""


class Switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for
            self.fall = True
            return True
        else:
            return False


# The following example is pretty much the exact use-case of a dictionary,
# but is included for its simplicity. Note that you can include statements
# in each suite.

v = 'ten3'
for case in Switch(v):
    if case('one'):
        print("1")
        break
    if case('two'):
        print("2")
        break
    if case('ten'):
        print('10')
        break
    if case('eleven'):
        print("11")
        break
    if case():  # default, could also just omit condition or 'if True'
        print("something else!")
        # No need to break here, it'll stop anyway

# ----------------------------------------------------------------------------------------------------------


def main_operation():
    """Part1: 初始化参数"""
    ip_address = "127.0.0.1"  # 主机IP地址
    db_name = "predictionData"  # 数据库名字
    collection_name = "U01"  # 读取数据集合的名字
    flag_insert = "0"  # 1代表写入数据库, 其他代表不输入数据库
    piece = 1000  # 每份多少个记录
    dp1 = SortTimestamp(db_name, collection_name,
                        ip_address, flag_insert, piece)
    dp1.find_all_records()  # 先从数据库中读取全部数据，每一份只有一千个数据。

if __name__ == "__main__":
    # 记录算法运行开始时间
    start_time = time.clock()
    # main_operation
    main_operation()
    # 记录算法运行结束时间
    end_time = time.clock()
    print("Running time: %s Seconds" % (end_time - start_time))  # 输出运行时间(包括最后输出所有结果)

