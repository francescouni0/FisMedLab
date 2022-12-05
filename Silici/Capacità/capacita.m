%% Pulisci tutto
clear
close all

%% Calcola media e deviazione standard di ogni picco
mean = [];
sigma = [];

[m, s] = peak_analysis("2.88_1k.Spe");
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis("2.88_1k_4.4pF.Spe");
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis("2.88_1k_6.9pF.Spe");
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis("cav_riv_test.Spe");
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis("2.88_1k_11.4pF.Spe");
mean = [mean m];
sigma = [sigma s];

%% CONTROLLA DATI POTREBBE MANCARE 8.6pF E UN ALTRO CAVO
C = [1 5.4 7.9 9.6 12.4]

sigmac = sigma./C

scatter(C, sigma)