import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import find_peaks
from scipy.optimize import curve_fit

Path.cwd()

y_88 = np.loadtxt('0.88.Spe')




x=np.linspace(0,2048,2048)


plt.plot(x,y_88)
plt.show()