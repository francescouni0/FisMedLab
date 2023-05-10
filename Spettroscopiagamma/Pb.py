import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from scipy import sparse
from scipy.sparse.linalg import spsolve
import math

Path.cwd()

Pb0 = np.loadtxt('Cs137_0mm_2.Spe')
Pb1 = np.loadtxt('Cs137_1cm.Spe')
Pb4 = np.loadtxt('Cs137_4mm.Spe')
Pb6 = np.loadtxt('Cs137_6mm.Spe')
Pb9 = np.loadtxt('Cs137_9mm.Spe')
Pb20 = np.loadtxt('Cs137_20cm.Spe')


back=np.loadtxt('fondo.Spe')

def func(b,m,a):
    z=m*b+a
    return z


def baseline_als(y, lam, p, niter=10):
  L = len(y)
  D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
  w = np.ones(L)
  for i in range(niter):
    W = sparse.spdiags(w, 0, L, L)
    Z = W + lam * D.dot(D.transpose())
    z = spsolve(Z, w*y)
    w = p * (y > z) + (1-p) * (y < z)
  return z

def FWHM(X,Y):
    half_max = max(Y) / 2.
    #find when function crosses line half_max (when sign of diff flips)
    #take the 'derivative' of signum(half_max - Y[])
    d = np.sign(half_max - np.array(Y[0:-1])) - np.sign(half_max - np.array(Y[1:]))
    #plot(X[0:len(d)],d) #if you are interested
    #find the left and right most indexes
    left_idx = np.where(d > 0)[0]
    right_idx = np.where(d < 0)[-1]
    return X[right_idx] - X[left_idx] #return the difference (full width)

x=np.linspace(0,2048,2048,dtype=int)

Pb0base=baseline_als(Pb0, 1e5, 0.001)
Pb1base=baseline_als(Pb1, 1e5, 0.001)
Pb4base=baseline_als(Pb4, 1e5, 0.001)
Pb6base=baseline_als(Pb6, 1e5, 0.001)
Pb9base=baseline_als(Pb9, 1e5, 0.001)
Pb20base=baseline_als(Pb20, 1e5, 0.001)



Pb0clean=Pb0-Pb0base
Pb1clean=Pb1-Pb1base
Pb4clean=(Pb4-Pb4base)*1.12
Pb6clean=Pb6-Pb6base
Pb9clean=Pb9-Pb9base
Pb20clean=(Pb20-Pb20base)*0.445

#CALCOLO RMSE
MSE=np.square(np.subtract(Pb0,Pb0clean)).mean()
rsme0=math.sqrt(MSE)
print("Root Mean Square Error:\n")
print(rsme0)

#CALCOLO NET AREA
Pb0net=np.sum(Pb0clean[750:910])
Pb1net=np.sum(Pb1clean[810:910])
Pb4net=np.sum(Pb4clean[770:910])
Pb6net=np.sum(Pb6clean[800:910])
Pb9net=np.sum(Pb9clean[800:910])
Pb20net=np.sum(Pb20clean[720:910])

Net=np.array([Pb0net, Pb4net,Pb6net,Pb9net,Pb1net])/Pb0net

print(Pb0net)
print(Pb1net)
print(Pb4net)
print(Pb6net)
print(Pb9net)
print(Pb20net)

#SIGMA

Pb0FWHM=FWHM(x,Pb0clean[650:1000])
#print(f'Pb0sigma: {Pb0FWHM}')
Pb1FWHM=FWHM(x,Pb1clean[650:1000])
#print(f'Pb1sigma: {Pb1FWHM}')
Pb4FWHM=FWHM(x,Pb4clean[650:1000])
#print(f'Pb4sigma: {Pb4FWHM}')
Pb6FWHM=FWHM(x,Pb6clean[650:1000])
#print(f'Pb6sigma: {Pb6FWHM}')
Pb9FWHM=FWHM(x,Pb9clean[650:1000])
#print(f'Pb9sigma: {Pb9FWHM}')
Pb20FWHM=FWHM(x,Pb20clean[650:1000])
#print(f'Pb20sigma: {Pb20FWHM}')

F=np.array([np.sqrt(Pb0net)+rsme0,np.sqrt(Pb4net)+rsme0,np.sqrt(Pb6net)+rsme0,np.sqrt(Pb9net)+rsme0,np.sqrt(Pb1net)+rsme0])

Sigma=np.absolute(F/Pb0net)
print(F)

'''
ig, axs = plt.subplots(2, 2)
axs[0, 0].set_title('Pb0')
axs[0,0].plot(x,Pb0clean,'tab:orange')

axs[0, 1].plot(x,Pb1clean)

axs[0, 1].set_title('Pb1')
axs[1, 0].plot(x,Pb4clean,'tab:red')

axs[1, 0].set_title('Pb4')
axs[1, 1].plot(x,Pb6clean,'tab:green')

axs[1, 1].set_title('Pb6')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')


plt.show()

plt.plot(x,Pb9clean,'m')
plt.title('Pb9')
plt.show()
fig= plt.plot(x,Pb20clean)
plt.title('Pb20')
plt.show()
'''
#FIT RETTA


l=np.array([0,4,6,9,10])
popt, cov =curve_fit(func, l, np.log(Net),sigma=Sigma) # fit(channel, energy)



print(np.sqrt(cov))
print('Results', popt)

#TEST R^2

residuals = np.log(Net)- func(l, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((np.log(Net)-np.mean(np.log(Net)))**2)
r_squared = 1 - (ss_res / ss_tot)
print('R^2=',r_squared)




plt.errorbar(l, Net,yerr=Sigma, fmt='o')
plt.title('ciao')
plt.show()

plt.xlabel('Spessori[mm]',fontsize=20)
plt.ylabel('log(I/I0) %',fontsize=20)
plt.errorbar(l, np.log(Net),yerr=Sigma, fmt='o')


plt.plot(l, func(l,popt[0],popt[1]))
plt.show()
