"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt

# 划分横坐标区间
x = [6, 12, 18, 24, 36, 48, 72, 96, 168]
x1 = range(len(x))
x2 = range(len(x))
x3 = range(len(x))  # Make an array of x values
x4 = range(len(x))  # Make an array of y values for each x value

# 划分纵坐标区间
y1 = [0.53, 0.67, 0.71, 0.75, 0.89, 0.90, 0.90, 0.91, 0.88]  # 每个人使用的数据量
y2 = [0.80, 0.75, 0.73, 0.72, 0.72, 0.71, 0.69, 0.61, 0.58]
y3 = [0.57, 0.68, 0.71, 0.74, 0.85, 0.85, 0.84, 0.83, 0.8]
y4 = [0.20, 0.31, 0.43, 0.45, 0.52, 0.51, 0.53, 0.52, 0.51]

plt.subplot(2, 2, 1)
plt.plot(x1, y1, '.-')
plt.xticks(x1, x)
# plt.title('A tale of 2 subplots')
# plt.xlabel('a')
plt.ylabel('$AP$', fontsize=13)

plt.subplot(2, 2, 2)
plt.plot(x2, y2, '.-')
plt.xticks(x2, x)
# plt.xlabel('tv')
plt.ylabel('$AR$', fontsize=13)

plt.subplot(2, 2, 3)
plt.plot(x3, y3, '.-')
plt.xticks(x3, x)
plt.xlabel('$tv$ (Hours)', fontsize=13)
plt.ylabel('$F_{β}$', fontsize=13)

plt.subplot(2, 2, 4)
plt.plot(x4, y4, '.-')
plt.xticks(x4, x)
plt.xlabel('$tv$ (Hours)', fontsize=13)
plt.ylabel('$RAP$', fontsize=13)

plt.show()

