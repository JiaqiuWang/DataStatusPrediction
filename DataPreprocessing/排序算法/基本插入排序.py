
def insert_sort(ary):
    n = len(ary)
    for i in range(1, n):
        if ary[i] < ary[i-1]:
            temp = ary[i]
            index = i  # 待插入的下标
            for j in range(i-1, -1, -1):  # 从i-1循环到0(包括0)
                if ary[j] > temp:
                    ary[j+1] = ary[j]
                    index = j  # 记录待插入下标
                else:
                    break
            ary[index] = temp
    return ary


print(insert_sort([3, 5, 2, 1, 10, 35, 26, 96, 14, 0, 21]))












