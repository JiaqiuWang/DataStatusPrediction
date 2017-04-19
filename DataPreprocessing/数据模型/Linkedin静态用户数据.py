"""
选出不同数据模型版本之间时间间隔参数，然后计算临近2个数据模型变化
"""

import time
import pymongo


class CreateModel:

    # 类公有变量
    nan_list = []  # 存放空值行的队列

    # 构造函数
    def __init__(self, db_name, collection_name, ip_address,
                 uid, flag):
        self.db_name = db_name
        self.collection_name = collection_name
        self.ip_address = ip_address
        self.uid = uid
        self.flag = flag
        # 全局变量-连接指定IP地址的数据库
        self.client = pymongo.MongoClient(self.ip_address, 27017)
        # 获取数据库
        self.db = self.client.get_database(self.db_name)  # 读取的数据库
        # 获取集合
        self.collection = self.db.get_collection(self.collection_name)

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
    def get_next_id(self, db):
        collection = db.get_collection("counters")
        _id_obj = collection.find_and_modify(query={'_id': "exp"},
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
    将字符时间转换成时间戳
    """
    @classmethod
    def date_transform_to_timestamp(cls, date_time):
        timeArray = time.strptime(date_time, "%Y-%m")
        # 2将"2011-09-28 10:00:00"转化为时间戳
        timestamp = int(time.mktime(timeArray))
        # print("timestamp:", timestamp)
        return timestamp

# ---------------------------------------------------------------------------------------

    """
    数据库操作
    """
    # 写入MongoDB数据库
    def insert_db(self):
        # 获取集合 --普通
        # collection = self.db.get_collection(self.collection_name)
        # date_from = "2012-08"
        # date_to = "2014-01"
        # timestamp_from = self.date_transform_to_timestamp(date_from)
        # timestamp_to = self.date_transform_to_timestamp(date_to)
        # # 时间戳转换成标准的字符串时间
        # date_from = self.get_datetime(timestamp_from)
        # date_to = self.get_datetime(timestamp_to)
        # duration = timestamp_to - timestamp_from
        # _id = self.get_next_id(self.db)
        # input_text = {"_id": _id, "uid": self.uid, "type": "Volunteer",
        #               "department": "Opera Software",
        #               "position": "Beta tester",
        #               "from": date_from, "to": date_to,
        #               "stamp_from": timestamp_from,
        #               "stamp_to": timestamp_to, "duration": duration}



        # 获取集合 ---至今的
        collection = self.db.get_collection(self.collection_name)
        date_from = "2012-08"
        timestamp_from = self.date_transform_to_timestamp(date_from)
        # 时间戳转换成标准的字符串时间
        date_from = self.get_datetime(timestamp_from)
        _id = self.get_next_id(self.db)
        input_text = {"_id": _id, "uid": self.uid, "type": "Volunteer",
                      "department": "Stack Exchange",
                      "position": "Participant",
                      "from": date_from, "to": "now",
                      "stamp_from": timestamp_from,
                      }

        print("input_text:", input_text)
        if self.flag == 1:
            # 添加单条记录到集合中
            collection.insert(input_text)



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
            new_id = self.get_next_id("data_status")
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

def asdf(value):
    for case in Switch(value):
        if case('one'):
            print("1")
            break
        if case('two'):
            print("2")
            break
        if case('ten'):
            print('10')
            return '10'
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
    db_name = "data_status"  # 读取数据库名字
    collection_name = "exp"  # 读取用户静态经历集合
    flag = 1  # 标志位，1：插入数据，否则不插入
    uid = "U04"
    # Part2: 插入数据库
    cm1 = CreateModel(db_name, collection_name, ip_address, uid, flag)
    cm1.insert_db()


if __name__ == "__main__":
    # 记录算法运行开始时间
    start_time = time.clock()
    # main_operation
    main_operation()
    # 记录算法运行结束时间
    end_time = time.clock()
    print("Running time: %s Seconds" % (end_time - start_time))  # 输出运行时间(包括最后输出所有结果)

























