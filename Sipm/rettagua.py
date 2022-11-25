import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import LorentzianModel, QuadraticModel, GaussianModel
from scipy.optimize import leastsq, curve_fit
from pathlib import Path
from scipy.integrate import simpson
from scipy.stats import linregress
from numpy import trapz

Path.cwd()
peaks = np.loadtxt('peaks.txt')
Dy = np.loadtxt('Dy.txt')

x=np.array([1,2,3,4,5,6])

def func1(x,m,c):
    y=m*x+c
    return y


par1, cov1 = curve_fit(func1, x, peaks[0,0:6], p0=(3e5,-6e5),sigma=Dy[0,0:6])
par2, cov2 = curve_fit(func1, x, peaks[1,0:6], p0=(1e13,-1e5),sigma=Dy[1,0:6])
par3, cov3 = curve_fit(func1, x, peaks[2,0:6], p0=(1.7e6,-1e5),sigma=Dy[2,0:6])
par4, cov4 = curve_fit(func1, x, peaks[3,0:6], p0=(2e6,1e5),sigma=Dy[3,0:6])
par5, cov5 = curve_fit(func1, x, peaks[4,0:6], p0=(3e6,-1e5),sigma=Dy[4,0:6])
par6, cov6 = curve_fit(func1, x, peaks[5,0:6], p0=(3e6,-5e5),sigma=Dy[5,0:6])
par7, cov7 = curve_fit(func1, x, peaks[6,0:6], p0=(3e6,-1e5),sigma=Dy[6,0:6])


print('par1=',par1)
print('par2=',par2)
print('par3=',par3)
print('par4=',par4)
print('par5=',par5)
print('par6=',par6)
print('par7=',par7)



fig, axs = plt.subplots(2, 2)
axs[0, 0].errorbar(x, peaks[0,0:6],Dy[0,0:6], fmt="o")
axs[0, 0].set_title('v1')
axs[0, 0].plot(x, func1(x,*par1), 'tab:orange')

axs[0, 1].errorbar(x, peaks[1,0:6],Dy[1,0:6], fmt="o")
axs[0, 1].plot(x, func1(x,*par2),'tab:purple')
axs[0, 1].set_title('v2')
axs[1, 0].errorbar(x, peaks[2,0:6],Dy[2,0:6], fmt="o")
axs[1, 0].plot(x, func1(x,*par3), 'tab:green')
axs[1, 0].set_title('v3')
axs[1, 1].errorbar(x, peaks[3,0:6],Dy[3,0:6], fmt="o")
axs[1, 1].plot(x, func1(x,*par4), 'tab:red')
axs[1, 1].set_title('v4')

fig, axs = plt.subplots(2, 2)
axs[0, 0].errorbar(x, peaks[4,0:6],Dy[4,0:6], fmt="o")
axs[0, 0].set_title('v5')
axs[0, 0].plot(x, func1(x,*par5), 'tab:orange')

axs[0, 1].errorbar(x, peaks[5,0:6],Dy[5,0:6], fmt="o")
axs[0, 1].plot(x, func1(x,*par6),'tab:purple')
axs[0, 1].set_title('v6')
axs[1, 0].errorbar(x, peaks[6,0:6],Dy[6,0:6], fmt="o")
axs[1, 0].plot(x, func1(x,*par7), 'tab:green')
axs[1, 0].set_title('v7')


plt.show()


#FIT GUADAGNO OVERVOLTAGE

V=np.array([55,55.5,56,56.5,57,57.5,58])
par=[]
par=np.stack((par1,par2,par3,par4,par5,par6,par7))
sig=[]
sig=np.stack((np.sqrt(cov1[0,0]),np.sqrt(cov2[0,0]),np.sqrt(cov3[0,0]),np.sqrt(cov4[0,0]),np.sqrt(cov5[0,0]),np.sqrt(cov6[0,0]),np.sqrt(cov7[0,0])))
gain=np.zeros(7)

for j in range(7):
        gain[j]=par[j,0]
            

parametri, covarianza = curve_fit(func1, V, gain, p0=(100000,0),sigma=sig)
print('guadagno=',parametri)
print(np.sqrt(covarianza[0,0]))

plt.errorbar(V, gain,yerr=np.sqrt(covarianza[0,0]),fmt="o")
plt.plot(V,func1(V,*parametri))


plt.show()
