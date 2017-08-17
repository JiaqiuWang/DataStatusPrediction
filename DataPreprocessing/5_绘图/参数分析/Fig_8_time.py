"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt

# 划分横坐标区间
x = [0.5, 1, 1.5, 2, 2.5, 3, 3.6]
x1 = range(len(x))
x2 = range(len(x))
x3 = range(len(x))  # Make an array of x values
x4 = range(len(x))  # Make an array of y values for each x value

# 划分纵坐标区间
AP_classify = [0.84, 0.85, 0.86, 0.86, 0.85, 0.85, 0.85]
AP_CF = [0.8, 0.81, 0.82, 0.83, 0.83, 0.84, 0.83]
AP_SRP = [0.76, 0.78, 0.77, 0.77, 0.78, 0.79, 0.81]
AP_PSC = [0.82, 0.83, 0.87, 0.89, 0.91, 0.90, 0.91]


y3 = [0.57, 0.58, 0.68, 0.8, 0.82, 0.82, 0.83]  # F BETA
y4 = [0.23, 0.31, 0.42, 0.43, 0.42, 0.43, 0.43]




RAP_classify = [160, 190, 270, 312, 356, 370, 385]
RAP_CF = [150, 200, 330, 340, 350, 365, 380]
RAP_SRP = [152, 180, 312, 337, 345, 354, 367]
RAP_PSC = [189, 210, 250, 280, 289, 292, 300]


plt.plot()
plt.plot(x1, RAP_classify, '*-', label="Average(PTAN+RNN)")
plt.plot(x1, RAP_CF, 'c.-', label="Average(CFR+LHMM)")
plt.plot(x1, RAP_SRP, 'gx-', label="Average(ARP+LAB)")
plt.plot(x1, RAP_PSC, 'rs-', label="PSC")
plt.xticks(x4, x)
plt.xlabel('Data Volume(million)', fontsize=13)
plt.ylabel('Running Time(s)', fontsize=13)
plt.legend(shadow=True, fancybox=True, loc='best', numpoints=1)

plt.show()

