import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

Path.cwd()

data = np.loadtxt('HVL.txt', skiprows=9)
print(np.shape(data))
Spessore = np.unique(data[:, 1])

Dose_40 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 40.]
Dose_52 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 52.]
Dose_64 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 64.]
Dose_76 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 76.]
Dose_88 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 88.]
Dose_100 = [data[i, 2] for i in range(len(data)) if data[i, 0] == 100.]

plt.plot(Spessore, Dose_40, 'o', color='purple', label='40kVp')
plt.plot(Spessore, Dose_52, 'o', color='blue', label='52kVp')
plt.plot(Spessore, Dose_64, 'o', color='green', label='64kVp')
plt.plot(Spessore, Dose_76, 'o', color='yellow', label='72kVp')
plt.plot(Spessore, Dose_88, 'o', color='orange', label='88kVp')
plt.plot(Spessore, Dose_100, 'o', color='red', label='100kVp')
plt.title('Dose vs Filter Thickness')
plt.xlabel('Thickness[mm]')
plt.ylabel('Dose[uGy]')
plt.legend()
plt.show()