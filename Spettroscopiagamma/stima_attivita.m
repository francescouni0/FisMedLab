% 1 pollice sono 2,54 cm
%% Pulisci tutto
clear
close all

%% Import spectrum
data = table2array(importfile_spe("Cs137_20cm.Spe"));
noise = table2array(importfile_spe("fondo.Spe"));
noise_norm = noise.*(1614/92163);
spectrum = data-noise_norm;
channel = linspace(1, length(data), length(data));

figure
subplot(2,1,1)
plot(channel, data)
xlim([0 1000])
title('Spectrum with background')
subplot(2,1,2)
plot(channel, spectrum)
xlim([0 1000])
title('Spectrum without background')

%% Remove continuum
x1 = 700;
x2 = 975;

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

figure
plot(index, peak)
xlim([x1 x2])

%% Activity (CONTROLLARE, SBALLA UN FATTORE 2)
net_counts = sum(peak);

r_in = 1.5;
r_m = r_in*0.0254
d = 0.2;
omega = 2*pi*(1-(d/sqrt(d^2+r_m^2)))

BR = 0.851;
T = 1611;
epsilon_int = 0.2;

A_mis = (net_counts/T)*(4*pi/(omega*epsilon_int*BR))

A_exp = 49967.61


