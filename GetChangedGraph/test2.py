import pymongo

# 类公有变量；IP地址或者写127.0.0.1
client = pymongo.MongoClient("192.168.1.228", 27017)
# 查询数据库游标
db_name = "yanglao"
collection_name = "graphPre"
db = client.get_database(db_name)
collection = db.get_collection(collection_name)
var_cursor = collection.find_one({"_id": "1"})
print("var_cursor:", var_cursor)
if var_cursor:
    print("youzhi")
else:
    print("none")
