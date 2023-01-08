clear all
close all
clc

data = importdata('RC_data_59V_good.txt').data;
time_diff = data(:, 1);
ampl = data(:, 2);

fit_func1 = @(a, b, c, x) -a*exp(-b.*x)+c;
ampl_fit = fit(time_diff, ampl, fit_func1, 'Exclude', ampl>0.22, 'Start', [0.11 0.005 10]);

figure
plot(ampl_fit, time_diff, ampl)
set(gca, 'xscale', 'log', 'yscale', 'log')
title('Rumore correlato')
xlabel('Time difference [ns]')
ylabel('Amplitude [a.u.]')

nbins=round(sqrt(length(time_diff)));
edges = logspace(log10(min(time_diff)), log10(max(time_diff)),nbins);
[occ,dt] = histcounts(time_diff,edges);
dt = dt(1:end-1);

fit_func1 = @(a, b, x) a*exp(-x./b);
occ_fit = fit(transpose(dt), transpose(occ), fit_func, 'Exclude', dt<900, 'Start', [0.1 0.1]);

figure
% plot(occ_fit, dt, occ)
plot(dt, occ)
set(gca, 'xscale', 'log', 'yscale', 'log')
title('Rumore correlato')
xlabel('Time difference [ns]')
ylabel('Occurrence')
