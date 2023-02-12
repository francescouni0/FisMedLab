import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import LorentzianModel, QuadraticModel, GaussianModel
from scipy.optimize import leastsq, curve_fit
from pathlib import Path
from scipy.integrate import simpson
from numpy import trapz
from math import isclose

Path.cwd()

data = np.loadtxt('F1--guadagnov1--00000.txt', delimiter=',')
x1 = data[:, 0]*1e9
y1 = data[:, 1]
#x1=x1[x1>0]
#y1=y1[72:492]
data = np.loadtxt('F1--guadagnov2--00000.txt', delimiter=',')
x2 = data[:, 0]*1e9
y2 = data[:, 1]
#x2=x2[x2>0]
#y2=y2[72:492]
data = np.loadtxt('F1--guadagnov3--00000.txt', delimiter=',')
x3 = data[:, 0]*1e9
y3 = data[:, 1]
#x3=x3[x3>0]
#y3=y3[72:492]
data = np.loadtxt('F1--guadagnov4--00000.txt', delimiter=',')
x4 = data[:, 0]*1e9
y4= data[:, 1]
#x4=x4[x4>0]
#y4=y4[72:492]
data = np.loadtxt('F1--guadagnov5--00000.txt', delimiter=',')
x5 = data[:, 0]*1e9
y5 = data[:, 1]
#x5=x5[x5>0]
#y5=y5[72:492]
data = np.loadtxt('F1--guadagnov6--00000.txt', delimiter=',')
x6 = data[:, 0]*1e9
y6 = data[:, 1]
#x6=x6[x6>0]
#y6=y6[72:492]
data = np.loadtxt('F1--guadagnov7--00000.txt', delimiter=',')
x7 = data[:, 0]*1e9
y7 = data[:, 1]
#x7=x7[x7>0]
#y7=y7[72:492]

#plt.plot(x,y)
#plt.show()

def func(x, *params):
    y = np.zeros_like(x)
    for i in range(0, len(params), 3):
        ctr = params[i]
        amp = params[i+1]
        wid = params[i+2]
        y = y + amp * np.exp( -((x - ctr)/wid)**2)
    return y

print(x3.shape)



guess1 = [0, 60, 2e-2,2, 60, 2e-2,3, 160, 2e-2,4 ,80, 2e-2,6, 60, 2e-2,7, 60, 2e-2,7.5, 60, 2e-2,8, 60, 2e-1]
guess2 = [1.4, 60, 2e-2,2.9, 60, 2e-2,4.4, 60, 2e-2,6 ,60, 2e-2,7.5, 60, 2e-2,8.8, 60, 2e-2,10.2, 60, 2e-2,10.5, 10, 1]
guess3 = [1.5, 60, 2e-2,3.2, 60, 2e-2,5, 60, 2e-2,6.8 ,60, 2e-2,8.5,60,2e-2,10.1,60,2e-2,11, 60, 2e-2,14, 60, 2e-1]
guess4 = [1.3, 60, 2e-2,3.5, 60, 2e-2,5.4, 60, 2e-2,7.64 ,60, 2e-2,9.4, 60, 2e-2,11.5,60,2e-2,13.5, 60, 2e-2,15,60,2e-2]
guess5 = [1, 60, 2e-2,4, 60, 2e-2,6, 60, 2e-2,8 ,60, 2e-2,11, 60, 2e-2,13, 60, 2e-2,15, 60, 2e-2,16, 10, 1]
guess6 = [2.5, 100, 2e-1,5, 150, 2e-1,8, 170, 2e-1,10 ,200, 2e-1,13, 150, 2e-1,15, 100, 2e-1,18, 100, 2e-1,20, 60, 2e-1]
guess7 = [2.5, 100, 2e-1,5, 150, 2e-1,8, 170, 2e-1,10 ,200, 2e-1,13, 150, 2e-1,15, 100, 2e-1,18, 100, 2e-1,20, 60, 2e-1]




popt1, pcov1 = curve_fit(func, x1, y1, p0=guess1)

popt2, pcov2 = curve_fit(func, x2, y2, p0=guess2)
popt3, pcov3 = curve_fit(func, x3, y3, p0=guess3)
popt4, pcov4 = curve_fit(func, x4, y4, p0=guess4)
popt5, pcov5 = curve_fit(func, x5, y5, p0=guess5)
popt6, pcov6 = curve_fit(func, x6, y6, p0=guess6)
popt7, pcov7 = curve_fit(func, x7, y7, p0=guess7)


fit1 = func(x1, *popt1)
fit2 = func(x2, *popt2)
fit3 = func(x3, *popt3)
fit4 = func(x4, *popt4)
fit5 = func(x5, *popt5)
fit6 = func(x6, *popt6)
fit7 = func(x7, *popt7)


