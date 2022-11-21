import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import LorentzianModel, QuadraticModel, GaussianModel
from scipy.optimize import leastsq, curve_fit
from pathlib import Path
from sklearn.mixture import GaussianMixture

Path.cwd()

data = np.loadtxt('F1--guadagnov1--00000.txt', delimiter=',')
x1 = data[:, 0]
y1 = data[:, 1]
#x1=x1[x1>0]
#y1=y1[72:492]
data = np.loadtxt('F1--guadagnov2--00000.txt', delimiter=',')
x2 = data[:, 0]
y2 = data[:, 1]
#x2=x2[x2>0]
#y2=y2[72:492]
data = np.loadtxt('F1--guadagnov3--00000.txt', delimiter=',')
x3 = data[:, 0]
y3 = data[:, 1]
#x3=x3[x3>0]
#y3=y3[72:492]
data = np.loadtxt('F1--guadagnov4--00000.txt', delimiter=',')
x4 = data[:, 0]
y4= data[:, 1]
#x4=x4[x4>0]
#y4=y4[72:492]
data = np.loadtxt('F1--guadagnov5--00000.txt', delimiter=',')
x5 = data[:, 0]
y5 = data[:, 1]
#x5=x5[x5>0]
#y5=y5[72:492]
data = np.loadtxt('F1--guadagnov6--00000.txt', delimiter=',')
x6 = data[:, 0]
y6 = data[:, 1]
#x6=x6[x6>0]
#y6=y6[72:492]
data = np.loadtxt('F1--guadagnov7--00000.txt', delimiter=',')
x7 = data[:, 0]
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


guess1 = [0.10e-8, 60, 2e-11,0.30e-8, 60, 2e-11,0.50e-8, 60, 2e-11,0.60e-8, 60, 2e-11,0.80e-8, 60, 2e-11,1e-8, 60, 2e-11]
guess2 = [0.10e-8, 60, 2e-11,0.30e-8, 60, 2e-11,0.50e-8, 60, 2e-11,0.60e-8, 60, 2e-11,0.80e-8, 60, 2e-11,1e-8, 60, 2e-11]
guess3 = [0.10e-8, 60, 2e-11,0.30e-8, 60, 2e-11,0.50e-8, 60, 2e-11,0.60e-8, 60, 2e-11,0.80e-8, 60, 2e-11,1e-8, 60, 2e-11]
guess4 = [0.10e-8, 60, 2e-11,0.30e-8, 60, 2e-11,0.50e-8, 60, 2e-11,0.60e-8, 60, 2e-11,0.90e-8, 60, 2e-11,1.10e-8, 60, 2e-11]
guess5 = [0.10e-8, 60, 2e-11,0.30e-8, 60, 2e-11,0.50e-8, 60, 2e-11,0.60e-8, 60, 2e-11,0.80e-8, 60, 2e-11,1e-8, 60, 2e-11]
guess6 = [0.10e-8, 60, 2e-11,0.30e-8, 60, 2e-11,0.50e-8, 60, 2e-11,0.60e-8, 60, 2e-11,0.80e-8, 60, 2e-11,1e-8, 60, 2e-11]
guess7 = [0.10e-8, 60, 2e-11,0.30e-8, 60, 2e-11,0.50e-8, 60, 2e-11,0.60e-8, 60, 2e-11,0.80e-8, 60, 2e-11,1e-8, 60, 2e-11]


popt1, pcov1 = curve_fit(func, x1, y1, p0=guess1)
popt2, pcov2 = curve_fit(func, x2, y2, p0=guess2)
popt3, pcov3 = curve_fit(func, x3, y3, p0=guess3)
popt4, pcov4 = curve_fit(func, x4, y4, p0=guess4)
popt5, pcov5 = curve_fit(func, x5, y5, p0=guess5)
popt6, pcov6 = curve_fit(func, x6, y6, p0=guess6)
popt7, pcov7 = curve_fit(func, x7, y7, p0=guess7)


print(popt1)
fit1 = func(x1, *popt1)
fit2 = func(x2, *popt2)
fit3 = func(x3, *popt3)
fit4 = func(x4, *popt4)
fit5 = func(x5, *popt5)
fit6 = func(x6, *popt6)
fit7 = func(x7, *popt7)

fig, axs = plt.subplots(2, 2)
axs[0, 0].scatter(x1, y1)
axs[0, 0].set_title('v1')
axs[0, 0].plot(x1, fit1, 'tab:orange')
axs[0, 1].scatter(x2, y2)
axs[0, 1].plot(x2, fit2,'tab:purple')
axs[0, 1].set_title('v2')
axs[1, 0].scatter(x3, y3)
axs[1, 0].plot(x3, fit3, 'tab:green')
axs[1, 0].set_title('v3')
axs[1, 1].scatter(x4, y4)
axs[1, 1].plot(x4, fit4, 'tab:red')
axs[1, 1].set_title('v4')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()