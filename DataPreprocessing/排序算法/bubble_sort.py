
def bubble_sort(arry):
    n = len(arry)                   # 获得数组的长度
    for i in range(n):
        print("i:", i)
        for j in range(1, n-i):
            print("j:", j)
            if arry[j-1] > arry[j]:       # 如果前者比后者大
                print("if- arry[j-1]:", arry[j-1], " > ", arry[j])
                arry[j-1], arry[j] = arry[j], arry[j-1]      # 则交换两者
        print("list:", arry)
    return arry


print(bubble_sort([3, 5, 2, 1, 10, 35, 26, 96, 14, 0, 21]))










