%% Pulisci tutto
clear
close all

%% Calcola media e deviazione standard di ogni picco
mean = [];
sigma = [];
error_mean = [];
error_sigma = [];

[m, s, em, es] = peak_analysis("3.04.Spe");
mean = [mean m];
sigma = [sigma s];
error_mean = [error_mean em];
error_sigma = [error_sigma es];

[m, s, em, es] = peak_analysis("2.80.Spe");
mean = [mean m];
sigma = [sigma s];
error_mean = [error_mean em];
error_sigma = [error_sigma es];

[m, s, em, es] = peak_analysis("2.24.Spe");
mean = [mean m];
sigma = [sigma s];
error_mean = [error_mean em];
error_sigma = [error_sigma es];

[m, s, em, es] = peak_analysis("1.92.Spe");
mean = [mean m];
sigma = [sigma s];
error_mean = [error_mean em];
error_sigma = [error_sigma es];

[m, s, em, es] = peak_analysis("1.44.Spe");
mean = [mean m];
sigma = [sigma s];
error_mean = [error_mean em];
error_sigma = [error_sigma es];

[m, s, em, es] = peak_analysis("0.88.Spe");
mean = [mean m];
sigma = [sigma s];
error_mean = [error_mean em];
error_sigma = [error_sigma es];

%% Fit/calibrazione
e = 1.602e-19;
E_gap = 3.6;
C = 1e-12;

signal = reshape([3.04 2.80 2.24 1.92 1.44 0.88], 6, 1);
energy = reshape(signal.*(E_gap*C*1e-3/e), 6, 1);
KeV = reshape(energy.*1e-3, 6, 1);

channel = reshape(mean, 6, 1);

err_dV = [1.28 1.28 1.28 1.28 1.2 1.2];
weight1 = 1./sqrt(err_dV);
err_E = err_dV.*(E_gap*C*1e-3/e);
weight2 = 1./sqrt(err_E);

figure
subplot(2, 1, 1)
% calibr1 = fit(signal, channel, 'poly1', 'Weights', weight)
[calibr1, gof1] = fit(channel, signal, 'poly1', 'Weights', weight1)
h1 = plot(calibr1, channel, signal);
hold on
errorbar(channel, signal, err_dV, "LineStyle", "none", "Color", "black");
hold off
legend( h1, 'Signal amplitude', 'Fit', 'Location', 'NorthWest');

title('Calibrazione con segnali di test');
ylabel( 'Voltage[mV]');
xlabel( 'Channel[a.u.]');
grid on

subplot(2, 1, 2)
[calibr2, gof2] = fit(channel, energy, 'poly1', 'Weights', weight2)
h2 = plot(calibr2, channel, energy);
hold on
errorbar(channel, energy, err_E, "LineStyle", "none", "Color", "black");
hold off
legend( h2, 'Simulated energy', 'Fit', 'Location', 'NorthWest');

ylabel( 'Energy[eV]');
xlabel( 'Channel[a.u.]');
grid on

%% Risoluzione energetica e rumore
% FWHM = reshape(sqrt(8*log(2)).*sigma, 6, 1)
FWHM = reshape(2.35.*sigma, 6, 1)
error_FWHM = 2.35.*error_sigma;
R = FWHM./channel
error_R = reshape([0.0001 0.0001 0.00008 0.00004 0.00003 0.00003], 6, 1)
weight3 = 1./sqrt(error_R);

fit_func = @(a, x) a./x;
[res_fit, gof3] = fit(KeV, R, fit_func, "Weights", weight3)
h3 = plot(res_fit, KeV, R);
hold on
scatter(KeV, R, 10, "blue", "filled")
hold off
title('Resolution R')
xlabel( 'Energy[keV]');
% xlim([min(KeV) max(KeV)])
xlim([15 70])
ylabel( 'R');
legend( h3, 'Resolution', 'Fit', 'Location', 'NorthEast');

% figure
% subplot(2,1,1)
% plot(channel, R)
% title('Resolution R')
% xlabel( 'Channel[a.u.]');
% ylabel( 'R');
% subplot(2,1,2)
% plot(channel, FWHM)
% xlabel( 'Channel[a.u.]');
% ylabel( 'FWHM');
% 
% FWHM1 = FWHM./calibr1.p1
% R1 = FWHM1./signal
% 
% figure
% subplot(2,1,1)
% plot(signal, R1)
% title('Signal amplitude')
% xlabel( 'Voltage[mV]');
% ylabel( 'dV/V');
% subplot(2,1,2)
% plot(signal, FWHM1)
% xlabel( 'Voltage[mV]');
% ylabel( 'FWHM');
% 
% FWHM2 = FWHM./calibr2.p1
% R2 = FWHM2./energy
% 
% figure
% subplot(2,1,1)
% plot(energy, R2)
% title('Simulated energy')
% xlabel( 'Energy[eV]');
% ylabel( 'dE/E');
% subplot(2,1,2)
% plot(energy, FWHM2)
% xlabel( 'Energy[eV]');
% ylabel( 'FWHM');


