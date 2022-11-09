import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

Path.cwd()

data = np.loadtxt('Riproducibilità.txt', skiprows=6)

D_aria, counts = np.unique(data, return_counts=True)

# Scatter plot
plt.figure(1)
plt.scatter(D_aria, counts)

# Istogramma
plt.figure(2)
plt.hist(data, bins=18)

plt.show()


