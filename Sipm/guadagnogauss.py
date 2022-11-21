import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import LorentzianModel, QuadraticModel, GaussianModel
from scipy.optimize import leastsq, curve_fit
from pathlib import Path
from sklearn.mixture import GaussianMixture

Path.cwd()

data = np.loadtxt('F1--guadagnov3--00000.txt', delimiter=',')
x = data[:, 0]
y = data[:, 1]
x=x[x>0]
y=y[72:492]

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

guess = [0.10e-8, 60, 2e-11,0.30e-8, 60, 2e-11,0.50e-8, 60, 2e-11,0.60e-8, 60, 2e-11,0.80e-8, 60, 2e-11,1e-8, 60, 2e-11]


popt, pcov = curve_fit(func, x, y, p0=guess)
print(popt)
fit = func(x, *popt)

plt.scatter(x, y)
plt.plot(x, fit , 'r-')
plt.show()