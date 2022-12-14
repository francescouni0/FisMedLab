function [mean, sigma] = peak_analysis_fluo(file_name, x1, x2)

data = table2array(importfile_spe(file_name));
noise = table2array(importfile_spe("rumore12V.Spe"));
spectrum = data-noise;
channel = transpose(linspace(1, length(data), length(data)));

% figure
% semilogy(channel,data)
% title('Raw data')
% xlim([0 500])
% 
% figure
% semilogy(channel,noise)
% title('Noise')
% xlim([0 500])

% fig = figure;
% semilogy(channel,spectrum)
% title('Spectrum')
% xlim([0 500])

% datacursormode on
% pointA = datacursormode(fig);
% disp('Click line to display a data tip, then press "Return"')
% pause 
% xy_A = getCursorInfo(pointA).Position;
% pointB = datacursormode(fig);
% disp('Click line to display a data tip, then press "Return"')
% pause 
% xy_B = getCursorInfo(pointB).Position;

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
% plot(peakfit, index, peak)

mean = peakfit.b1;
sigma = peakfit.c1;

end