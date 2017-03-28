import pymongo
# import PyV8

# 全局变量-连接指定IP地址的数据库
client = pymongo.MongoClient("127.0.0.1", 27017)
# 获取数据库
db = client.get_database("predictionData")
# 获取集合
collection = db.get_collection("counters")
c2 = db.get_collection("products")
# input_tuple = {"_id": "productid", "sequence_value": 0}
# input_tuple1 = {"_id": getNextSequenceVaule, "sequence_value": 0}

#　默认相同数据库
def get_next_counter(c_name):
    collection = db.get_collection(c_name)
    _id_obj = collection.find_and_modify(query={'_id': "productid"},
                                     update={"$inc": {"sequence_value": +1}},
                                     upsert=False,
                                     full_response=True, new=True
                                     )
    _id = _id_obj.get("value").get("sequence_value")
    print("_id:", _id)
    return _id
# print("_id:", get_next_counter("counters"))



input_tuple1 = {"_id": get_next_counter("counters"),
                "product_name": "Apple iPhone",
                "category": "mobiles"
                }


c2.insert(input_tuple1)

input_tuple2 = {"_id": get_next_counter("counters"),
                "product_name": "Samsung S3",
                "category": "phone"
                }
c2.insert(input_tuple2)
