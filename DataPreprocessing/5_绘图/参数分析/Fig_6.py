"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt

# 划分横坐标区间
x = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
x1 = range(len(x))
x2 = range(len(x))
x3 = range(len(x))  # Make an array of x values
x4 = range(len(x))  # Make an array of y values for each x value

# 划分纵坐标区间
y1 = [0.53, 0.55, 0.68, 0.86, 0.88, 0.87, 0.90]  # AP
y2 = [0.83, 0.81, 0.75, 0.69, 0.68, 0.66, 0.67]  # AR
y3 = [0.57, 0.58, 0.68, 0.8, 0.82, 0.82, 0.83]  # F BETA
y4 = [0.23, 0.31, 0.42, 0.43, 0.42, 0.43, 0.43]

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
plt.xlabel('$min\_sup$', fontsize=13)
plt.ylabel('$F_{β}$', fontsize=13)

plt.subplot(2, 2, 4)
plt.plot(x4, y4, '.-')
plt.xticks(x4, x)
plt.xlabel('$min\_sup$', fontsize=13)
plt.ylabel('$RAP$', fontsize=13)

plt.show()

