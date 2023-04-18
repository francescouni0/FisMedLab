function [mean, sigma, mean_error] = peak_analysis_background(spectrum, x1, x2)
xy_A = [x1 spectrum(x1)];
xy_B = [x2 spectrum(x2)];

m = (xy_B(2)-xy_A(2))/(xy_B(1)-xy_A(1));
k = xy_A(2)-m*xy_A(1);
peak = [];
index = [];
for i = xy_A(1):xy_B(1)
    point = m*round(i)+k;
    peak = [peak (spectrum(round(i))-point)];
    index = [index round(i)];
end

peakfit = fit(transpose(index), transpose(peak), 'gauss1');
% figure
% plot(peakfit, index, peak)

mean = peakfit.b1;
sigma = peakfit.c1;

ci = confint(peakfit)
mean_error = (ci(2,2)-ci(1,2)) / (2);
end