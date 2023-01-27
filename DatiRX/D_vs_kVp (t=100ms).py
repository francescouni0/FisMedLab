import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from pathlib import Path


def fit_func(x, a, b, c):
    return a*x**2+b*x+c


Path.cwd()

Err_perc = 0.028
Err_stat = 0.4

data = np.loadtxt('D_vs_kVp (t=100ms).txt', skiprows=8)
kVp = data[:, 0]
Dose = data[:, 1]
sigma_D = np.sqrt(((Dose*Err_perc)**2)+(Err_stat**2))

params, cov = optimize.curve_fit(fit_func, kVp, Dose, sigma=sigma_D)
print(f'Model: y=a*x^2+b*x+c \na={params[0]} \nb={params[1]} \nc={params[2]}')
print(f'Err_a={np.sqrt(cov[0,0])} \nErr_b={np.sqrt(cov[1,1])} \nErr_c={np.sqrt(cov[2,2])}')

plt.figure()
plt.plot(kVp, fit_func(kVp, *params), 'r-', label='Fit')
plt.errorbar(kVp, Dose, yerr=sigma_D, fmt='o', ms='3', mec='green', ecolor='black', barsabove=False, label='Dose')
plt.title('Dose vs. Tube Voltage')
plt.xlabel('Voltage[kV]')
plt.ylabel('Dose[uGy]')
plt.legend()

Dose_fit = fit_func(kVp, *params)
residuals = Dose - Dose_fit
plt.figure()
plt.plot(kVp, residuals, 'bo')
plt.title('Residuals plot')
plt.xlabel('Voltage[kV]')
plt.ylabel('Residual[a.u.]')

chi_squared = np.sum((residuals/sigma_D)**2)
dof = len(Dose)-len(params)
chi_reduced = chi_squared/dof
print(f'Chi Squared: {chi_squared} \nDegree of freedom: {dof} \nChi Reduced: {chi_reduced}')

plt.show()
