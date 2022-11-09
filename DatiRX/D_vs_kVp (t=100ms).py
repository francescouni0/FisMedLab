import numpy  as np
import matplotlib.pyplot as plt
from pathlib import Path
Path.cwd()
data=np.loadtxt('D_vs_kVp (t=100ms).txt',skiprows=8)
print(np.shape(data))
kVp=data[:,0]
Dose=data[:,1]

plt.scatter(kVp, Dose)
plt.show()
