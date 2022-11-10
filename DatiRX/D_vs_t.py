import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

Path.cwd()

data = np.loadtxt('D_vs_t.txt', skiprows=8)
print(np.shape(data))
Esp = data[:, 0]
Dose = data[:, 1]

coeff = np.polyfit(Esp, Dose, 1)
print(f'y=A*x+B \nA: {coeff[0]} \nB: {coeff[1]}')
chi_squared = np.sum((np.polyval(coeff, Esp) - Dose) ** 2)
dof = len(Dose)-len(coeff)
chi_reduced = chi_squared/dof
print(f'Chi Squared: {chi_squared} \nDegree of freedom: {dof} \nChi Reduced: {chi_reduced}')

xn = np.linspace(min(Esp), max(Esp), 100)
yn = np.poly1d(coeff)
plt.plot(xn, yn(xn), '-r', Esp, Dose, 'og')
plt.title('Dose vs Time')
plt.xlabel('Time[ms]')
plt.ylabel('Dose[uGy]')
plt.show()
