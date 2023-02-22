function [counts, err_counts] = peak_analysis_att(file_name)

data = table2array(importfile_spe(file_name));
channel = transpose(linspace(1, length(data), length(data)));

% figure
% plot(channel, data)
% xlim([200 500])

x1=320;
x2=360;

xy_A = [x1 data(x1)];
xy_B = [x2 data(x2)];

m = (xy_B(2)-xy_A(2))/(xy_B(1)-xy_A(1));
k = xy_A(2)-m*xy_A(1);
peak = [];
index = [];
for i = xy_A(1):xy_B(1)
    point = m*round(i)+k;
    peak = [peak (data(round(i))-point)];
    index = [index round(i)];
end

peakfit = fit(transpose(index), transpose(peak), 'gauss1');
% plot(peakfit, index, peak)

counts = peakfit.a1;
ci = confint(peakfit);
err_counts = (ci(2,1)-ci(1,1)) / (2);

end
