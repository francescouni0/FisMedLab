import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import math
from scipy import optimize
Path.cwd()

data = np.loadtxt('HVL.txt', skiprows=9)
print(np.shape(data))
Spessore = np.unique(data[:, 1])

Dose_40 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 40.]
Dose_52 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 52.]
Dose_64 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 64.]
Dose_76 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 76.]
Dose_88 = np.array([data[i, 2] for i in range(len(data)) if data[i, 0] == 88.])
Dose_100 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 100.]
print(Dose_100)
'''
plt.plot(Spessore, Dose_40, 'o', color='purple', label='40kVp')
plt.plot(Spessore, Dose_52, 'o', color='blue', label='52kVp')
plt.plot(Spessore, Dose_64, 'o', color='green', label='64kVp')
plt.plot(Spessore, Dose_76, 'o', color='yellow', label='72kVp')
plt.plot(Spessore, Dose_100, 'o', color='red', label='100kVp')
'''
#PROVO FIT ESPONENZIALE
def func(x,mu,b):
    y=np.exp(-mu*x+b)
    return y

Dosi=np.array([Dose_40,Dose_52,Dose_64, Dose_76, Dose_88, Dose_100])

np.reshape(Dosi,(6,5))

x=np.linspace(0,4)
Dy=np.zeros((6,5))

for i in range(Dosi.shape[0]):
    for j in range(Dosi.shape[1]):
        err=0.01

        Dy[i,j]=Dosi[i][j]*err
        
print(Dy)
print(Dosi)
        

for i in range(Dosi.shape[0]):

    params, params_cov = optimize.curve_fit(func, Spessore, Dosi[i,:], sigma=Dy[i,:])
    print(params)
    plt.plot(x, func(x, *params))
    plt.scatter(Spessore,Dosi[i,:])
    plt.errorbar(Spessore, Dosi[i,:],yerr=Dy[i,:],fmt="o")
#plt.errorbar(Spessore, Dose_88,yerr=Dy)
#plt.plot(x,np.exp(-(1/5)*x+4.17))








jls_extract_var = plt
jls_extract_var.title('Dose vs Filter Thickness')
plt.xlabel('Thickness[mm]')
plt.ylabel('Dose[uGy]')
plt.show()