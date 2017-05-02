"""
选出不同数据模型版本之间时间间隔参数，然后计算临近2个数据模型变化
"""

import time
import pymongo
import DataPreprocessing.数据模型.class_model as cm  # 导入模块
import Levenshtein


class CreateModel:

    # 类公有变量
    nan_list = []  # 存放空值行的队列

    # 构造函数
    def __init__(self, db_name, collection_name, ip_address, k_no,
                 ratio, net_db):
        self.db_name = db_name
        self.collection_name = collection_name
        self.ip_address = ip_address
        # 全局变量-连接指定IP地址的数据库
        self.client = pymongo.MongoClient(self.ip_address, 27017)
        # 获取数据库
        self.db = self.client.get_database(self.db_name)  # 读取的数据库
        self.net_db = self.client.get_database(net_db)  # 待写入的数据库
        # 获取集合
        self.collection = self.db.get_collection(self.collection_name)
        self.first_stamp = 0  # 初始时间戳
        self.k_no = k_no  # 初始数据网络包含的文档数
        self.ratio = ratio
        self.list_network = []  # 存放初始个人数据网络,包括节点,存放实例对象
        self.list_network_relation = []  # 存放关系
        self.position = []  # 存放linkedin个人静态数据节点的列表
        self.flag = False  # 判断是否存在Linkedin静态数据

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
    Part2: 创建初始个人数据网络,选取时间序列中前k条记录作为构建网络的基础结构
    """
    def initial_data_status(self):
        counter = 0  # 计数器
        # 查询所有记录
        cursors = self.collection.find()
        for data in cursors:
            # 大于初始数据网络的一条数据处理
            if counter >= self.k_no:
                break
            # 设置Linkedin用户状态数据的初始状态
            if counter == self.k_no - 1:
                print("最后一条记录！！")
                self.flag = self.initialize_linked_status(data)
            obj = self.create_class_obj(data)  # 创建对象
            self.list_network.append(obj)
            counter += 1  # 计数器
            print("counter:", counter)
            # 查找联系
            if counter >= 2:
                for i in range(len(self.list_network)):
                    iter_obj = self.list_network[i]  # 迭代的对象
                    original_content = obj.get_content()
                    if (original_content == "") or (original_content is None):
                        original_content = str(obj.get_keywords())
                    if obj is iter_obj:
                        continue
                    iterate_content = iter_obj.get_content() + \
                        iter_obj.get_title()
                    if (iterate_content == "") or (iterate_content is None):
                        iterate_content = str(iter_obj.get_keywords())
                    print("original_content:", original_content)
                    print("iter_cont:", iterate_content)
                    # 计算两个不同文本的相似性
                    rate = Levenshtein.ratio(original_content, iterate_content)
                    print("rate:", rate)
                    # 判断如果相似率大于阈值，则存入个人数据网络中
                    if rate >= self.ratio:
                        # obj新插入的对象； iter_obj是老对象
                        # print("新对象对应的Class:", obj.__class__.__name__,
                        #       ", type:", type(obj.__class__.__name__))

                        # 获取联系
                        relation = cm.get_relation(iter_obj.__class__,
                                                   obj.__class__)
                        # 存入初始个人数据网络，字典数据结构
                        dict_relation = {"pre_id": iter_obj.get_id(), "relation": relation, "post_id": obj.get_id(),
                                         "pre_Class": iter_obj.__class__.__name__,
                                         "post_Class": obj.__class__.__name__, "pre_Activity": iter_obj.get_activity(),
                                         "post_Activity": obj.get_activity()}
                        self.list_network_relation.append(dict_relation)

        # self.list_network.extend(self.list_network_relation)
        # 1.节点
        if self.list_network:
            for i in range(len(self.list_network)):
                print("i:", i, ", list_network:", self.list_network[i])
        else:
            print("list_network is empty!")
        # 2.联系
        if self.list_network_relation:
            for i in range(len(self.list_network_relation)):
                print("i:", i, ", list_network:", self.list_network_relation[i])
        else:
            print("list_network_relation is empty!")
        # 3.输出用户职位数据 linkedin
        if self.position:
            for i in range(len(self.position)):
                print("i:", ", position:", self.position[i])
        else:
            print("list_position is Empty!")
        print("counter:", counter)


# ---------------------------------------------------------------------------------------

    """
    计算初始数据网络之后的数据节点和变化, document是初始个人数据网络的最后一个文档
    """
    def initialize_linked_status(self, document):
        timestamp = document.get("timestamp")
        print("_id:", document.get("_id"), ", timestamp:", timestamp)
        # 循环获取所有的linkedin所有状态，查找目前用户所处的状态
        cursor = self.if_there_exp()
        if cursor:
            for i in cursor:
                print("i-:", i)
                if i.get("stamp_from") <= timestamp <= i.get("stamp_to"):
                    # print("i&:", i)
                    print("initial pos:", i)
                    self.position.append(i)
                if i.get("to") == "now":
                    current_time = int(time.time())
                    if i.get("stamp_from") <= timestamp <= current_time:
                        # print("i&:", i)
                        self.position.append(i)
            return True
        else:  # 如果不存在linked in 服务
            print("flag:", cursor)
            return False

# ---------------------------------------------------------------------------------------

    """
    计算用户静态数据是否有变化,先判断是否有Linkedin 数据
    """
    def if_there_exp(self):
        # 查询该用户是否有linkedin记录
        # 获取集合
        collection = self.db.get_collection("exp")
        cursors = collection.find({"uid": self.collection_name}).sort([("stamp_from", 1)])
        # print("cursor:", cursors.count(), ", type:", type(cursors.count()))
        if cursors.count() == 0:
            print("没有 pos")
            return False
        else:
            print("YOU POS")
            return cursors

# ---------------------------------------------------------------------------------------

    """
    计算初始数据网络之后的数据节点和变化
    """
    def compute_data_network(self):
        new_LNR = []  # 存放新生成的关系
        new_obj = []  # 存放新生成的实例对象
        new_obj_dict = []  # 存放新生成的对象字典
        list_service = []  # 存放新生成的service
        # 查询所有除了initial网络以外的数据
        cursors = self.collection.find(no_cursor_timeout=True).skip(self.k_no)
        counter = 0  # 计数器
        for data in cursors:
            # if counter > 30:
            #     break
            counter += 1
            print("data:", data)
            obj = self.create_class_obj(data)
            print("服务：", data.get("服务ID"))
            # print("实例对象:", obj.__class__.__name__, ", 实例：", obj.get_id())
            data['object'] = obj.__class__.__name__
            print("实例对象:", data)
            # print("obj_id:", obj.get_id())
            print("count:", counter)
            new_obj.append(obj)  # 将新的实例对象添加进
            new_obj_dict.append(data)  # 对象的字典形式
            list_service.append(data.get("服务ID"))
            # 1.计算新节点与原数据网络的关系
            dict_relation = self.compute_updating_relation(obj)
            # 2.计算数据状态的变化-linkedin用户职位变化
            dict_varied = []
            if self.flag:
                # dict_varied变量是List类型
                dict_varied = self.compute_updating_position(obj)
            if len(dict_relation) != 0 or len(dict_varied) != 0:
                print("dict_relation:", dict_relation)
                new_LNR.clear()
                new_LNR.append(dict_relation)
                # 插入数据库
                _id = self.get_next_id(self.net_db)
                input_text = {"_id": _id, "service": list_service,
                              "instance": new_obj_dict,
                              "connect": new_LNR,
                              "varied_pos": dict_varied
                              }
                print("input_text:", input_text)
                self.insert_db(input_text)
                new_obj_dict.clear()
                list_service.clear()
                # end 1: 将新新生成的若干实例对象，存储到前一个版本的实例网络中，即self.list_network
                for j in range(len(new_obj)):
                    self.list_network.append(new_obj[j])
                new_obj.clear()  # 清空
                # end 2: 将新产生的联系,添加到上一个版本的联系队列里面，形成下一个版本的前一个版本
                for item in dict_relation:
                    self.list_network_relation.append(item)
                dict_relation.clear()
            print("*-*-*-*-*-*-*-*-*-*-*-*")
            new_LNR.append(dict_relation)  # 新关系


# ---------------------------------------------------------------------------------------

    """
    计算联系的变化
    """
    def compute_updating_relation(self, obj):
        list_rela = []
        print("新个人数据网络的实例个数：", len(self.list_network))
        for i in range(len(self.list_network)):
            iter_obj = self.list_network[i]  # 迭代的对象
            original_content = obj.get_content()
            if (original_content == "") or (original_content is None):
                original_content = str(obj.get_keywords())
            if obj is iter_obj:
                continue
            iterate_content = iter_obj.get_content() + iter_obj.get_title()
            if (iterate_content == "") or (iterate_content is None):
                iterate_content = str(iter_obj.get_keywords())
            # print("original_content:", original_content)
            # print("iter_cont:", iterate_content)
            # 计算两个不同文本的相似性
            rate = Levenshtein.ratio(original_content, iterate_content)
            # print("rate:", rate)
            # 判断如果相似率大于阈值，则存入个人数据网络中
            if rate >= self.ratio:
                print("rate:", rate)
                # obj新插入的对象； iter_obj是老对象
                # print("新对象对应的Class:", obj.__class__.__name__,
                #       ", type:", type(obj.__class__.__name__))
                # 获取联系
                relation = cm.get_relation(iter_obj.__class__, obj.__class__)
                # 存入初始个人数据网络，字典数据结构
                dict_relation = {"pre_id": iter_obj.get_id(), "relation": relation, "post_id": obj.get_id(),
                                 "pre_Class": iter_obj.__class__.__name__,
                                 "post_Class": obj.__class__.__name__, "pre_Activity": iter_obj.get_activity(),
                                 "post_Activity": obj.get_activity()}
                # 将每一个新联系加载到队列中
                print("新联系:", dict_relation)
                list_rela.append(dict_relation)
        return list_rela

# ---------------------------------------------------------------------------------------

    """
    计算position的变化
    """
    def compute_updating_position(self, obj):
        varied_position = []  # 变化的position
        # 1.计算当前所处的position
        timestamp = obj.get_timestamp()  # 当前记录的时间戳
        datetime = obj.get_datetime()  # 当前记录的时间
        print("该记录的时间：", datetime)
        current_position = []
        # 获取集合
        collection = self.db.get_collection("exp")
        cursors = collection.find({"uid": self.collection_name}).sort([("stamp_from", 1)])
        for i in cursors:
            if i.get("to") == "now":
                current_time = int(time.time())
                if int(i.get("stamp_from")) <= timestamp <= current_time:
                    current_position.append(i)
            elif int(i.get("stamp_from")) <= timestamp <= int(i.get("stamp_to")):
                current_position.append(i)
        # 计算变化， 前面的版本self.position,后面版本current_position
        temp_pre_pos = self.position.copy()
        print("pre-version:")
        for w in temp_pre_pos:
            print(w)
        print("current-version:")
        temp_cur_pos = current_position.copy()
        for t in temp_cur_pos:
            print(t)
        same_temp_pos = []
        for j in temp_cur_pos:
            # print("current_pos:", j.get("_id"))
            for k in temp_pre_pos:
                # print("pre_V所有字典值：", k.values())
                if j.get("_id") in k.values():
                    same_temp_pos.append(j)
                    continue
        # 把所有的_id放到一起
        same_temp_pos_ids = []
        # print("same_temp_pos:", len(same_temp_pos))
        for i in same_temp_pos:
            # print(i.get("_id"))
            same_temp_pos_ids.append(i.get("_id"))
        # pre-version和current-version分别删除相同的，保留不同的。就是最后变化的部分
        for i in temp_pre_pos:
            if i.get("_id") not in same_temp_pos_ids:
                varied_position.append(i)
        for i in temp_cur_pos:
            if i.get("_id") not in same_temp_pos_ids:
                varied_position.append(i)
        print("varied_pos:")
        for i in varied_position:
            print("变化的Position:", i)
        # 把currrent_pos赋值给pre_version
        self.position = current_position
        return varied_position

# ---------------------------------------------------------------------------------------

    """
    生成数据类的对象
    """
    def create_class_obj(self, data):
        _id = ""
        uid = ""
        user = ""
        service_name = ""
        datetime = ""
        timestamp = 0
        activity = ""
        title = ""
        content = ""
        keywords = []
        for key in data:
            value = data[key]
            # print("key:", key, ":", value)
            if key == "_id":
                _id = value
            if key == "uid":
                uid = value
            if key == '用户ID':
                user = value
                # print("user:", user)
            if key == "服务ID":
                service_name = value
            if key == "时间":
                datetime = value
            if key == "timestamp":
                timestamp = value
            if key == "activity":
                activity = value
            if key == "内容":
                content = value
            if key == "title":
                title = value
            if key == "keywords":
                keywords = value
        data_class = self.get_data_class(service_name)
        # print("对应的数据类：", data_class)
        obj = cm.get_class(data_class)(_id=_id, uid=uid,
                                       u_name=user, datetime=datetime,
                                       timestamp=timestamp,
                                       service=service_name,
                                       activity=activity, content=content,
                                       title=title, keywords=keywords)
        # print('obj:', obj, ", _id:", obj.get_id())
        return obj

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
    将时间戳转换成时间
    """
    def clear_all(self):
        # 1.删除varied_net数据库中的U0X用户的集合
        collection = self.net_db.get_collection(self.collection_name)
        self.delete_one_collection(collection)
        # 2.将auto_incre 1数据表格归零
        count_col = self.net_db.get_collection("counters")
        count_col.update({"_id": self.collection_name}, {"$set": {"no": 0}})

