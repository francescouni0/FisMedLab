import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
Path.cwd()
data = np.loadtxt('Riproducibilità.txt', skiprows=6)

D_aria, counts = np.unique(data, return_counts=True)


plt.figure(1)

plt.scatter(D_aria, counts)
plt.figure(2)
# oppure istogramma

plt.hist(data, bins=18)
plt.show()


