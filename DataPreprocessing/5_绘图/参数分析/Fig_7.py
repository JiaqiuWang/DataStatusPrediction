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

plt.subplot(2, 2, 1)
plt.plot(x1, AP_classify, '*-', label="Average(PTAN+RNN)")
plt.plot(x1, AP_CF, 'c.-')
plt.plot(x1, AP_SRP, 'gx-')
plt.plot(x1, AP_PSC, 'rs-')
plt.legend(shadow=False, fancybox=True, loc='best', numpoints=1)
plt.xticks(x1, x)
# plt.title('A tale of 2 subplots')
# plt.xlabel('a')
plt.ylabel('$AP$', fontsize=13)

# ------------------------------------------------------------------------

AR_classify = [0.75, 0.75, 0.74, 0.72, 0.70, 0.68, 0.65]
AR_CF = [0.79, 0.75, 0.74, 0.73, 0.73, 0.72, 0.70]
AR_SRP = [0.78, 0.77, 0.76, 0.72, 0.70, 0.68, 0.68]
AR_PSC = [0.82, 0.81, 0.79, 0.75, 0.75, 0.73, 0.72]
# [0.83, 0.81, 0.75, 0.69, 0.68, 0.66, 0.67]


plt.subplot(2, 2, 2)
plt.plot(x1, AR_classify, '*-')
plt.plot(x1, AR_CF, 'c.-', label="Average(CFR+LHMM)")
plt.plot(x1, AR_SRP, 'gx-')
plt.plot(x1, AR_PSC, 'rs-')
plt.legend(shadow=False, fancybox=True, loc='best', numpoints=1)
plt.xticks(x2, x)
# plt.xlabel('tv')
plt.ylabel('$AR$', fontsize=13)

# -----------------------------------------------------

F_classify = [0.82, 0.83, 0.82, 0.83, 0.81, 0.81, 0.8]
F_CF = [0.79, 0.80, 0.8, 0.81, 0.81, 0.81, 0.80]
F_SRP = [0.73, 0.75, 0.77, 0.77, 0.76, 0.77, 0.78]
F_PSC = [0.82, 0.83, 0.85, 0.86, 0.87, 0.86, 0.86]

plt.subplot(2, 2, 3)
plt.plot(x1, F_classify, '*-')
plt.plot(x1, F_CF, 'c.-')
plt.plot(x1, F_SRP, 'gx-', label="Average(ARP+LAB)")
plt.plot(x1, F_PSC, 'rs-')
plt.xticks(x3, x)
plt.xlabel('Data Volume(million)', fontsize=13)
plt.ylabel('$F_{β}$', fontsize=13)
plt.legend(shadow=False, fancybox=True, loc='best', numpoints=1)


#--------------------------------------------------------------------------


RAP_classify = [0.47, 0.48, 0.48, 0.49, 0.48, 0.47, 0.47]
RAP_CF = [0.43, 0.44, 0.45, 0.46, 0.45, 0.46, 0.46]
RAP_SRP = [0.45, 0.45, 0.44, 0.45, 0.44, 0.45, 0.46]
RAP_PSC = [0.53, 0.55, 0.54, 0.52, 0.52, 0.53, 0.54]


plt.subplot(2, 2, 4)
plt.plot(x1, RAP_classify, '*-')
plt.plot(x1, RAP_CF, 'c.-')
plt.plot(x1, RAP_SRP, 'gx-', )
plt.plot(x1, RAP_PSC, 'rs-', label="PSC")
plt.xticks(x4, x)
plt.xlabel('Data Volume(million)', fontsize=13)
plt.ylabel('$RAP$', fontsize=13)
plt.legend(shadow=False, fancybox=True, loc='best', numpoints=1)

plt.show()

