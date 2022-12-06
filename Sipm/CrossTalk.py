import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import LorentzianModel, QuadraticModel, GaussianModel
from scipy.optimize import leastsq, curve_fit
from pathlib import Path
from scipy.integrate import simpson
from numpy import trapz
from math import isclose

Path.cwd()

data = np.loadtxt('count55.txt')
tresh1 = data[:, 0]/70
count1 = data[:, 1]

data = np.loadtxt('count56.txt')
tresh2 = data[:, 0]/70
count2 = data[:, 1]

data = np.loadtxt('count57.txt')
tresh3 = data[:, 0]/70
count3 = data[:, 1]

data = np.loadtxt('count58.txt')
tresh4 = data[:, 0]/70
count4= data[:, 1]

data = np.loadtxt('count59.txt')
tresh5 = data[:, 0]/70
count5 = data[:, 1]


data = np.loadtxt('counttef55.txt')
treshtef1 = data[:, 0]/70
counttef1 = data[:, 1]

data = np.loadtxt('counttef56.txt')
treshtef2 = data[:, 0]/70
counttef2 = data[:, 1]

data = np.loadtxt('counttef57.txt')
treshtef3 = data[:, 0]/70
counttef3 = data[:, 1]

data = np.loadtxt('counttef58.txt')
treshtef4 = data[:, 0]/70
counttef4= data[:, 1]

data = np.loadtxt('counttef59.txt')
treshtef5 = data[:, 0]/70
counttef5 = data[:, 1]

plt.yscale('log')
plt.scatter(treshtef3,counttef3)
plt.show()