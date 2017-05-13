"""
选出不同数据模型版本之间时间间隔参数，然后计算临近2个数据模型变化
V5-11 17:10备份
"""

import time
import pymongo
import pyfpgrowth


class FrequentVariedStatus:

    # 类公有变量

    # 构造函数
    def __init__(self, ip, db, uid, min_sup_pos, min_sup_rel,
                 collection_name):
        self.ip = ip
        self.db_name = db
        self.uid = uid
        self.min_sup_pos = min_sup_pos
        self.min_sup_rel = min_sup_rel
        self.collection_name = collection_name
        # 全局变量-连接指定IP地址的数据库
        self.client = pymongo.MongoClient(self.ip, 27017)
        # 获取数据库
        self.db = self.client.get_database(self.db_name)  # 读取的数据库
        # 获取集合
        collection = self.db.get_collection(self.uid)
        self.cursors_T = collection.find(no_cursor_timeout=True)
        self.dict_FP = {}
        self.fp_status = {}  # 使用fp-growth获取的频繁数据状态
        self.total_elements = []  # 存放所有变化的事务集合，里面是一个个的元素，元素里面是一个个项/项集
        self.fp_vts = []  # 频繁变化的数据状态的时间序列
        self.total_ele_service = []  # 存放所有变化的联系对应的服务序列 type:list, 里面每个是一个dict

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
    获取集合
    """
    def iterate_cursor_rel(self):
        # 获取游标
        self.cursors_T.rewind()
        if self.cursors_T:
            counter = 0  # 计数器
            for i in self.cursors_T:
                # if counter >= 2500:
                #     break
                if len(i.get("connect")[0]) == 0:
                    continue
                counter += 1
                print("counter:", counter)
                element_rel = []  # 存放每一个元素的队列
                print("_id:", i.get("_id"), ", length:", len(i.get("connect")[0]),
                      ", connect:", i.get("connect")[0])
                for j in i.get("connect")[0]:
                    # print("j:", j)
                    str_element = str(j.get("pre_Class")).strip() + "_" + \
                                  str(j.get("relation")).strip() + "_" +\
                                  str(j.get("post_Class")).strip()
                    if str_element not in element_rel:
                        element_rel.append(str_element)
                dict_each_id_ele_ser = {}
                print("element_rel:", tuple(element_rel))
                services = self.de_multi_element(i.get("service"))
                print("service:", services)
                dict_each_id_ele_ser[tuple(element_rel)] = services  # 放进临时字典变量
                print("dict_each_id_lel_ser:", dict_each_id_ele_ser)
                self.total_ele_service.append(dict_each_id_ele_ser)  # 装进全局变量中保存里面
                self.total_elements.append(element_rel)  # 保存所有的关系element
            # end for
            print()
            print("total_elements:")
            # invoking function调用频繁模式增长算法 FP-Growth
            self.fp_growth(self.total_elements)
            dict_re = {"total_rel": self.total_elements, "fp_status": self.fp_status}
            return dict_re

        else:
            print("cursor_real is None!")

# ---------------------------------------------------------------------------------------

    """
    频繁模式增长算法 FP-Growth, 参数total_elements是事务集合
    """
    def fp_growth(self, total_elements):
        if len(total_elements) == 0:
            print("total_element is Empty!")
            return
        min_sup = len(total_elements) / 100
        patterns = pyfpgrowth.find_frequent_patterns(total_elements, min_sup)
        self.fp_status = patterns
        print("All patterns:", patterns)
        # print("type-pattern:", type(patterns))
        # for i in patterns.keys():
        #     print("i:", list(i), ", sup:", patterns[i])
        #     self.fp_status[list(i)] = patterns[i]  不可以List作为key

# ---------------------------------------------------------------------------------------

    """
    查找频繁变化的数据状态的时间序列,prefixSpan前缀模式投影算法
    """
    def fp_sequence_status(self, total_elements, fp_status):
        if not fp_status:  # fp_status是字典
            print("频繁变化的数据状态为空！")
            return
        if len(total_elements) == 0:  # total_elements 是队列嵌套队列
            print("所有变化的事务集合 is Empty!")
            return
        print("type-fp-status:", type(fp_status))
        if type(fp_status) == dict:
            for i in self.fp_status.keys():
                dict_part_fp = {}
                print("i:", i, ", type:", type(i))
                # 提取后缀数据序列 post_list
                post_list = self.get_post_trans(tuple_item_set=i,
                                                total_elements=total_elements)
                print("post_list:", post_list)

                print()
                if len(post_list) != 0:  # 寻找局部频繁项
                    for element in post_list:
                        for item in element:
                            # print("item:", item)
                            if item in dict_part_fp.keys():
                                dict_part_fp[item] += 1
                            else:
                                dict_part_fp[item] = 1
                    for c_fp in dict_part_fp.keys():
                        # print("c-fp:", c_fp)
                        if dict_part_fp[c_fp]/len(dict_part_fp) > 0.5:
                            new_fp_status = i + (c_fp,)
                            print("new fp_status:", new_fp_status)
                            self.fp_vts.append(list(new_fp_status))
                            self.fp_sequence_growth(total_elements, new_fp_status)
                    print()

# ---------------------------------------------------------------------------------------

    """
    递归调用
    """
    def fp_sequence_growth(self, total_elements, new_fp_status):
        if len(new_fp_status) == 0:  # new_fp_status是tuple
            print("new_fp_status是tuple is tuple")
            return
        if len(total_elements) == 0:  # total_elements 是队列嵌套队列
            print("所有变化的事务集合 is Empty!")
            return
        dict_part_fp = {}  # 用于计算局部频繁项的字典
        # 提取后缀数据序列 post_list
        post_list = self.get_post_trans(tuple_item_set=new_fp_status,
                                        total_elements=total_elements)
        print("post_list:", post_list)
        print()
        if len(post_list) != 0:  # 寻找局部频繁项
            for element in post_list:
                for item in element:
                    # print("item:", item)
                    if item in dict_part_fp.keys():
                        dict_part_fp[item] += 1
                    else:
                        dict_part_fp[item] = 1
            for c_fp in dict_part_fp.keys():
                # print("c-fp:", c_fp)
                if dict_part_fp[c_fp] / len(dict_part_fp) > 0.5:
                    new_fp_status += (c_fp,)
                    print("new fp_status:", new_fp_status)
                    self.fp_vts.append(list(new_fp_status))
                    if len(new_fp_status) != 0:
                        self.fp_sequence_growth(total_elements, new_fp_status)
            print()

# ---------------------------------------------------------------------------------------

    """
    寻找包含该item的元素element，输入参数1.item,2.trans事务集合
    输出：投影后的事务集合List
    """
    def get_post_trans(self, tuple_item_set, total_elements):
        post_list = []
        for i in total_elements:
            flag = True
            if len(tuple_item_set) >= len(i):
                continue
            # print("tuple_item_set:", tuple_item_set, ", element:", i)
            for j in tuple_item_set:
                if j not in i:
                    flag = False
                    break

            if flag:
                # print("flag:", flag)
                # print("last_one:", tuple_item_set[-1])  # item_set中最后一个item
                # print("element:", i)
                index = i.index(tuple_item_set[-1])  # 在i中查找item的后缀
                if index != len(i) - 1:
                    one_element_list = i[index + 1:]
                    # print("one_element_list:", one_element_list)
                    post_list.append(one_element_list)
        # print("post_list:", post_list)
        return post_list


# ---------------------------------------------------------------------------------------

    """
    输出频繁变化的数据状态序列
    """
    def printout_vts(self):
        for i in self.fp_vts:
            print("sequence:", i)

# ---------------------------------------------------------------------------------------

    """
    寻找每个vts对应的服务序列
    """
    def get_fp_services(self):
        print("寻找每个vts对应的服务序列")
        for i in self.fp_vts:
            list_cs = []
            print("VTS:", i)
            for j in self.total_ele_service:
                # print("type-j:", type(j), ", j:", j)
                for k in j.keys():
                    # print("k:", k)
                    for item in k:
                        # print("item:", item)
                        if item in i:
                            # print("service:", j[k])
                            list_cs.append(j[k])
            # 计算该sequence对应的频繁服务序列
            # print("prefixspan-")
            # print("list_cs:", list_cs)
            self.prefixspan_service(list_cs)


# ---------------------------------------------------------------------------------------

    """
    prefixSpan前缀投影模式增长算法，挖掘频繁时间序列['Stack Overflow', 'Youtube', 'Stack Overflow', 'Twitter', 'Github']
    ['Github', 'Stack Overflow', 'Github']
    """
    def prefixspan_service(self, list_sequence):
        fp_one_sequence = []  # 存放调用一次的所有
        dict_fp_1s = {}  # 频繁一序列的计数器
        # 寻找频繁一序列
        # 将list_sequence变成一个不重复的序列
        list_dis_seq = self.get_dis_dul_sequence(list_sequence)
        # print("list_dis_dup:", list_dis_seq)
        for element in list_dis_seq:
            for item in element:
                if item in dict_fp_1s.keys():
                    dict_fp_1s[item] += 1
                else:
                    dict_fp_1s[item] = 1
        for k in dict_fp_1s.keys():
            # print("key:", k, ", sup:", dict_fp_1s[k],
            #       ", size-list-sequence:", len(list_sequence),
            #       ", rel_sup:", dict_fp_1s[k]/len(list_sequence))
            if dict_fp_1s[k] >= 30:
                fp_one_sequence.append(k)
        # print("频繁一序列:")
        # for w in fp_one_sequence:
        #     print("w:", w)
        # 递归扫描投影数据库中的局部频繁项，然后形成新的序列
        self.prefixspan_second_service(fp_one_sequence, list_sequence)

# ---------------------------------------------------------------------------------------

    """
    prefixspan_service_second_service
    参数：prefix_fp是前缀服务序列的队列
    参数：list_sequence是全部的服务序列的队列
    """
    def prefixspan_second_service(self, prefix_fp, list_sequence):
        if len(prefix_fp) == 0:
            print("prefix_fp是前缀服务序列的队列 is Empty")
            return
        if len(list_sequence) == 0:
            print("list_sequence是全部的服务序列的队列 is Empty")
            return
        for each_prefix_s in prefix_fp:
            # print("each_prefix_s:", each_prefix_s, ", type:", type(each_prefix_s))

            # 提取每一个的each_prefix_s后缀序列
            dict_part_fp = {}  # 用于计算局部频繁项的字典
            post_list = self.get_post_trans(tuple_item_set=(each_prefix_s,),
                                            total_elements=list_sequence)
            # print("post-list:", post_list)
            if len(post_list) != 0:
                for element in post_list:
                    de_dup_item = []  # 一个元素中去掉重复item计数的队列
                    for item in element:
                        if item not in de_dup_item:
                            de_dup_item.append(item)
                            if item in dict_part_fp.keys():
                                dict_part_fp[item] += 1
                            else:
                                dict_part_fp[item] = 1
                for c_fp in dict_part_fp.keys():
                    new_prefix_sp = [each_prefix_s]
                    if c_fp != "Stack Overflow":
                        dict_part_fp[c_fp] *= 5
                    if dict_part_fp[c_fp] >= 40:
                        new_prefix_sp.append(c_fp)
                        # print("局部频繁项：")
                        # print("c_fp:", c_fp, ", sup:", dict_part_fp[c_fp])
                        print("频繁服务序列：", self.get_no_same_item_seq(new_prefix_sp))
                        self.recur_third_post_prefix(new_prefix_sp, list_sequence)

# ---------------------------------------------------------------------------------------

    """ 递归
    recur_third_post_prefix
    参数：list_prefix
    参数：list_sequence是全部的服务序列的队列
    """
    def recur_third_post_prefix(self, list_prefix, list_sequence):
        if len(list_prefix) == 0:  # new_fp_status是tuple
            print("list_prefix is Empty")
            return
        if len(list_sequence) == 0:  # list_sequence 是队列嵌套队列
            print("list_sequence is Empty!")
            return
        # print("new_prefix_sp", list_prefix)
        dict_part_fp = {}  # 用于计算局部频繁项的字典
        # 提取后缀数据序列 post_list
        post_list = self.get_post_trans(tuple_item_set=tuple(list_prefix),
                                        total_elements=list_sequence)
        # print("post_list:", post_list)
        if len(post_list) != 0:  # 寻找局部频繁项
            for element in post_list:
                de_dup_item = []  # 一个元素中去掉重复item计数的队列
                for item in element:
                    if item not in de_dup_item:
                        de_dup_item.append(item)
                        if item in dict_part_fp.keys():
                            dict_part_fp[item] += 1
                        else:
                            dict_part_fp[item] = 1
            for c_fp in dict_part_fp.keys():
                if c_fp != "Stack Overflow":
                    dict_part_fp[c_fp] *= 5
                if dict_part_fp[c_fp] >= 40:
                    list_prefix.append(c_fp)
                    if len(list_prefix) >= 7:
                        break
                    print("频繁服务序列：", self.get_no_same_item_seq(list_prefix))
                    self.recur_third_post_prefix(list_prefix, list_sequence)


# ---------------------------------------------------------------------------------------

    """
    不重复的序列
    """
    @classmethod
    def get_no_same_item_seq(cls, list_sequence):
        total_dis_list = []
        pivot = ""
        for i in range(len(list_sequence)):
            if i == 0:
                total_dis_list.append(list_sequence[i])
                pivot = list_sequence[i]
            else:
                if list_sequence[i]:
                    if list_sequence[i] != pivot:
                        total_dis_list.append(list_sequence[i])
                        pivot = list_sequence[i]
        return total_dis_list

# ---------------------------------------------------------------------------------------

    """
    不重复的序列
    """
    @classmethod
    def get_dis_dul_sequence(cls, list_sequence):
        total_dis_list = []
        for element in list_sequence:
            temp_list = []
            for item in element:
                if item not in temp_list:
                    temp_list.append(item)
                total_dis_list.append(temp_list)
        return total_dis_list

# ---------------------------------------------------------------------------------------

    """
    获取自增1的_id,
    数据库：
    """
    def iterate_cursor_pos(self):
        # # 获取集合
        # collection = self.db.get_collection(self.uid)
        # cursors = collection.find()
        count = 0
        list_varied = []  # 存放所有变化的pos字典的队列
        list_i = []  # 存放变化的每个文档，用户提取出service
        dict_type = {}  # 第一层type存储数据结构
        list_ft = []  # 第一层频繁的type,每个元素是字典结构
        dict_dep = {}  # 第二层department存储数据结构
        list_fd = []  # 第二层频繁的department存储结构
        dict_pot = {}  # 第三城position职位的存储结构
        """第一层支持度计数"""
        for i in self.cursors_T:
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

        print("size:", self.cursors_T.count())

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

"""
类： frequent Pattern Sequence，数据对象，频繁模式的序列
"""


class FrequentP:

    def __init__(self, sequence, support):
        self.sequence = []
        self.sequence = sequence
        self.support = support
        self.cfe = 0  # 置信度

    def get_sequence(self):
        return self.sequence

    def set_sequence(self, value):
        self.sequence = value

    def get_support(self):
        return self.support

    def set_support(self, var_sup):
        self.support = var_sup

    def get_cfe(self):
        return self.cfe

    def set_cfe(self, value):
        self.cfe = value

# ----------------------------------------------------------------------------------------------------------


def main_operation():
    """Part1: 初始化参数"""
    ip_address = "127.0.0.1"  # 主机IP地址
    db_name = "varied_net"  # 读取数据库名字
    uid = "U07"  # 用户标识
    min_sup_pos = 0.4  # 数据状态varied_pos的支持度阈值
    min_sup_rel = 0.01  # 频繁变化联系relation的最小支持度
    collection_name = uid  # 读取数据集合的名字
    db_candidate_sequence = "CS"  # 存放pos候选序列
    fvs = FrequentVariedStatus(ip_address, db_name, uid, min_sup_pos,
                               min_sup_rel, collection_name)
    """Part2: 调用方法"""
    # 清空数据表格
    fvs.clear_all(db_candidate_sequence)
    # fvs.iterate_cursor_pos()  # 查找pos变化的服务序列
    dict_rel = fvs.iterate_cursor_rel()  # 查找relation频繁变化的,查找频繁变化的数据状态
    # dict_re = {"total_rel": self.total_elements, "fp_status": self.fp_status}
    fvs.fp_sequence_status(total_elements=dict_rel.get("total_rel"),
                           fp_status=dict_rel.get("fp_status"))   # 查找频繁变化的数据状态的时间序列
    fvs.printout_vts()  # 输出频繁变化的数据状态序列
    # fvs.get_fp_services()  # 寻找每个vts对应的服务序列


if __name__ == "__main__":
    # 记录算法运行开始时间
    start_time = time.clock()
    # main_operation
    main_operation()
    # 记录算法运行结束时间
    end_time = time.clock()
    print("Running time: %s Seconds" % (end_time - start_time))  # 输出运行时间(包括最后输出所有结果)
