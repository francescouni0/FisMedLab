clear all
close all
clc

data = importdata('RC_data_59V_good.txt').data;
time_diff = data(:, 1);
ampl = data(:, 2);


outlier1 = ~excludedata(time_diff,ampl,'range',[0.22 inf]);
outlier2 = ampl>((0.0004.*time_diff)+0.1);
outliers = outlier1|outlier2;
fit_func1 = @(a, b, c, x) -a*exp(-b.*x)+c;
ampl_fit = fit(time_diff, ampl, fit_func1, 'Exclude', outliers, 'Start', [0.11 0.005 10]);

figure
plot(ampl_fit, time_diff, ampl)
set(gca, 'xscale', 'log', 'yscale', 'log')
title('Rumore correlato')
xlabel('Time difference [ns]')
ylabel('Amplitude [a.u.]')
ylim([min(ampl) max(ampl)])

nbins=round(sqrt(length(time_diff)));
edges = logspace(log10(min(time_diff)), log10(max(time_diff)),nbins);
[occ,dt] = histcounts(time_diff,edges);
dt = dt(1:end-1);

fit_func2 = @(a, b, c, x) a*exp(-b*(x-c)).*x;
occ_fit = fit(transpose(dt), transpose(occ), fit_func2, 'Exclude', dt<800, 'Start', [0.1 0.00005 800]);

figure
plot(occ_fit, dt, occ)
set(gca, 'xscale', 'log', 'yscale', 'log')
title('Rumore correlato')
xlabel('Time difference [ns]')
ylabel('Occurrence')
ylim([1 1e3])
