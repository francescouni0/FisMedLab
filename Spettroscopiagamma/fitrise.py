import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from scipy import sparse
from scipy.sparse.linalg import spsolve
import math

energy=np.array([662,31,81,356,60,1174,1332,511,1274])


RisE=np.loadtxt('risE.txt')
ErrisE=np.loadtxt('ErrisE.txt')
yerr=2.35/ErrisE

plt.xlabel('Energia',fontsize=20)
plt.ylabel('Risoluzione Energetica %',fontsize=20)
plt.errorbar(energy,RisE,yerr=yerr,fmt= 'o')
plt.show()

