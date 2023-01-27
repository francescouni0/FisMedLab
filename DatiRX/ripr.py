import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

Path.cwd()

data = np.loadtxt('Riproducibilità.txt', skiprows=6)

D_aria, counts = np.unique(data, return_counts=True)


def FWHM(X,Y):
    half_max = max(Y) / 2.
    #find when function crosses line half_max (when sign of diff flips)
    #take the 'derivative' of signum(half_max - Y[])
    d = np.sign(half_max - np.array(Y[0:-1])) - np.sign(half_max - np.array(Y[1:]))
    #plot(X[0:len(d)],d) #if you are interested
    #find the left and right most indexes
    left_idx = np.where(d > 0)[0]
    print(left_idx)
    right_idx = np.where(d < 0)[-1]
    print(right_idx)
    return X[right_idx] - X[left_idx] #return the difference (full width)

FWHMrip=FWHM(D_aria, counts)
print('Larghezza distribuzione=',FWHMrip[1])
ErrY=D_aria*0.01+FWHMrip[1]
print(ErrY)

np.savetxt('FWHMdata.txt',FWHMrip)
# Scatter plot
plt.figure(1)
plt.scatter(D_aria, counts)

# Histogram
plt.figure(2)
plt.hist(data, bins=18)

plt.show()

