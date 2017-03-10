import random
dict_edges = {}
list_var = []
count = 0
for i in range(1, 16):
    list_var.append(i)
print("list_var:", list_var)

# random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
num = random.randint(4*15, 15*(15-1)/2)
print("随机的个数：", num)
while count < num:

    slice_var = random.sample(list_var, 2)
    # print("slice:", slice_var, " TYPE:", type(slice_var))
    # print("slice[0]:", slice_var[0], ", slice[1]:", slice_var[1])
    # 如果后面的结点比前面的结点，把数字小的几点放到前面
    if slice_var[0] > slice_var[1]:
        t = slice_var[1]
        slice_var[1] = slice_var[0]
        slice_var[0] = t
    # print("slice:", slice_var)
    list_aft = []
    # 将slice放入到新的数据结构里面：pre:vi, aft:[v2, v5,...vn]
    if slice_var[0] not in dict_edges.keys():
        # 新存入字典
        list_aft.append(slice_var[1])
        dict_edges.setdefault(slice_var[0], list_aft)
    else:
        # 判断新产生的边(2, 5)的aft是不是已经存在aft队列中了，如果存在则重新执行for循环：continue
        if slice_var[1] in dict_edges[slice_var[0]]:
            continue
        else:
            # 存入老字典的键值
            dict_edges[slice_var[0]].append(slice_var[1])
            dict_edges[slice_var[0]].sort()
    print("slice:", slice_var)
    count += 1
    print("dict_edges:", dict_edges)
print("count:", count, " num:", num)

print("key_dict:", dict_edges.keys(), " type:", type(dict_edges.keys()))
transform_dict = {}
for i in dict_edges.keys():
    print("i:", i, "; type:", type(i), "value:", dict_edges[i])
    transform_dict.setdefault(str(i), dict_edges[i])
print("转换后的字典为：")
dict_edges = transform_dict.copy()
for i in dict_edges.keys():
    print("i:", i, "; type:", type(i), "value:", dict_edges[i])











