%% Pulisci tutto
clear
close all

%% Calcola media e deviazione standard di ogni picco
mean = [];
sigma = [];

[m, s] = peak_analysis_fluo("Am241_12V_180s.Spe", 320, 360);
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis_fluo("Am241_12V_180s_120micronGd64.Spe", 220, 260);
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis_fluo("Am241_12V_180s_250micronSn50.Spe", 120, 160);
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis_fluo("Am241_12V_180s_100micronMo42.Spe", 85, 115);
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis_fluo("Am241_12V_180s_250micronZr40.Spe", 78, 102);
mean = [mean m];
sigma = [sigma s];

[m, s] = peak_analysis_fluo("Am241_12V_180s_50micronPb82.Spe", 48, 72);
mean = [mean m];
sigma = [sigma s];

%% Fit/calibrazione

energy = reshape([59.54 42.749 25.192 17.443 15.756 10.511], 6, 1);

channel = reshape(mean, 6, 1);

weight = 1./sqrt(sigma);

figure
calibr = fit(energy, channel, 'poly1', 'Weights', weight);
h2 = plot(calibr, energy, channel);
hold on
errorbar(energy, mean, sigma, "LineStyle", "none", "Color", "black");
hold off
legend( h2, 'Photon energy', 'Fit', 'Location', 'NorthWest');

xlabel( 'Energy[KeV]');
ylabel( 'Channel');
grid on