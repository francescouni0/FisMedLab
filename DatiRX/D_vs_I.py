import math

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from pathlib import Path


def fit_func(x, m, b):
    return m*x+b


Path.cwd()

Err_perc = 0.028
Err_stat = 0.4

data = np.loadtxt('D_vs_I.txt', skiprows=8)
I = data[:, 0]
Dose = data[:, 1]
sigma_D = np.sqrt(((Dose*Err_perc)**2)+(Err_stat**2))

params, cov = optimize.curve_fit(fit_func, I, Dose, sigma=sigma_D)
print(f'Model: y=m*x+b \nSlope: m={params[0]} \nIntercept: b={params[1]}')
print(f'Err_m={np.sqrt(cov[0,0])} \nErr_b={np.sqrt(cov[1,1])}')

plt.figure()
plt.plot(I, fit_func(I, *params), 'r-', label='Fit')
plt.errorbar(I, Dose, yerr=sigma_D, fmt='o', ms='3', mec='green', ecolor='black', barsabove=False, label='Dose')
plt.title('Dose vs. Tube Current')
plt.xlabel('Current[mA]')
plt.ylabel('Dose[uGy]')
plt.legend()

Dose_fit = fit_func(I, *params)
residuals = Dose - Dose_fit
plt.figure()
plt.plot(I, residuals, 'bo')
plt.title('Residuals plot')
plt.xlabel('Current[mA]')
plt.ylabel('Residual[a.u.]')

ss_res = np.sum(residuals**2)
ss_tot = np.sum((Dose-np.mean(Dose))**2)
r_squared = 1 - (ss_res / ss_tot)
print('R^2=',r_squared)

chi_squared = np.sum((residuals/sigma_D)**2)
dof = len(Dose)-len(params)
chi_reduced = chi_squared/dof
print(f'Chi Squared: {chi_squared} \nDegree of freedom: {dof} \nChi Reduced: {chi_reduced}')

plt.show()
