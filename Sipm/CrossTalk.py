import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import leastsq, curve_fit
from pathlib import Path
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
datatef1[:,0]= datatef1[:, 0]/75


datatef2 = np.loadtxt('counttef56.txt')
treshtef2 = datatef2[:, 0]/118
counttef2 = datatef2[:, 1]
datatef2[:,0] = datatef2[:, 0]/118


datatef3 = np.loadtxt('counttef57.txt')
treshtef3 = datatef3[:, 0]/138
counttef3 = datatef3[:, 1]
datatef3[:,0] = datatef3[:, 0]/138


datatef4 = np.loadtxt('counttef58.txt')
treshtef4 = datatef4[:, 0]/175
counttef4= datatef4[:, 1]
datatef4[:,0] = datatef4[:, 0]/175


datatef5 = np.loadtxt('counttef59.txt')
treshtef5 = datatef5[:, 0]/205
counttef5 = datatef5[:, 1]
datatef5[:,0] = datatef5[:, 0]/205

#CALCOLO BUIO
a1=np.ma.masked_greater_equal(data1[:,0], 0.5)
a2=np.ma.masked_greater_equal(data2[:,0], 0.5)
a3=np.ma.masked_greater_equal(data3[:,0], 0.5)
a4=np.ma.masked_greater_equal(data4[:,0], 0.5)
a5=np.ma.masked_greater_equal(data5[:,0], 0.5)



b1=np.ma.masked_greater_equal(data1[:,0], 1.5)
b2=np.ma.masked_greater_equal(data2[:,0], 1.5)
b3=np.ma.masked_greater_equal(data3[:,0], 1.5)
b4=np.ma.masked_greater_equal(data4[:,0], 1.5)
b5=np.ma.masked_greater_equal(data5[:,0], 1.5)



Pct1=np.mean(data1[np.ma.getmask(b1),1])/np.mean(data1[np.ma.getmask(a1),1])
Pct2=np.mean(data2[np.ma.getmask(b2),1])/np.mean(data2[np.ma.getmask(a2),1])
Pct3=np.mean(data3[np.ma.getmask(b3),1])/np.mean(data3[np.ma.getmask(a3),1])
Pct4=np.mean(data4[np.ma.getmask(b4),1])/np.mean(data4[np.ma.getmask(a4),1])
Pct5=np.mean(data5[np.ma.getmask(b5),1])/np.mean(data5[np.ma.getmask(a5),1])

print('Pct1=',Pct1)
print('Pct2=',Pct2)
print('Pct3=',Pct3)
print('Pct4=',Pct4)
print('Pct5=',Pct5)


#CALCOLO CON TEFLON


alfa1=np.ma.masked_greater_equal(datatef1[:,0], 0.5)
alfa2=np.ma.masked_greater_equal(datatef2[:,0], 0.5)
alfa3=np.ma.masked_greater_equal(datatef3[:,0], 0.5)
alfa4=np.ma.masked_greater_equal(datatef4[:,0], 0.5)
alfa5=np.ma.masked_greater_equal(datatef5[:,0], 0.5)



beta1=np.ma.masked_greater_equal(datatef1[:,0], 1.5)
beta2=np.ma.masked_greater_equal(datatef2[:,0], 1.5)
beta3=np.ma.masked_greater_equal(datatef3[:,0], 1.5)
beta4=np.ma.masked_greater_equal(datatef4[:,0], 1.5)
beta5=np.ma.masked_greater_equal(datatef5[:,0], 1.5)



Pcttef1=np.mean(datatef1[np.ma.getmask(beta1),1])/np.mean(datatef1[np.ma.getmask(alfa1),1])
Pcttef2=np.mean(datatef2[np.ma.getmask(beta2),1])/np.mean(datatef2[np.ma.getmask(alfa2),1])
Pcttef3=np.mean(datatef3[np.ma.getmask(beta3),1])/np.mean(datatef3[np.ma.getmask(alfa3),1])
Pcttef4=np.mean(datatef4[np.ma.getmask(beta4),1])/np.mean(datatef4[np.ma.getmask(alfa4),1])
Pcttef5=np.mean(datatef5[np.ma.getmask(beta5),1])/np.mean(datatef5[np.ma.getmask(alfa5),1])

print('Pcttef1=',Pcttef1)
print('Pcttef2=',Pcttef2)
print('Pcttef3=',Pcttef3)
print('Pcttef4=',Pcttef4)
print('Pcttef5=',Pcttef5)


plt.yscale('log')
plt.scatter(data1[np.ma.getmask(a1),0],data1[np.ma.getmask(a1),1])
plt.show()
