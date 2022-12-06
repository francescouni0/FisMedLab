import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import LorentzianModel, QuadraticModel, GaussianModel
from scipy.optimize import leastsq, curve_fit
from pathlib import Path
from scipy.integrate import simpson
from numpy import trapz
from math import isclose

Path.cwd()

data1 = np.loadtxt('count55.txt')
tresh1 = data1[:, 0]/75
count1 = data1[:, 1]
data1[:,0]= data1[:, 0]/75

data2 = np.loadtxt('count56.txt')
tresh2 = data2[:, 0]/118
count2 = data2[:, 1]
data2[:,0] = data2[:, 0]/118

data3 = np.loadtxt('count57.txt')
tresh3 = data3[:, 0]/138
count3 = data3[:, 1]
data3[:,0] = data3[:, 0]/138

data4 = np.loadtxt('count58.txt')
tresh4 = data4[:, 0]/175
count4= data4[:, 1]
data4[:,0] = data4[:, 0]/175


data5 = np.loadtxt('count59.txt')
tresh5 = data5[:, 0]/205
count5 = data5[:, 1]
data5[:,0] = data5[:, 0]/205



datatef1 = np.loadtxt('counttef55.txt')
treshtef1 = datatef1[:, 0]/75
counttef1 = datatef1[:, 1]

datatef2 = np.loadtxt('counttef56.txt')
treshtef2 = datatef2[:, 0]/118
counttef2 = datatef2[:, 1]

datatef3 = np.loadtxt('counttef57.txt')
treshtef3 = datatef3[:, 0]/138
counttef3 = datatef3[:, 1]

datatef4 = np.loadtxt('counttef58.txt')
treshtef4 = datatef4[:, 0]/175
counttef4= datatef4[:, 1]

datatef5 = np.loadtxt('counttef59.txt')
treshtef5 = datatef5[:, 0]/205
counttef5 = datatef5[:, 1]

a1=np.ma.masked_less_equal(data1[:,0], 0.5)
a2=np.ma.masked_less_equal(data2[:,0], 0.5)
a3=np.ma.masked_less_equal(data3[:,0], 0.5)
a4=np.ma.masked_less_equal(data4[:,0], 0.5)
a5=np.ma.masked_less_equal(data5[:,0], 0.5)

b1=np.ma.masked_greater_equal(data1[:,0], 0.5)
b2=np.ma.masked_greater_equal(data2[:,0], 0.5)
b3=np.ma.masked_greater_equal(data3[:,0], 0.5)
b4=np.ma.masked_greater_equal(data4[:,0], 0.5)
b5=np.ma.masked_greater_equal(data5[:,0], 0.5)

c1=np.ma.masked_greater_equal(b1, 1.5)
c2=np.ma.masked_greater_equal(b2, 1.5)
c3=np.ma.masked_greater_equal(b3, 1.5)
c4=np.ma.masked_greater_equal(b4, 1.5)
c5=np.ma.masked_greater_equal(b5, 1.5)

Pct1=np.mean(data1[np.ma.getmask(c1),1])/np.mean(data1[np.ma.getmask(a1),1])
Pct2=np.mean(data2[np.ma.getmask(c2),1])/np.mean(data2[np.ma.getmask(a2),1])
Pct3=np.mean(data3[np.ma.getmask(c3),1])/np.mean(data3[np.ma.getmask(a3),1])
Pct4=np.mean(data4[np.ma.getmask(c4),1])/np.mean(data4[np.ma.getmask(a4),1])
Pct5=np.mean(data5[np.ma.getmask(c5),1])/np.mean(data5[np.ma.getmask(a5),1])

print('Pct1=',Pct1)
print('Pct2=',Pct2)
print('Pct3=',Pct3)
print('Pct4=',Pct4)
print('Pct5=',Pct5)


plt.yscale('log')
plt.scatter(data1[np.ma.getmask(a1),0],data1[np.ma.getmask(a1),1])
plt.show()