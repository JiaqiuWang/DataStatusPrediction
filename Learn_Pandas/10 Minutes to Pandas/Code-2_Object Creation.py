import numpy as np

a = np.array([2, 0, 1, 5])
print('a:', a)
print(a[:3])
print(a.min())
print(a.max())
a.sort()
print(a)
# 创建二位数据组
b = np.array([[1, 2, 3], [4, 5, 6]])
print('b:', b)
# 输出数组的平方阵
print(b*b)
