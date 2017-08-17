"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt

# 划分横坐标区间
x1 = np.linspace(0, 120)
# x2 = np.linspace(0, 120)

# 划分纵坐标区间
y1 = (8,  10, 9, 8, 8, 7, 17, 8, 9, 7, 8,
      8, 11, 9, 12, 8, 9, 10, 12, 15, 6, 8,
      10, 10, 8, 7, 9, 8, 11, 7, 8, 8, 8,
      9, 9, 7, 8, 9, 10, 8, 8, 10, 11, 9,
      9, 8, 8, 9, 10, 13)  # 每个人使用的数据量


plt.plot(x1, y1, '.-')
# plt.title('A tale of 2 subplots')
plt.xlabel('Each User', fontsize=13)
plt.ylabel('Number of \n Distinct Services', fontsize=13)

plt.show()
