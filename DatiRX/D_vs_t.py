import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from pathlib import Path


def fit_func(x, m, b):
    return m*x+b


Path.cwd()

Err_perc = 0.028

data = np.loadtxt('D_vs_t.txt', skiprows=8)
Esp = data[:, 0]
Dose = data[:, 1]
sigma_D = Dose*Err_perc

params = optimize.curve_fit(fit_func, Esp, Dose, sigma=sigma_D, full_output=True)[0]
print(f'Model: y=m*x+b \nSlope: m={params[0]} \nIntercept: b={params[1]}')

plt.figure()
plt.plot(Esp, fit_func(Esp, *params), 'r-', label='Fit')
plt.errorbar(Esp, Dose, yerr=sigma_D, fmt='none', ecolor='black', barsabove=True, label='Dose')
plt.title('Dose vs Time')
plt.xlabel('Time[ms]')
plt.ylabel('Dose[uGy]')

Dose_fit = fit_func(Esp, *params)
residuals = Dose - Dose_fit
plt.figure()
plt.plot(Esp, residuals, 'bo')
plt.title('Residuals plot')
plt.xlabel('Time[mA]')
plt.ylabel('Residual[a.u.]')

chi_squared = np.sum((residuals/sigma_D)**2)
dof = len(Dose)-len(params)
chi_reduced = chi_squared/dof
print(f'Chi Squared: {chi_squared} \nDegree of freedom: {dof} \nChi Reduced: {chi_reduced}')

plt.show()
