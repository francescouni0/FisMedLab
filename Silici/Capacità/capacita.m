%% Pulisci tutto
clear
close all

%% Calcola media e deviazione standard di ogni picco
mean = [];
sigma = [];
err_sigma = [];

[m, s, es] = peak_analysis("2.88_1k_t2.Spe");
mean = [mean m];
sigma = [sigma s];
err_sigma = [err_sigma es];

[m, s, es] = peak_analysis("2.88_1k_4.4pF.Spe");
mean = [mean m];
sigma = [sigma s];
err_sigma = [err_sigma es];

[m, s, es] = peak_analysis("2.88_1k_6.9pF.Spe");
mean = [mean m];
sigma = [sigma s];
err_sigma = [err_sigma es];

% [m, s] = peak_analysis("cav_riv_test.Spe");
% mean = [mean m];
% sigma = [sigma s];

[m, s, es] = peak_analysis("2.88_1k_11.4pF.Spe");
mean = [mean m];
sigma = [sigma s];
err_sigma = [err_sigma es];

%% CONTROLLA DATI POTREBBE MANCARE 8.6pF E UN ALTRO CAVO
C = [1 5.4 7.9 12.4]

FWHM = 2.35.*sigma;
% FWHM = [13.51 14.14 15.36 14.27]
err_FWHM = 2.35.*err_sigma;

scatter(C, FWHM, 20, "red", "filled")
% hold on
% errorbar(C, FWHM, err_FWHM, 'LineStyle', 'none', 'Color', 'black', 'CapSize', 10, )
% hold off
xlabel('Capacità[pF]')
ylabel('FWHM[a.u.]')
title('Capacitance')
grid on