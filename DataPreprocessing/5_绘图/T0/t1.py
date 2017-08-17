from matplotlib import pyplot as plt
import numpy as np
import matplotlib

x = np.arange(1, 120, 5)
y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
s = 300

plt.scatter(x, y, s, c="g", alpha=0.4, marker=r'.',
            label="Luck")
plt.xlabel("Leprechauns")
plt.ylabel("Gold")
plt.legend(loc=2)
plt.show()
