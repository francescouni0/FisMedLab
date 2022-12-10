import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import find_peaks
from scipy.optimize import curve_fit

Path.cwd()

s2V= np.loadtxt('sorgente2V.Spe')
s4V= np.loadtxt('sorgente4V.Spe')
s6V= np.loadtxt('sorgente6V.Spe')
s8V= np.loadtxt('sorgente8V.Spe')
s10V= np.loadtxt('sorgente10V.Spe')





x=np.linspace(0,2048,2048)


plt.plot(x,s2V)
plt.show()
plt.plot(x,s4V)
plt.show()
plt.plot(x,s6V)
plt.show()
plt.plot(x,s8V)
plt.show()
plt.plot(x,s10V)
plt.show()