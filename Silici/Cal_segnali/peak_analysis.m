function [mean, sigma, err_m, err_s] = peak_analysis(file_name)

data = table2array(importfile_spe(file_name));
channel = transpose(linspace(1, length(data), length(data)));

peakfit = fit(channel, data, 'gauss1', 'Exclude', channel < 50);

mean = peakfit.b1;
sigma = peakfit.c1;

ci = confint(peakfit);
err_m = (ci(2,2)-ci(1,2)) / (2);
err_s = (ci(2,3)-ci(1,3)) / (2);

%plot(peakfit,channel,data)
%xlim([0 500])

end