import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import find_peaks
from scipy.optimize import curve_fit

Path.cwd()

Cs137cal = np.loadtxt('Cs137cal2.Spe')
Ba133cal = np.loadtxt('Ba133cal.Spe')
Am241cal = np.loadtxt('Am241cal.Spe')
Co60cal = np.loadtxt('Co60cal.Spe')
Na22cal = np.loadtxt('Na22cal.Spe')

back=np.loadtxt('fondo.Spe')


x=np.linspace(0,2048,2048)

#NORMALIZZO TUTTO
Cs137cal_norm= Cs137cal / (np.max(Cs137cal)*770)
Ba133cal_norm= Ba133cal /( np.max(Ba133cal)*564)
Co60cal_norm= Co60cal / (np.max(Co60cal)*2230)
Am241cal_norm= Am241cal / (np.max(Am241cal)*102)
Na22cal_norm= Na22cal / (np.max(Na22cal)*2063)

back_norm= back / (np.max(back)*92163)

Cs137clean=Cs137cal_norm-back_norm
Am241clean=Am241cal_norm-back_norm
Co60clean=Co60cal_norm-back_norm
Ba133clean=Ba133cal_norm-back_norm
Na22clean=Na22cal_norm-back_norm
#TROVO PICCHI
pCs, _ =find_peaks(Cs137clean,prominence=0.00004)
pAm, _ =find_peaks(Am241clean,prominence=0.00004)
pNa, _ =find_peaks(Na22clean,prominence=0.00004)
pCo, _ =find_peaks(Co60clean,prominence=0.00004)
pBa, _ =find_peaks(Ba133clean,prominence=0.00004)
#SELEZIONO FOTOPICCHI (indici dello stesso elemento hanno energia consegcutiva)
ppCs=pCs[7]
ppBa1=pBa[1]
ppBa2=pBa[2]
ppBa3=pBa[3]
ppAm=pAm[3]
ppCo1=pCo[5]
ppCo2=pCo[6]
ppNa1=pNa[1]
ppNa2=pNa[2]
print('Cs:',ppCs)
print('Ba:' ,ppBa1,ppBa2,ppBa3)
print('Na:' ,ppNa1,ppNa2)
print('Co:' ,ppCo1,ppCo2)
print('Am:' ,ppAm)

#FITTO RETTA CALIBRAZIONE

def func(b,m,a):
    z=m*b +a 
    return z

pp=np.array([ppCs,ppBa1,ppBa2,ppBa3,ppAm,ppCo1,ppCo2,ppNa1,ppNa2])


y=[662,31,81,356,60,1174,1332,511,1274]


popt, cov =curve_fit(func, pp, y)

print(popt)
plt.plot(pp,func(pp,popt[0],popt[1]))



plt.scatter(pp,y)
plt.show()

#PLOTTO

fig, axs = plt.subplots(2, 2)
axs[0, 0].set_title('Cs137')
axs[0,0].scatter(pCs,Cs137clean[pCs])
axs[0,0].plot(x,Cs137clean,'tab:orange')

axs[0, 1].plot(x,Ba133clean)
axs[0,1].scatter(pBa,Ba133clean[pBa])

axs[0, 1].set_title('Ba133')
axs[1, 0].plot(x,Am241clean,'tab:red')
axs[1,0].scatter(pAm,Am241clean[pAm])

axs[1, 0].set_title('Am241')
axs[1, 1].plot(x,Co60clean,'tab:green')
axs[1,1].scatter(pCo,Co60clean[pCo])

axs[1, 1].set_title('Co60')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')


plt.show()


plt.plot(x,Na22clean,'m')
plt.scatter(pNa,Na22clean[pNa])
plt.title('Na22')
plt.show()
fig= plt.plot(x,back_norm)
plt.title('Background')
plt.show()




