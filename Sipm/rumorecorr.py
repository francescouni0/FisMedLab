import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from pathlib import Path

Path.cwd()

data = np.loadtxt('C2--wf55--00001.txt', skiprows=3)
for i in range(10):
    print(data[i])