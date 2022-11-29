import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path

Path.cwd()

Cs137cal = np.loadtxt('Cs137cal2.Spe')
Ba133cal = np.loadtxt('Ba133cal.Spe')
Am241cal = np.loadtxt('Am241cal.Spe')
Co60cal = np.loadtxt('Co60cal.Spe')
Na22cal = np.loadtxt('Na22cal.Spe')

back=np.loadtxt('Cs137cal2.Spe')


x=np.linspace(0,2048,2048)

#NORMALIZZO TUTTO
Cs137cal_norm= Cs137cal / np.max(Cs137cal)
Ba133cal_norm= Ba133cal / np.max(Ba133cal)
Co60cal_norm= Co60cal / np.max(Co60cal)
Am241cal_norm= Am241cal / np.max(Am241cal)
Na22cal_norm= Na22cal / np.max(Na22cal)

back_norm= back / np.max(back)

Cs137clean=Cs137cal_norm-back_norm
Am241clean=Am241cal_norm-back_norm
Co60clean=Co60cal_norm-back_norm
Ba133clean=Ba133cal_norm-back_norm



#PLOTTO

fig, axs = plt.subplots(2, 2)
axs[0, 0].set_title('Cs137')
axs[0,0].plot(x,Cs137cal_norm,'tab:orange')

axs[0, 1].plot(x,Ba133cal_norm)
axs[0, 1].set_title('Ba133')
axs[1, 0].plot(x,Am241cal_norm,'tab:red')
axs[1, 0].set_title('Am241')
axs[1, 1].plot(x,Co60cal_norm,'tab:green')

axs[1, 1].set_title('Co60')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')


plt.show()


plt.plot(x,Na22cal_norm,'m')
plt.title('Na22')
plt.show()
fig= plt.plot(x,back_norm)
plt.title('Background')
plt.show()




