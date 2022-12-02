function [mean, sigma] = peak_analysis(file_name)

data = table2array(importfile_spe(file_name));
channel = transpose(linspace(0, length(data), length(data)));

peakfit = fit(channel, data, 'gauss1', 'Exclude', channel < 50);

mean = peakfit.b1;
sigma = peakfit.c1;

plot(peakfit,channel,data)
xlim([0 500])

end