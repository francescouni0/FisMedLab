import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from scipy import sparse
from scipy.sparse.linalg import spsolve
import math
from scipy.stats import chisquare

energy=np.array([31,60,81,356,511,662,1174,1274,1332])

def func1(x,a,b):
    z= a/np.sqrt(x)+b
    return z

def func2(x,a,b):
    z= (np.sqrt(a+b*x))/(x)
    return z

def func3(x,a,b,c):
    z= (a/x)+b+c*x 
    return z



RisE=np.loadtxt('risE.txt')
ErrisE=np.loadtxt('ErrisE.txt')
yerr=2.35/ErrisE
popt1, cov1 =curve_fit(func1,energy,RisE,[0,0],sigma=yerr) 
popt2, cov2 =curve_fit(func2,energy,RisE,[0,0],sigma=yerr) 
popt3, cov3 =curve_fit(func3,energy,RisE,[0,0,0],sigma=yerr) 


xx=np.linspace(0,1400)
plt.xlabel('Energia',fontsize=20)
plt.ylabel('Risoluzione Energetica %',fontsize=20)
plt.errorbar(energy,RisE,yerr=yerr,fmt= 'o')
plt.plot(xx,func1(xx,popt1[0],popt1[1]))
plt.show()

plt.xlabel('Energia',fontsize=20)
plt.ylabel('Risoluzione Energetica %',fontsize=20)
plt.errorbar(energy,RisE,yerr=yerr,fmt= 'o')
plt.plot(xx,func2(xx,popt2[0],popt2[1]))
plt.show()

plt.xlabel('Energia',fontsize=20)
plt.ylabel('Risoluzione Energetica %',fontsize=20)
plt.errorbar(energy,RisE,yerr=yerr,fmt= 'o')
plt.plot(xx,func3(xx,popt3[0],popt3[1],popt3[2]))
plt.show()

residuals1 = RisE- func1(energy, *popt1)
ss_res1 = np.sum(residuals1**2)
ss_tot1 = np.sum((RisE-np.mean(RisE))**2)
r_squared1 = 1 - (ss_res1 / ss_tot1)
print('R^2_1=',r_squared1)

residuals2 = RisE- func2(energy, *popt2)
ss_res2 = np.sum(residuals2**2)
ss_tot2 = np.sum((RisE-np.mean(RisE))**2)
r_squared2 = 1 - (ss_res2 / ss_tot2)
print('R^2_2=',r_squared2)


residuals3 = RisE- func3(energy, *popt3)
ss_res3 = np.sum(residuals3**2)
ss_tot3 = np.sum((RisE-np.mean(RisE))**2)
r_squared3 = 1 - (ss_res3 / ss_tot3)
print('R^2_2=',r_squared3)


