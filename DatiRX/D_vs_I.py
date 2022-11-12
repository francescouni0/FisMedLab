import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from pathlib import Path


def fit_func(x, m, b):
    return m*x+b


Path.cwd()

data = np.loadtxt('D_vs_I.txt', skiprows=8)
print(np.shape(data))
I = data[:, 0]
Dose = data[:, 1]
Dd = Dose*0.01
print(Dose.shape)
print(I.shape)

params, params_cov = optimize.curve_fit(fit_func, I, Dose, sigma=Dd)
print(params)
'''
coeff = np.polyfit(I, Dose, 1)
print(f'y=A*x+B \nA: {coeff[0]} \nB: {coeff[1]}')
chi_squared = np.sum((np.polyval(coeff, I) - Dose) ** 2)
dof = len(Dose)-len(coeff)
chi_reduced = chi_squared/dof
print(f'Chi Squared: {chi_squared} \nDegree of freedom: {dof} \nChi Reduced: {chi_reduced}')

xn = np.linspace(min(I), max(I), 100)
yn = np.poly1d(coeff)
plt.plot(xn, yn(xn), '-r', I, Dose, 'og')
'''
plt.errorbar(I, fit_func(I, *params), yerr=Dd)

plt.title('Dose vs Tube Current')
plt.xlabel('Current[mA]')
plt.ylabel('Dose[uGy]')
plt.show()
