clear all
close all
clc

data = importdata('RC_data_58V_good.txt').data;
time_diff = data(:, 1)*0.2;
ampl = data(:, 2);


outlier1 = ~excludedata(time_diff,ampl,'range',[0.175 inf]);
outlier2 = ampl>((0.00187414.*time_diff)+0.0825);
outliers = outlier1|outlier2;
% fit_func1 = @(a, b, c, x) -a*exp(-b.*x)+c;
% ampl_fit = fit(time_diff, ampl, fit_func1, 'Exclude', outliers, 'Start', [0.11 0.005 10])
fit_func1 = @(a, b, x) a*(1-exp(-b.*x));
ampl_fit = fit(time_diff, ampl, fit_func1, 'Exclude', outliers, 'Start', [0.11 0.04])

% figure
% scatter(time_diff, ampl, 3, 'filled')
% hold on
% plot(time_diff, ((0.00187414.*time_diff)+0.0825))
% hold off

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
occ_fit = fit(transpose(dt), transpose(occ), fit_func2, 'Exclude', dt<165, 'Start', [0.1 0.00005 165])

% figure
subplot(2,1,2)
plot(occ_fit, dt, occ)
set(gca, 'xscale', 'log', 'yscale', 'log')
xlabel('Time difference [ns]')
ylabel('Occurrence')
ylim([1 1e3])
sgtitle('Correlated noise, OV=5.33V')

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
ylim([min(ampl) 0.4])
yl1 = yline(0.245, '-', 'First Threshold');
yl2 = yline(0.20, '-', 'Second Threshold');
yl1.Color = [0.6350 0.0780 0.1840];
yl1.LineWidth = 1;
yl2.Color = [0.6350 0.0780 0.1840];
yl2.LineWidth = 1;
yl1.LabelHorizontalAlignment = "left";
yl2.LabelHorizontalAlignment = "left";

time_diff1 = time_diff<1e2;
time_diff2 = time_diff>1e2;
ampl1 = ampl(time_diff1);
ampl2 = ampl(time_diff2);

ampl1 = ampl1(ampl1>0.245);
ampl2 = ampl2(ampl2>0.20);
N_ct = length(ampl1)+length(ampl2);
P_ct = (N_ct/N_tot)*100

roi = drawpolygon("Color", [0.4660 0.6740 0.1880], 'MarkerSize', 3, 'LineWidth', 1);
counts = inROI(roi, time_diff, ampl);
[N,edges] = histcounts(counts);
P_ct2 = (N(2)/N_tot)*100
