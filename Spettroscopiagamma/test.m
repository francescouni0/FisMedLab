file_name = "Ba133cal.Spe";
x1 = 430
x2 = 510
time_data = 564

data = table2array(importfile_spe(file_name));
data_norm = data./(max(data)*time_data);
noise = table2array(importfile_spe("fondo.Spe"));
noise_norm = noise./(max(noise)*92163);
spectrum = data_norm-noise_norm;
channel = linspace(1, length(data), length(data));

% figure
% plot(channel, data_norm)
% xlim([0 200])
% figure
% plot(channel, noise_norm)
% xlim([0 200])

figure
plot(channel, spectrum)
xlim([0 200])

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

peakfit = fit(transpose(index), transpose(peak), 'gauss1', );
plot(peakfit, index, peak)

mean = peakfit.b1;
sigma = peakfit.c1;