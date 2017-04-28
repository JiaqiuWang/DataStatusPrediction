"""
选出不同数据模型版本之间时间间隔参数，然后计算临近2个数据模型变化
"""

import time
import pymongo


class FrequentVariedStatus:

    # 类公有变量

    # 构造函数
    def __init__(self, ip, db, uid, collection_name):
        self.ip = ip
        self.db_name = db
        self.uid = uid
        self.collection_name = collection_name
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
        collection = db_name.get_collection("counters")
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
    获取自增1的_id,
    数据库：data_status
    文档：counters
    """
    def iterate_cursor(self):
        # 获取集合
        collection = self.db.get_collection(self.uid)
        cursors = collection.find()
        for i in cursors:
            # if i.get("connect")[0]:
            #     print("relation:", i.get("connect")[0].get("relation"))
            if i.get("varied_pos"):
                print("varied_pos:", i.get("varied_pos"))
                print("relation：", i.get("relation"))
                print("service:", i.get("service"))
                print("")

            #
            #
            #
            #
            #
            #
            #
            # if len(i.get("connect")) == 0:
            #     print("asdfjaogn")
            #     continue
            # print("size:", len(i.get('connect')), "i.get(connect):", i.get('connect'), ", type:", type(i.get('connect')))
            # if len(i.get("connect")) != 0:
            #     print("type-i:", type(i.get("connect")[0].get("relation")), "i:", i.get("connect")[0])
            #     print("------------------------------")
        print("size:", cursors.count())

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
    db_name = "varied_net"  # 读取数据库名字
    uid = "U02"  # 用户标识
    collection_name = uid  # 读取数据集合的名字
    fvs = FrequentVariedStatus(ip_address, db_name, uid, collection_name)
    """Part2: """
    fvs.iterate_cursor()


if __name__ == "__main__":
    # 记录算法运行开始时间
    start_time = time.clock()
    # main_operation
    main_operation()
    # 记录算法运行结束时间
    end_time = time.clock()
    print("Running time: %s Seconds" % (end_time - start_time))  # 输出运行时间(包括最后输出所有结果)

