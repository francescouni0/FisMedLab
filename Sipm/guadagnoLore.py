import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import LorentzianModel, QuadraticModel, GaussianModel
from scipy.optimize import leastsq
from pathlib import Path

Path.cwd()

data = np.loadtxt('F1--guadagnov3--00000.txt', delimiter=',')
xdat = data[:, 0]
ydat = data[:, 1]


def add_peak(prefix, center,amplitude=100, sigma=3e-10):
    
    peak = LorentzianModel(prefix=prefix)
    pars = peak.make_params()
    pars[prefix + 'center'].set(center)
    pars[prefix + 'amplitude'].set(amplitude)
    pars[prefix + 'sigma'].set(sigma, min=0)
    return peak, pars

model = LorentzianModel(prefix='bkg_')
params = model.make_params(a=0, b=0, c=0)

rough_peak_positions = (0.10e-8, 0.30e-8, 0.50e-8, 0.60e-8, 0.80e-8, 1e-8)
for i, cen in enumerate(rough_peak_positions):
    peak, pars = add_peak('lz%d_' % (i+1), cen)
    model = model + peak
    params.update(pars)

init = model.eval(params, x=xdat)
result = model.fit(ydat, params, x=xdat)
comps = result.eval_components()

print(result.fit_report(min_correl=0.5))

plt.scatter(xdat, ydat, label='data')
plt.plot(xdat, result.best_fit, label='best fit')


plt.show()