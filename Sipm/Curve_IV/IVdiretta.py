import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from pathlib import Path


def fit_func(x, m, b):
    return m*x+b


Path.cwd()

data = np.loadtxt('curvaIVdiretta.txt', skiprows=2)
I = -data[:-8, 1]
I_fittabile = I[7:]
V = -data[:-8, 0]
V_fittabile = V[7:]
sigma_I = [0.1 for i in range(len(I_fittabile))]

params = optimize.curve_fit(fit_func, V_fittabile, I_fittabile, sigma=sigma_I, full_output=True)[0]
print(f'Model: y=m*x+b \nSlope: m={params[0]} \nIntercept: b={params[1]}')

plt.figure()
plt.plot(V_fittabile, fit_func(V_fittabile, *params), 'r-', label='Fit')
plt.errorbar(V_fittabile, I_fittabile, yerr=sigma_I,fmt='bo', ecolor='black', barsabove=True, label='Current')
plt.title('IV Curve for direct polarization')
plt.xlabel('Voltage[V]')
plt.ylabel('Current[nA]')
plt.legend()

I_fit = fit_func(V_fittabile, *params)
residuals = I_fittabile - I_fit
plt.figure()
plt.plot(V_fittabile, residuals, 'bo')
plt.title('Residuals plot')
plt.xlabel('Voltage[V]')
plt.ylabel('Residual[a.u.]')

chi_squared = np.sum((residuals/sigma_I)**2)
dof = len(I)-len(params)
chi_reduced = chi_squared/dof
print(f'Chi Squared: {chi_squared} \nDegree of freedom: {dof} \nChi Reduced: {chi_reduced}')

N_celle = 667
R_q = (N_celle/params[0])*1e9
print(f'R_q: {R_q} ohm')

#plt.show()