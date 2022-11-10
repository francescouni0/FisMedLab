import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

Path.cwd()

data = np.loadtxt('D_vs_kVp (t=100ms).txt', skiprows=8)
print(np.shape(data))
kVp = data[:, 0]
Dose = data[:, 1]

coeff = np.polyfit(kVp, Dose, 2)
print(f'y=A*x^2+B*x+C \nA: {coeff[0]} \nB: {coeff[1]} \nC: {coeff[2]}')
chi_squared = np.sum((np.polyval(coeff, kVp) - Dose) ** 2)
dof = len(Dose)-len(coeff)
chi_reduced = chi_squared/dof
print(f'Chi Squared: {chi_squared} \nDegree of freedom: {dof} \nChi Reduced: {chi_reduced}')

xn = np.linspace(min(kVp), max(kVp), 100)
yn = np.poly1d(coeff)
plt.plot(xn, yn(xn), '-r', kVp, Dose, 'og')
plt.title('Dose vs Tube Voltage')
plt.xlabel('Voltage[kV]')
plt.ylabel('Dose[uGy]')
plt.show()
