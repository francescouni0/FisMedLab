import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

Path.cwd()

data = np.loadtxt('HVL.txt', skiprows=9)
print(np.shape(data))
kVp = data[:, 0]
Spessore = data[:, 1]
Dose = data[:, 2]