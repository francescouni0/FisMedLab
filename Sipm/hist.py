import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import math
from scipy import optimize
from uncertainties import ufloat

Path.cwd()

data = np.loadtxt('F1--guadagnov1--00000.txt',delimiter=',')
x=data[:,0]
y=data[:,1]
print(data)

plt.plot(x,y)
plt.show()
