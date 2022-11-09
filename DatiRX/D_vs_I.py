import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
Path.cwd()
data = np.loadtxt('D_vs_I.txt', skiprows=8)
print(np.shape(data))
I = data[:, 0]
Dose = data[:, 1]

plt.scatter(I, Dose)
plt.show()
