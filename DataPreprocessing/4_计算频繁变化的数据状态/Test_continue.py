
list1 = [2, 3, 5, 7]
list2 = [7, 8, 3, 2, 5, 1]

index = list2.index(1)
print("index:", index)
if index != len(list2)-1:
    print("post-list:", list2[index+1:])
else:
    print("最后一位")


# 元组转变成序列
tuple_i = (5, 4, "d", "54")
print("list:", list(tuple_i))
