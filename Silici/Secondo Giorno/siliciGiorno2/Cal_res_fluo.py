import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import find_peaks
from scipy.optimize import curve_fit

Path.cwd()

Pb= np.loadtxt('Am241_12V_180s_50micronPb82.Spe')
Mo= np.loadtxt('Am241_12V_180s_100micronMo42.Spe')
Gd1= np.loadtxt('Am241_12V_180s_120micronGd64.Spe')
Gd2= np.loadtxt('Am241_12V_180s_240micronGd64.Spe')
Sn= np.loadtxt('Am241_12V_180s_250micronSn50.Spe')
Zr= np.loadtxt('Am241_12V_180s_250micronZr40.Spe')
Am= np.loadtxt('Am241_12V_180s.Spe')
noise=np.loadtxt('rumore12V.Spe')

x=np.linspace(0,2048,2048)

plt.plot(x,noise)
plt.show()
plt.plot(x,Pb-noise)
plt.show()

plt.plot(x,Mo-noise)
plt.show()
plt.plot(x,Gd1-noise)
plt.show()
plt.plot(x,Gd2-noise)
plt.show()
plt.plot(x,Sn-noise)
plt.show()
plt.plot(x,Zr-noise)
plt.show()
plt.plot(x,Am-noise)
plt.show()