fig, axs = plt.subplots(2, 2)
axs[0, 0].scatter(x1, y1)
axs[0, 0].set_title('55V')
axs[0, 0].plot(x1, fit1, 'tab:orange')

axs[0, 1].scatter(x2, y2)
axs[0, 1].plot(x2, fit2,'tab:purple')
axs[0, 1].set_title('55.5V')
axs[1, 0].scatter(x3, y3)
axs[1, 0].plot(x3, fit3, 'tab:green')
axs[1, 0].set_title('546V')
axs[1, 1].scatter(x4, y4)
axs[1, 1].plot(x4, fit4, 'tab:red')
axs[1, 1].set_title('56.5V')

for ax in axs.flat:
    ax.set(xlabel='Area[nWb]', ylabel='Count')



fig, axs = plt.subplots(2, 2)
axs[0, 0].scatter(x5, y5)
axs[0, 0].set_title('57V')
axs[0, 0].plot(x5, fit5, 'tab:orange')

axs[0, 1].scatter(x6, y6)
axs[0, 1].plot(x6, fit6,'tab:purple')
axs[0, 1].set_title('57.5V')
axs[1, 0].scatter(x7, y7)
axs[1, 0].plot(x7, fit7, 'tab:green')
axs[1, 0].set_title('58V')

for ax in axs.flat:
    ax.set(xlabel='Area[nWb]', ylabel='Count')




plt.show()


#FIT RETTA GUADAGNO


x=np.array([1,2,3,4,5,6])

peaks=np.zeros((7,7))


popt=[]
popt=np.stack((popt1,popt2,popt3,popt4,popt5,popt6,popt7))


def func1(x,m,c):
    z=m*x+c
    return z



for j in range(7):
    for i in range(len(popt3)):

        a=i*3
        if a<18:
        
            peaks[j,i]=popt[j,a]/5000e9
            peaks[j,i]=peaks[j,i]/1.602176634e-19

Dy=np.zeros((7,7))


for j in range(7):
    for i in range(len(popt3)):

        a=(i*3)+2
        if a<23:
        
            Dy[j,i]=np.abs(popt[j,a])/5000e9
            Dy[j,i]=Dy[j,i]/1.602176634e-19
            


peaks=np.ma.masked_less(peaks, 1)
Dy=np.ma.masked_less(Dy, 0)


np.savetxt('peaks.txt',peaks)
np.savetxt('Dy.txt',Dy)


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
axs[0, 0].set_title('55V')
axs[0, 0].plot(x, func1(x,*par1), 'tab:orange')

axs[0, 1].errorbar(x, peaks[1,0:6],Dy[1,0:6], fmt="o")
axs[0, 1].plot(x, func1(x,*par2),'tab:purple')
axs[0, 1].set_title('55.5V')
axs[1, 0].errorbar(x, peaks[2,0:6],Dy[2,0:6], fmt="o")
axs[1, 0].plot(x, func1(x,*par3), 'tab:green')
axs[1, 0].set_title('56V')
axs[1, 1].errorbar(x, peaks[3,0:6],Dy[3,0:6], fmt="o")
axs[1, 1].plot(x, func1(x,*par4), 'tab:red')
axs[1, 1].set_title('56.5V')

fig, axs = plt.subplots(2, 2)
axs[0, 0].errorbar(x, peaks[4,0:6],Dy[4,0:6], fmt="o")
axs[0, 0].set_title('57V')
axs[0, 0].plot(x, func1(x,*par5), 'tab:orange')

axs[0, 1].errorbar(x, peaks[5,0:6],Dy[5,0:6], fmt="o")
axs[0, 1].plot(x, func1(x,*par6),'tab:purple')
axs[0, 1].set_title('57.5V')
axs[1, 0].errorbar(x, peaks[6,0:6],Dy[6,0:6], fmt="o")
axs[1, 0].plot(x, func1(x,*par7), 'tab:green')
axs[1, 0].set_title('58V')
for ax in axs.flat:
    ax.set(xlabel='Peak Index', ylabel='Charge/e')

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
plt.xlabel('Tensione OV [V]')
plt.ylabel('Gain')


plt.show()
print('Ov=',-parametri[1]/parametri[0])
'''
f=np.linspace(52,60)

plt.plot(f,func1(f, *parametri))




plt.show()
'''



#STIMA CAPACITÀ MICROCELLA


V_OV=np.array(V+(parametri[1]/parametri[0]))
print(V_OV)
C=[]
for l in range(7):
    C=np.append(C,(par[0+2*l:14]*1.602176634e-19)/V_OV[l])


Ccel=np.mean(C)

print(Ccel)