clear all
close all
clc

data = importdata('RC_data_55V_good.txt').data;
time_diff = data(:, 1)*0.2;
ampl = data(:, 2);

% fit_func1 = @(a, b, c, x) -a*exp(-b.*x)+c;
fit_func1 = @(a, b, x) a*(1-exp(-b.*x));
outliers = ~excludedata(time_diff,ampl,'range',[0.075 inf]);
% ampl_fit = fit(time_diff, ampl, fit_func1, 'Exclude', outliers, 'Start', [0.11 0.05 10])
ampl_fit = fit(time_diff, ampl, fit_func1, 'Exclude', outliers, 'Start', [0.11 0.01])

% figure
subplot(2,1,1)
plot(ampl_fit, time_diff, ampl)
set(gca, 'xscale', 'log', 'yscale', 'log')
xlabel('Time difference [ns]')
ylabel('Amplitude [a.u.]')
ylim([min(ampl) max(ampl)])

nbins=round(sqrt(length(time_diff)));
edges = logspace(log10(min(time_diff)), log10(max(time_diff)),nbins);
[occ,dt] = histcounts(time_diff,edges);
dt = dt(1:end-1);

fit_func2 = @(a, b, c, x) a*exp(-b*(x-c)).*x;
occ_fit = fit(transpose(dt), transpose(occ), fit_func2, 'Exclude', dt<165, 'Start', [0.1 0.001 165])

% figure
subplot(2,1,2)
plot(occ_fit, dt, occ)
set(gca, 'xscale', 'log', 'yscale', 'log')
xlabel('Time difference [ns]')
ylabel('Occurrence')
ylim([1 1e3])
sgtitle('Correlated noise, OV=2.33V')

% figure
% plot(dt, occ)
% set(gca, 'xscale', 'log', 'yscale', 'log')

a_0 = ampl_fit.a
lambda_1 = ampl_fit.b
ci = confint(ampl_fit);
err_lambda_1 = (ci(2,2)-ci(1,2))/2
err_a_0 = (ci(2,1)-ci(1,1))/2

N_0 = occ_fit.a
lambda_2 = occ_fit.b
ci = confint(occ_fit)
err_lambda_2 = (ci(2,2)-ci(1,2))/2
err_N_0 = (ci(2,1)-ci(1,1))/2

mask = dt<165;
residuals = occ(mask) - fit_func2(occ_fit.a, occ_fit.b, occ_fit.c, dt(mask));
N_rc = round(sum(residuals))
N_tot = sum(occ)
P = (N_rc/N_tot)*100

%% CT Probability
figure
scatter(time_diff, ampl, 5, "blue", "filled")
set(gca, 'xscale', 'log', 'yscale', 'log')
xlabel('Time difference [ns]')
ylabel('Amplitude [a.u.]')
ylim([min(ampl) 0.25])
yl = yline(0.1002, '-', 'Threshold');
yl.Color = [0.6350 0.0780 0.1840];
yl.LineWidth = 1;

time_diff1 = time_diff>10;
ampl1 = ampl(time_diff1);

% ampl1 = ampl1(ampl1>0.1);
ampl1 = ampl(ampl>0.1002);
N_ct = length(ampl1);
P_ct = (N_ct/N_tot)*100

roi = drawpolygon("Color", [0.4660 0.6740 0.1880], 'MarkerSize', 5, 'LineWidth', 1);
counts = inROI(roi, time_diff, ampl);
[N,edges] = histcounts(counts);
P_ct2 = (N(2)/N_tot)*100
