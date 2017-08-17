"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt

# 划分横坐标区间
x1 = np.linspace(0, 120)
x2 = np.linspace(0, 120)

# 划分纵坐标区间
y1 = (3.0, 2.5, 2.3, 2.6, 2.8, 3.4, 3.7, 3.5, 3.1, 3.6, 3.8,
      3.1, 3.6, 3.8, 3.7, 3.0, 3.2, 3.5, 3.6, 5.6, 3.9, 3.2,
      3.1, 3.6, 3.0, 3.5, 3.7, 3.6, 3.4, 3.1, 3.5, 3.6, 3.8,
      2.1, 3.6, 3.9, 3.5, 3.6, 3.7, 3.6, 3.2, 5.6, 3.1, 2.8,
      3.6, 3.8, 4.2, 3.9, 3.4, 3.5)  # 每个人使用的数据量
y2 = (7.6, 6.8, 6.1, 7.6, 6.9, 7.2, 8.3, 5.1, 6.1, 6.8, 7.4,
      7.1, 7.9, 7.8, 6.8, 5.1, 10.3, 12.5, 9.3, 8.4, 7.6, 7.5,
      6.1, 7.5, 7.4, 8.2, 6.4, 6.0, 6.1, 6.2, 6.3, 7.6, 7.4,
      7.2, 6.4, 8.6, 9.6, 7.5, 8.4, 7.6, 7.0, 7.2, 7.6, 7.5,
      6.4, 6.5, 7.6, 8.6, 7.4, 7.7)  # 每个用户的时间跨度

plt.subplot(2, 1, 1)
plt.plot(x1, y1, '.-')
# plt.title('A tale of 2 subplots')
# plt.xlabel('a')
plt.ylabel('Data Volume \n (Ten Thousands)', fontsize=13)

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('Each User (1~120)', fontsize=13)
plt.ylabel('Span of Time(Year)', fontsize=13)

plt.show()
