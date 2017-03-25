

# Method1
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # 将第一个值作为基准
        print("pivot:", pivot)
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        # 得到第一轮分组之后，继续讲分组进行下去
        less = quickSort(less)
        more = quickSort(more)
        print("pivotList:", pivotList)
        return less + pivotList + more


if __name__ == "__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print("original list:", a)
    print(quickSort(a))


























