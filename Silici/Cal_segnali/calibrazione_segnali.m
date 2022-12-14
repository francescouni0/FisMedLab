%% Pulisci tutto
clear
close all

%% Calcola media e deviazione standard di ogni picco
mean = [];
sigma = [];

[m, s] = peak_analysis("3.04.Spe");
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis("2.80.Spe");
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis("2.24.Spe");
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis("1.92.Spe");
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis("1.44.Spe");
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis("0.88.Spe");
mean = [mean m];
sigma = [sigma s];

%% Fit/calibrazione
e = 1.602e-19;
E_gap = 3.9;
C = 1e-12;

signal = reshape([3.04 2.80 2.24 1.92 1.44 0.88], 6, 1);
energy = reshape(signal.*(E_gap*C*1e-3/e), 6, 1);
KeV = reshape(energy.*1e-3, 6, 1);

channel = reshape(mean, 6, 1);

weight = 1./sqrt(sigma);

figure
subplot(2, 1, 1)
calibr1 = fit(signal, channel, 'poly1', 'Weights', weight)
h1 = plot(calibr1, signal, channel)
hold on
errorbar(signal, mean, sigma, "LineStyle", "none", "Color", "black");
hold off
legend( h1, 'Signal amplitude', 'Fit', 'Location', 'NorthWest');

title('Calibrazione con segnali di test');
xlabel( 'Voltage[mV]');
ylabel( 'Channel');
grid on

subplot(2, 1, 2)
calibr2 = fit(energy, channel, 'poly1', 'Weights', weight);
h2 = plot(calibr2, energy, channel)
hold on
errorbar(energy, mean, sigma, "LineStyle", "none", "Color", "black");
hold off
legend( h2, 'Simulated energy', 'Fit', 'Location', 'NorthWest');

xlabel( 'Energy[eV]');
ylabel( 'Channel');
grid on

%% Risoluzione energetica e rumore
FWHM = reshape(sqrt(8*log(2)).*sigma, 6, 1)
R = FWHM./channel

figure
subplot(2,1,1)
plot(channel, R)
title('Channel')
xlabel( 'Channel[a.u.]');
ylabel( 'dH/H');
subplot(2,1,2)
plot(channel, FWHM)
xlabel( 'Channel[a.u.]');
ylabel( 'FWHM');

FWHM1 = FWHM./calibr1.p1
R1 = FWHM1./signal

figure
subplot(2,1,1)
plot(signal, R1)
title('Signal amplitude')
xlabel( 'Voltage[mV]');
ylabel( 'dV/V');
subplot(2,1,2)
plot(signal, FWHM1)
xlabel( 'Voltage[mV]');
ylabel( 'FWHM');

FWHM2 = FWHM./calibr2.p1
R2 = FWHM2./energy

figure
subplot(2,1,1)
plot(energy, R2)
title('Simulated energy')
xlabel( 'Energy[eV]');
ylabel( 'dE/E');
subplot(2,1,2)
plot(energy, FWHM2)
xlabel( 'Energy[eV]');
ylabel( 'FWHM');


