"""
读入csv数据，到内存中
"""
import time
import pandas as pd
import DataPreprocessing.NaturalLanProcess as dpt4  # 引入自然语言处理
import pymongo
import codecs
import re


class ProcessingData:

    # 类公有变量
    nan_list = []  # 存放空值行的队列

    # 构造函数
    def __init__(self, file_path, db_name, collection_name, ip_address,
                 flag_insert, encode):
        self.file_path = file_path
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
        self.encode = encode

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        self.client.close()
        print(class_name, "Destroy.")

# ---------------------------------------------------------------------------------------

    # 读取文本中每行的节点队
    def read_file(self):
        data = pd.read_csv(self.file_path, encoding=self.encode)  # 读取数据
        print("data:")
        count = 0  # 计数器
        # 逐个元素判断是否为空值,将空值行，放入一个队列中
        for i in range(len(data)):
            print("i:", i)
            user_id = ""  # 用户ID
            service_id = ""  # 服务ID
            date_time = ""  # 格式化时间
            time_stamp = ""  # 时间戳
            activity = ""  # 行为
            content = ""  # 内容
            key_words = []  # 内容关键词（自然语言做的分词）
            title_text = ""  # 标题
            star_badge = ""  # 奖励
            row = data.iloc[i]  # 数据元组
            # print("type:", type(row), "row: ", row)
            for j in data.columns:
                j = str(j)
                # if str(data.iloc[i][j]) == "nan":
                #     print("空值", row, j, "element：", data.iloc[i][j])
                #     self.nan_list.append(row)
                #     continue
                element = str(data.iloc[i][j])
                if j == "用户ID":
                    user_id = element
                    print(j, ":", user_id)
                if j == "服务ID":
                    service_id = element
                    print(j, ":", service_id)
                if j == "时间":
                    if str(data.iloc[i][j]) == "nan":
                        # print("空值", row, j, "element：", data.iloc[i][j])
                        self.nan_list.append(row)
                        continue
                    element = element.replace("Z", "")
                    date_time = element
                    print(j, ":", date_time)
                    # 将格式化时间转换成时间戳10位
                    # 1中间过程，一般都需要将字符串转化为时间数组
                    timeArray = time.strptime(element, "%Y-%m-%d %H:%M:%S")
                    # 2将"2011-09-28 10:00:00"转化为时间戳
                    timestamp = int(time.mktime(timeArray))
                    print("timestamp:", timestamp, " type:", type(timestamp))
                    time_stamp = timestamp
                if j == "行为":
                    activity = element
                    print(j, ":", activity)
                if j == "内容":
                    content = element
                    print(j, ":", content)
                    temp_keywords = dpt4.main(element)   # keywords是一个List结构
                    print("keywords:", temp_keywords)
                    key_words += temp_keywords
                if j == "title":
                    title_text = element
                    print(j, ":", title_text)
                    temp_keywords = dpt4.main(title_text)  # keywords是一个List结构
                    print("keywords:", temp_keywords)
                    key_words += temp_keywords
                if j == "标记":
                    star_badge = element
                    print(j, ":", star_badge)
                    temp_keywords = dpt4.main(star_badge)  # keywords是一个List结构
                    print("keywords:", temp_keywords)
                    key_words += temp_keywords
                # end if
                # 调用Switch结构
            # 输出每一行的input_list
            _id = self.get_next_counter()
            insert_text = {"uid": self.collection_name, "用户ID": user_id,
                           "服务ID": service_id, "时间": date_time,
                           "timestamp": time_stamp, "activity": activity, "内容": content,
                           "keywords": key_words, "title": title_text, "标记": star_badge,
                           "_id": _id}
            print("row_input_list:", insert_text)
            count += 1
            # 插入数据库
            if self.flag_insert == "1":
                self.input_database(insert_text)
            print()
        # end for, 判断是不是有空值的元组
        print("The number of log:", count)
        if self.nan_list:
            for var_nan in self.nan_list:
                print("NaN row:", var_nan)
            print("空值的个数：", len(self.nan_list))

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
        for data in self.collection.find():
            print(data)
        print("总记录数为：", self.collection.find().count())
        self.client.close()

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
    读取txt文本文件到内存中
    """
    def read_lines_from_file(self, filename):
        counter = 0  # 计数器
        f = codecs.open(filename, "r+", self.encode)  # 读取中文
        line = f.readline()  # 读取一行
        # line.replace('\r\n', ' ')
        line = line.replace("   ", "")
        line.strip()  # 删除字符串左右的空格
        first_datetime = ""
        first_timestamp = ""
        second_datetime = ""
        second_timestamp = ""
        last_time = 0
        app_name = ""
        app_nic_name = ""
        while line:
            line = line.strip('\r\n')  # 去掉每个字符的'\r\n'
            print("line:", line)
            line = f.readline()
            elements = line.split(",")
            print("element_size:", len(elements))
            if len(elements) < 3:
                continue
            for i in range(len(elements)):
                print("i:", i, ", elements[i]:", elements[i])
                if (i == 0) and elements[i]:
                    first_datetime = elements[i]
                    first_timestamp = self.transform_datetime(first_datetime)
                if (i == 1) and elements[i]:
                    second_datetime = elements[i]
                    second_timestamp = self.transform_datetime(second_datetime)
                if (i == 2) and elements[i]:
                    app_name = elements[i]
                if (i == 3) and elements[i]:
                    app_nic_name = elements[i]
            if first_timestamp and second_timestamp:
                last_time = second_timestamp - first_timestamp
            _id = self.get_next_counter()
            input_text = {"_id": _id, "uid": self.collection_name,
                          "first_datetime": first_datetime,
                          "first_timestamp": first_timestamp,
                          "second_datetime": second_datetime,
                          "second_timestamp": second_timestamp,
                          "app_name": app_name,
                          "app_nickname": app_nic_name,
                          "last_time": last_time
                          }
            print("input_text:", input_text)
            counter += 1
            # 插入数据库
            if self.flag_insert == "1":
                self.input_database(input_text)
        print("The number of log:", counter)
        f.close()

# ----------------------------------------------------------------------------------------------------------

    """
    获取自增1的_id,默认与初始参数相同的数据库
    """
    def get_next_counter(self):
        collection = self.db.get_collection("counters")
        _id_obj = collection.find_and_modify(query={'_id': self.collection_name},
                                             update={"$inc": {"no": +1}},
                                             upsert=False,
                                             full_response=True, new=True)
        # print("_id_obj:", _id_obj)
        _id = _id_obj.get("value").get("no")
        # print("_id:", _id)
        return _id

# ----------------------------------------------------------------------------------------------------------

    """
    将标准时间转换成时间戳
    """
    @classmethod
    def transform_datetime(cls, date_time):
        # 转化成时间戳
        matchObj = re.search(r'(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})', date_time, re.M | re.I)
        if matchObj:
            date_time = matchObj.group(0)
            timeArray = time.strptime(date_time, "%Y-%m-%d %H:%M:%S")
            # 2将"2011-09-28 10:00:00"转化为时间戳
            timestamp = int(time.mktime(timeArray))
            return timestamp
        else:
            return None

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

"""
注意修改：UID UID UID UID UID UID UID UID UID UID UID UID UID UID UID UID UID UID UID UID

"""


def main_operation():
    """Part1: 初始化参数"""
    file_path = 'data/评论.csv'  # 读取文件路径和文件名
    ip_address = "127.0.0.1"  # 主机IP地址
    db_name = "predictionData"  # 数据库名字
    collection_name = "MU47"  # 集合的名字
    flag_insert = "1"  # 1代表写入数据库, 其他代表不输入数据库
    file_name = "../data/log47.txt"
    encode = 'utf-8'  # 编码方式
    dp1 = ProcessingData(file_path, db_name, collection_name,
                         ip_address, flag_insert, encode)
    dp1.read_lines_from_file(file_name)

if __name__ == "__main__":
    # 记录算法运行开始时间
    start_time = time.clock()
    # main_operation
    main_operation()
    # 记录算法运行结束时间
    end_time = time.clock()
    print("Running time: %s Seconds" % (end_time - start_time))  # 输出运行时间(包括最后输出所有结果)










