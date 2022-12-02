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

signal = []

weight = 1./sqrt(sigma);

peakfit = fit(channel, data, 'gauss1', 'Exclude', channel < 50);
