import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([1, 8, 10])
ypoint = np.array([3, 10, 5])

plt.figure(figsize=(5, 5))
plt.plot(xpoint, ypoint, color='red')
plt.xlim([0, 15])
plt.ylim([0, 15])
plt.show()
