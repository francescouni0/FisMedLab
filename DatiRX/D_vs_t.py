import numpy  as np
import matplotlib.pyplot as plt
from pathlib import Path
Path.cwd()
data=np.loadtxt('D_vs_t.txt',skiprows=8)
print(np.shape(data))
Esp=data[:,0]
Dose=data[:,1]

plt.scatter(Esp, Dose)
plt.show()