# ---------------------------------------------------------------------------------------

    """
    数据库操作
    """
    # 写入MongoDB数据库
    def insert_db(self, input_tuple):
        # 获取集合
        collection = self.net_db.get_collection(self.collection_name)
        # 添加单条记录到集合中
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
    @classmethod
    def delete_one_collection(cls, col):
        col.remove()
        # self.client.close()

# ----------------------------------------------------------------------------------------------------------

    """
    确定每个服务归属于哪一个数据类
    """
    @classmethod
    def get_data_class(cls, service):
        if service in ("Twitter", "Google Plus", "Facebook", "Reddit"):
            return "SNS"
        if service in ("Stack Overflow", "ABT"):
            return "Stack"
        if service in ("META", "Software Engineering", "Code Review",
                       "Web Applications", "Ubuntu",
                       "Server Fault", "Information Security",
                       "Ask Ubuntu", "German Language", "Biology",
                       "Religion"
                       ):
            return "FAQ"
        if service in ("Super User", "English Language & Usage",
                       "Drupal Answers", "English Language Learners",
                       "Seasoned Advice", "Database Administrators",
                       "Programming Puzzles", "skeptics", "TEX",
                       "Science Fiction & Fantasy", "Workplace",
                       "Christianity", "Unix & Linux", "Bicycles",
                       "Webmasters", "Arqade", "Movies & TV", "Travel",
                       "Personal Productivity"):
            return "YL"
        if service in ("blogs", "Blog", "Blogs", "blog", "Quora", "Pinboard"):
            return "Blog"
        if service in ("Github", "Gitlib", "Bitbucket", "jessehouwing"):
            return "Git"
        if service in ("Youtube", "Last.fm", "flickr", "Instagram", "vimeo"):
            return "Media"
        if service in ("Amazon", "mall"):
            return "EC"
        return "others"

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
    collection_name = "U06"  # 读取数据集合的名字
    net_db = "varied_net"  # 变化的个人数据网络-数据库
    # Part2: 创建初始个人数据网络,选取时间序列中前k条记录作为构建网络的基础结构
    k_no = 50
    # 所有的参数初始化，并建立类的对象
    # 文本相似度比率
    ratio = 0.7
    cm1 = CreateModel(db_name, collection_name, ip_address, k_no, ratio, net_db)
    cm1.initial_data_status()
    # 清空数据表格
    cm1.clear_all()
    # 计算初始数据网络之后的数据网络和联系
    cm1.compute_data_network()

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

