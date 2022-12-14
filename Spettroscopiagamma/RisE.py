import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from scipy import sparse
from scipy.sparse.linalg import spsolve
import math

Path.cwd()

Cs137cal = np.loadtxt('Cs137cal2.Spe')
Ba133cal = np.loadtxt('Ba133cal.Spe')
Am241cal = np.loadtxt('Am241cal.Spe')
Co60cal = np.loadtxt('Co60cal.Spe')
Na22cal = np.loadtxt('Na22cal.Spe')

back=np.loadtxt('fondo.Spe')


x=np.linspace(0,2048,2048,dtype=int)


# PICCHI

ppCs=840
ppBa1=47
ppBa2=118
ppBa3=468
ppAm=90
ppCo1=1458
ppCo2=1650
ppNa1=661
ppNa2=1570

pp=np.array([ppCs,ppBa1,ppBa2,ppBa3,ppAm,ppCo1,ppCo2,ppNa1,ppNa2])
y=[662,31,81,356,60,1174,1332,511,1274]




#ALGORITMO SCEMO PER ELIMINARE IL CONTINUM

c=x[590:710]
a=[]
b=[]
a=np.append(a,Na22cal[460:490])
b=np.append(b,Na22cal[750:780])


Mi=np.sum(a)/len(a)
Mf=np.sum(b)/len(b)
F=((Mi+Mf)*440)/2

Na22net_=np.sum(Na22cal[c])-F
Na22gross=np.sum(Na22cal[c])




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

#CALCOLO BASELINE
Na22base=baseline_als(Na22cal, 1e5, 0.001)
Co60base=baseline_als(Co60cal, 1e5, 0.001)
Ba133base=baseline_als(Ba133cal, 1e5, 0.001)
Am241base=baseline_als(Am241cal, 1e5, 0.001)
Cs137base=baseline_als(Cs137cal, 1e5, 0.001)

#CALCOLO NET AREA
Na22net1=np.sum(Na22cal[c]-Na22base[c])
Na22net2=np.sum(Na22cal[1475:1655]-Na22base[1475:1655])

Co60net1=np.sum(Co60cal[1355:1550]-Co60base[1355:1550])
Co60net2=np.sum(Co60cal[1550:1755]-Co60base[1550:1755])

Ba133net1=np.sum(Ba133cal[25:65]-Ba133base[25:65])
Ba133net2=np.sum(Ba133cal[95:135]-Ba133base[95:135])
Ba133net3=np.sum(Ba133cal[427:515]-Ba133base[427:515])

Cs137net=np.sum(Cs137cal[750:910]-Cs137base[750:910])
Am241net=np.sum(Am241cal[60:105]-Am241base[60:105])

#TROVO FWHM

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


Na22FWHM1=FWHM(x,Na22cal[c]-Na22base[c])
print(f'I sigma Na22: {Na22FWHM1/2.335}')
Na22FWHM2=FWHM(x,Na22cal[1475:1655]-Na22base[1475:1655])
print(f'II sigma Na22: {Na22FWHM2[3]/2.335}')

Co60FWHM1=FWHM(x,Co60cal[1355:1550]-Co60base[1355:1550])
print(f'I sigma Co60: {Co60FWHM1[1]/2.335}')
Co60FWHM2=FWHM(x,Co60cal[1550:1755]-Co60base[1550:1755])
print(f'II sigma Co60: {Co60FWHM2/2.335}')

Ba133FWHM1=FWHM(x,Ba133cal[25:65]-Ba133base[25:65])
print(f'I sigma Ba133: {Ba133FWHM1/2.335}')
Ba133FWHM2=FWHM(x,Ba133cal[95:135]-Ba133base[95:135])
print(f'II sigma Ba133: {Ba133FWHM2/2.335}')
Ba133FWHM3=FWHM(x,Ba133cal[427:515]-Ba133base[427:515])
print(f'III sigma Ba133: {Ba133FWHM3/2.335}')

Cs137FWHM=FWHM(x,Cs137cal[750:910]-Cs137base[750:910])
print(f'sigma Cs137: {Cs137FWHM/2.335}')

Am241FWHM=FWHM(x,Am241cal[60:105]-Am241base[60:105])
print(f'sigma Am241: {Am241FWHM/2.335}')



#RISOLUZIONE ENERGETICA INGENUA
RisE=np.array([(Cs137FWHM/ppCs)*100,(Ba133FWHM1/ppBa1)*100,(Ba133FWHM2/ppBa2)*100,(Ba133FWHM3/ppBa3)*100,(Am241FWHM/ppAm)*100,(Co60FWHM1[1]/ppCo1)*100,(Co60FWHM2/ppCo2),(Na22FWHM1/ppNa1)*100,(Na22FWHM2[3]/ppNa2)*100])

print('RisENa1:',(Na22FWHM1/ppNa1)*100)

print('RisENa2:',(Na22FWHM2[3]/ppNa2)*100)
print('RisECo1:',(Co60FWHM1[1]/ppCo1)*100)
print('RisECo2:',(Co60FWHM2/ppCo2)*100)

print('RisECs:',(Cs137FWHM/ppCs)*100)
print('RisEAm:',(Am241FWHM/ppAm)*100)

np.savetxt('risE.txt',RisE)


#PROVIAMO MEGLIO TENENDO CONTRO DEGLI ELETTRONI GENERATI DAI FOTOTUBI

FNa1=(Na22FWHM1)/np.sqrt(np.sum(Na22cal[c]-Na22base[c]))
FNa2=(Na22FWHM2[3])/np.sqrt(np.sum(Na22cal[1475:1655]-Na22base[1475:1655]))
FCo1=(Co60FWHM1[1])/np.sqrt(np.sum(Co60cal[1355:1550]-Co60base[1355:1550]))
FCo2=(Co60FWHM2)/np.sqrt(np.sum(Co60cal[1550:1755]-Co60base[1550:1755]))
FCs=(Cs137FWHM)/np.sqrt(np.sum(Cs137cal[750:910]-Cs137base[750:910]))
FAm=(Am241FWHM)/np.sqrt(np.sum(Am241cal[60:105]-Am241base[60:105]))


#PLOTTO
xen=(x*0.81718445)-17.68967536
plt.scatter(xen[pp],RisE)

plt.show()
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



