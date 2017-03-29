"""
定义自增加_id的计数器
"""
import pymongo

# 连接指定IP地址的数据库
client = pymongo.MongoClient("127.0.0.1", 27017)
# 获取数据库
db = client.get_database("data_status")
# 获取集合
ctn = db.get_collection("counters")
ctn.drop()  # 先删除集合，再插入
# 批量插入documents,插入一个数组
input_tuple = [{"_id": "U01", "no": 0}, {"_id": "U02", "no": 0},
               {"_id": "U03", "no": 0}, {"_id": "U04", "no": 0},
               {"_id": "U05", "no": 0}, {"_id": "U06", "no": 0},
               {"_id": "U07", "no": 0}, {"_id": "U08", "no": 0}
               ]
ctn.insert(input_tuple)

