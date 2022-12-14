import numpy as np
from scipy import optimize, signal
import matplotlib.pyplot as plt
from pathlib import Path
import time

Path.cwd()

start = time.time()

voltage = 59

if voltage == 55:
    a = 1
    b = 50
    c = 49
elif voltage == 59:
    a = 0
    b = 49
    c = 49
else:
    a = 0
    b = 50
    c = 50

waveform = []
for i in range(a, b):
    if i<10:
        waveform.append(f'C2--wf{voltage}--0000{i}.txt')
    else:
        waveform.append(f'C2--wf{voltage}--000{i}.txt')

amplitude = np.concatenate([np.loadtxt(waveform[i], skiprows=3) for i in range(0, c)])

t = [i for i in range(len(amplitude))]

first = time.time()
print(f'Import time: {first-start}')

#plt.figure()
#plt.plot(t, amplitude, 'r-')
#plt.title('Rumore correlato @55V')
#plt.xlabel('Time[ms]')
#plt.ylabel('Amplitude[a.u.]')

second = time.time()
print(f'WF plot time I: {second-first}')

if voltage == 55:
    peaks_index = signal.find_peaks(amplitude, prominence=0.02)[0]
else:
    peaks_index = signal.find_peaks(amplitude, prominence=0.15)[0]
#peaks_index = signal.find_peaks(amplitude, height=0.04)[0]
peaks_ampl = [amplitude[i] for i in peaks_index]

third = time.time()
print(f'Peak time: {third-second}')

#plt.plot(peaks_index, peaks_ampl, 'bo')

time_diff = [peaks_index[i+1]-peaks_index[i] for i in range(len(peaks_index)-1)]

#print(len(peaks_index))
#print(len(peaks_ampl))
#print(len(time_diff))

#plt.figure()
#plt.plot(time_diff, peaks_ampl[1:], 'go')
#plt.title(f'Rumore correlato @{voltage}V')
#plt.xlabel('Time[ms]')
#plt.xscale("log")
#plt.ylabel('Amplitude[mV]')
#plt.yscale("log")

if voltage == 55:
    data = np.stack((time_diff, peaks_ampl[1:]), axis=1)
    file = np.savetxt('RC_data_55V.txt', data, delimiter=' ', header='Time[ms] Peak Amplitude[mV]')
elif voltage == 57:
    data = np.stack((time_diff, peaks_ampl[1:]), axis=1)
    file = np.savetxt('RC_data_57V_2.txt', data, delimiter=' ', header='Time[ms] Peak Amplitude[mV]')
elif voltage == 58:
    data = np.stack((time_diff, peaks_ampl[1:]), axis=1)
    file = np.savetxt('RC_data_58V_2.txt', data, delimiter=' ', header='Time[ms] Peak Amplitude[mV]')
else:
    data = np.stack((time_diff, peaks_ampl[1:]), axis=1)
    file = np.savetxt('RC_data_59V_8.txt', data, delimiter=' ', header='Time[ms] Peak Amplitude[mV]')

end = time.time()
print(f'Elapsed time: {end-start}')

#plt.show()
