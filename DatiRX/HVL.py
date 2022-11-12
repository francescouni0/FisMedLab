import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import math
from scipy import optimize
from uncertainties import ufloat

Path.cwd()

data = np.loadtxt('HVL.txt', skiprows=9)
Spessore = np.unique(data[:, 1])

Dose_40 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 40.]
Dose_52 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 52.]
Dose_64 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 64.]
Dose_76 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 76.]
Dose_88 = np.array([data[i, 2] for i in range(len(data)) if data[i, 0] == 88.])
Dose_100 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 100.]
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

x=np.linspace(0,5,10000)

Dy=np.zeros((6,5))

for i in range(Dosi.shape[0]):
    for j in range(Dosi.shape[1]):
        err=0.028

        Dy[i,j]=Dosi[i][j]*err
             
HVL=np.zeros(shape=(6,100000))
for i in range(Dosi.shape[0]):
    
    params, params_cov = optimize.curve_fit(func, Spessore, Dosi[i,:], sigma=Dy[i,:])
    print('Dose di partenza=',Dosi[i,0])
    print('mu,offset=',params)
    plt.plot(x, func(x, *params))
    plt.scatter(Spessore,Dosi[i,:])
    plt.errorbar(Spessore, Dosi[i,:],yerr=Dy[i,:],fmt="o")
    for value in x:

        if math.isclose(func(value,*params),Dosi[i,0]/2, rel_tol = Dy[i,0]/16)==True:
            HVL[i,:]=value

    hvl=HVL[i,:].mean()
    print('HVL=',hvl)
    
    






jls_extract_var = plt
jls_extract_var.title('Dose vs Filter Thickness')
plt.xlabel('Thickness[mm]')
plt.ylabel('Dose[uGy]')
plt.show()