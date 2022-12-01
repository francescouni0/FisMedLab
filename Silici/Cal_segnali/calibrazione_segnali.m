clear
close all

mean = [];
sigma = [];

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

weight = 1./sqrt(sigma);

peakfit = fit(channel, data, 'gauss1', 'Exclude', channel < 50);
