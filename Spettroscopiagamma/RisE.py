import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from scipy import sparse
from scipy.sparse.linalg import spsolve

Path.cwd()

Cs137cal = np.loadtxt('Cs137cal2.Spe')
Ba133cal = np.loadtxt('Ba133cal.Spe')
Am241cal = np.loadtxt('Am241cal.Spe')
Co60cal = np.loadtxt('Co60cal.Spe')
Na22cal = np.loadtxt('Na22cal.Spe')

back=np.loadtxt('fondo.Spe')


x=np.linspace(0,2048,2048,dtype=int)


#TROVO PICCHI
pCs, _ =find_peaks(Cs137cal,prominence=0.00004)
pAm, _ =find_peaks(Am241cal,prominence=0.00004)
pNa, _ =find_peaks(Na22cal,prominence=0.00004)
pCo, _ =find_peaks(Co60cal,prominence=0.00004)
pBa, _ =find_peaks(Ba133cal,prominence=0.00004)
ppCs=pCs[7]
ppBa1=pBa[1]
ppBa2=pBa[2]
ppBa3=pBa[3]
ppAm=pAm[3]
ppCo1=pCo[5]
ppCo2=pCo[6]
ppNa1=pNa[1]
ppNa2=pNa[2]
y=[662,31,81,356,60,1174,1332,511,1274]




#ALGORITMO PER ELIMINARE IL CONTINUM

c=x[590:710]
a=[]
b=[]
a=np.append(a,Na22cal[460:490])
b=np.append(b,Na22cal[750:780])


Mi=np.sum(a)/len(a)
Mf=np.sum(b)/len(b)
F=((Mi+Mf)*440)/2

Na22net=np.sum(Na22cal[c])-F
Na22gross=np.sum(Na22cal[c])
print(Na22net)
print(Na22gross)



#MULTILEASTSQUARED ESKERE



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

Na22base=baseline_als(Na22cal, 1e5, 0.001)
print(Na22base)
Co60base=baseline_als(Co60cal, 1e5, 0.001)
Ba133base=baseline_als(Ba133cal, 1e5, 0.001)
Am241base=baseline_als(Am241cal, 1e5, 0.001)
Cs137base=baseline_als(Cs137cal, 1e5, 0.001)


Na22net1=np.sum(Na22cal[c]-Na22base[c])
print(Na22net1)
'''
Co60net2=np.sum(Co60cal[c]-Co60base[c])
Ba133net3=np.sum(Ba133cal[c]-Ba133base[c])
Cs137net4=np.sum(Cs137cal[c]-Cs137base[c])
Am241net5=np.sum(Am241cal[c]-Am241base[c])
'''
#PLOTTO



fig, axs = plt.subplots(2, 2)
axs[0, 0].set_title('Cs137')
axs[0,0].plot(x,Cs137cal)
axs[0,0].plot(x,Cs137cal-Cs137base,'tab:orange')

axs[0, 1].plot(x,Ba133cal-Ba133base,'-m')
axs[0,1].plot(x,Ba133cal)

axs[0, 1].set_title('Ba133')
axs[1, 0].plot(x,Am241cal-Am241base,'tab:red')
axs[1,0].plot(x,Am241cal)

axs[1, 0].set_title('Am241')
axs[1, 1].plot(x,Co60cal-Co60base,'tab:green')
axs[1,1].plot(x,Co60cal)

axs[1, 1].set_title('Co60')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')


plt.show()


plt.plot(x,Na22cal-Na22base,'tab:pink')
plt.plot(x,Na22cal)
plt.title('Na22')
plt.show()



