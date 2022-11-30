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

x=x[590:710]
a=[]
b=[]
a=np.append(a,Na22cal[460:490])
b=np.append(b,Na22cal[750:780])


Mi=np.sum(a)/len(a)
Mf=np.sum(b)/len(b)
F=((Mi+Mf)*440)/2

Na22net=np.sum(Na22cal[x])-F
Na22gross=np.sum(Na22cal[x])
print(Na22net)
print(Na22gross)
#PLOTTO


plt.plot(x,Na22cal[x])
#plt.scatter(pNa,Na22clean[pNa])
plt.title('Na22')
plt.show()




