%% Pulisci tutto
clear
close all

%% Inizialization
file_name = ["Am241cal.Spe" "Na22cal.Spe" "Cs137cal2.Spe" "Co60cal.Spe" "Ba133cal.Spe"];
time_data = [102 2063 770 2230 564];

noise = table2array(importfile_spe("fondo.Spe"));
noise_norm = noise./(max(noise)*92163);

channel = linspace(1, 2048, 2048);
energy = (channel.*0.8093598329870725)-10.902148156778575;

%% Am241
i = 1;
data = table2array(importfile_spe(file_name(i)));
data_norm = data./(max(data)*time_data(i));

spectrum = data_norm-noise_norm;

figure
subplot(2,1,1)
plot(energy, spectrum, 'k', ...
    energy(45:60), spectrum(45:60), 'g', ...
    energy(75:110), spectrum(75:110), 'r', ...
    'LineWidth', 1)
xlim([0 100])

hold on
s1 = scatter(energy(90), spectrum(90), 1)
s2 = scatter(energy(45), spectrum(45), 1)
hold off

dt1 = datatip(s1);
s1.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s1.DataTipTemplate.DataTipRows(2).Label = 'Photopeak';
s1.DataTipTemplate.DataTipRows(2).Value = '';
s1.DataTipTemplate.DataTipRows(3).Label = '';
s1.DataTipTemplate.DataTipRows(3).Value = '';
dt2 = datatip(s2);
s2.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s2.DataTipTemplate.DataTipRows(2).Label = 'Compton edge';
s2.DataTipTemplate.DataTipRows(2).Value = '';
s2.DataTipTemplate.DataTipRows(3).Label = '';
s2.DataTipTemplate.DataTipRows(3).Value = '';

subplot(2,1,2)
semilogy(energy, spectrum, 'k', ...
    energy(45:60), spectrum(45:60), 'g', ...
    energy(75:110), spectrum(75:110), 'r', ...
    'LineWidth', 1)
xlim([0 100])
sgtitle('Spectrum of Am241') 

%% Na22
i = 2;
data = table2array(importfile_spe(file_name(i)));
data_norm = data./(max(data)*time_data(i));

spectrum = data_norm-noise_norm;

figure
subplot(2,1,1)
plot(energy, spectrum, 'k', ...
    energy(70:160), spectrum(70:160), 'b', ...
    energy(380:520), spectrum(380:520), 'g', ...
    energy(575:725), spectrum(575:725), 'c', ...
    energy(1240:1400), spectrum(1240:1400), 'g', ...
    energy(1485:1675), spectrum(1485:1675), 'r', ...
    'LineWidth', 1)
xlim([0 1600])

hold on
s1 = scatter(energy(114), spectrum(114), 1)
s2 = scatter(energy(380), spectrum(380), 1)
s3 = scatter(energy(661), spectrum(661), 1)
s4 = scatter(energy(1240), spectrum(1240), 1)
s5 = scatter(energy(1570), spectrum(1570), 1)
hold off

dt1 = datatip(s1);
s1.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s1.DataTipTemplate.DataTipRows(2).Label = 'Pb K-line';
s1.DataTipTemplate.DataTipRows(2).Value = '';
s1.DataTipTemplate.DataTipRows(3).Label = '';
s1.DataTipTemplate.DataTipRows(3).Value = '';
dt2 = datatip(s2);
s2.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s2.DataTipTemplate.DataTipRows(2).Label = 'Compton edge';
s2.DataTipTemplate.DataTipRows(2).Value = '';
s2.DataTipTemplate.DataTipRows(3).Label = '';
s2.DataTipTemplate.DataTipRows(3).Value = '';
dt3 = datatip(s3);
s3.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s3.DataTipTemplate.DataTipRows(2).Label = 'Annihilation peak';
s3.DataTipTemplate.DataTipRows(2).Value = '';
s3.DataTipTemplate.DataTipRows(3).Label = '';
s3.DataTipTemplate.DataTipRows(3).Value = '';
dt4 = datatip(s4);
s4.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s4.DataTipTemplate.DataTipRows(2).Label = 'Compton edge';
s4.DataTipTemplate.DataTipRows(2).Value = '';
s4.DataTipTemplate.DataTipRows(3).Label = '';
s4.DataTipTemplate.DataTipRows(3).Value = '';
dt5 = datatip(s5);
s5.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s5.DataTipTemplate.DataTipRows(2).Label = 'Compton edge';
s5.DataTipTemplate.DataTipRows(2).Value = '';
s5.DataTipTemplate.DataTipRows(3).Label = '';
s5.DataTipTemplate.DataTipRows(3).Value = '';

subplot(2,1,2)
semilogy(energy, spectrum, 'k', ...
    energy(70:160), spectrum(70:160), 'b', ...
    energy(380:520), spectrum(380:520), 'g', ...
    energy(575:725), spectrum(575:725), 'c', ...
    energy(1240:1400), spectrum(1240:1400), 'g', ...
    energy(1485:1675), spectrum(1485:1675), 'r', ...
    'LineWidth', 1)
xlim([0 1600])
sgtitle('Spectrum of Na22') 

%% Cs137
i = 3;
data = table2array(importfile_spe(file_name(i)));
data_norm = data./(max(data)*time_data(i));

spectrum = data_norm-noise_norm;

figure
subplot(2,1,1)
plot(energy, spectrum, 'k', ...
    energy(35:70), spectrum(35:70), 'b', ...
    energy(225:305), spectrum(225:305), 'c', ...
    energy(555:650), spectrum(555:650), 'g', ...
    energy(755:915), spectrum(755:915), 'r', ...
    'LineWidth', 1)
xlim([0 800])

hold on
s1 = scatter(energy(50), spectrum(50), 1)
s2 = scatter(energy(262), spectrum(262), 1)
s3 = scatter(energy(555), spectrum(555), 1)
s4 = scatter(energy(840), spectrum(840), 1)
hold off

dt1 = datatip(s1);
s1.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s1.DataTipTemplate.DataTipRows(2).Label = 'Ba K-line';
s1.DataTipTemplate.DataTipRows(2).Value = '';
s1.DataTipTemplate.DataTipRows(3).Label = '';
s1.DataTipTemplate.DataTipRows(3).Value = '';
dt2 = datatip(s2);
s2.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s2.DataTipTemplate.DataTipRows(2).Label = 'Backscatter peak';
s2.DataTipTemplate.DataTipRows(2).Value = '';
s2.DataTipTemplate.DataTipRows(3).Label = '';
s2.DataTipTemplate.DataTipRows(3).Value = '';
dt3 = datatip(s3);
s3.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s3.DataTipTemplate.DataTipRows(2).Label = 'Compton edge';
s3.DataTipTemplate.DataTipRows(2).Value = '';
s3.DataTipTemplate.DataTipRows(3).Label = '';
s3.DataTipTemplate.DataTipRows(3).Value = '';
dt4 = datatip(s4);
s4.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s4.DataTipTemplate.DataTipRows(2).Label = 'Photopeak';
s4.DataTipTemplate.DataTipRows(2).Value = '';
s4.DataTipTemplate.DataTipRows(3).Label = '';
s4.DataTipTemplate.DataTipRows(3).Value = '';

subplot(2,1,2)
semilogy(energy, spectrum, 'k', ...
    energy(35:70), spectrum(35:70), 'b', ...
    energy(225:305), spectrum(225:305), 'c', ...
    energy(555:650), spectrum(555:650), 'g', ...
    energy(755:915), spectrum(755:915), 'r', ...
    'LineWidth', 1)
xlim([0 800])
sgtitle('Spectrum of Cs137') 

%% Co60
i = 4;
data = table2array(importfile_spe(file_name(i)));
data_norm = data./(max(data)*time_data(i));

spectrum = data_norm-noise_norm;

figure
subplot(2,1,1)
plot(energy, spectrum, 'k', ...
    energy(260:340), spectrum(260:340), 'c', ...
    energy(1120:1230), spectrum(1120:1230), 'g', ...
    energy(1360:1555), spectrum(1360:1555), 'r', ...
    energy(1555:1755), spectrum(1555:1755), 'r', ...
    'LineWidth', 1)
xlim([0 1500])

hold on
s1 = scatter(energy(304), spectrum(304), 1)
s2 = scatter(energy(1120), spectrum(1120), 1)
s3 = scatter(energy(1458), spectrum(1458), 1)
s4 = scatter(energy(1650), spectrum(1650), 1)
hold off

dt1 = datatip(s1);
s1.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s1.DataTipTemplate.DataTipRows(2).Label = 'Backscatter peak';
s1.DataTipTemplate.DataTipRows(2).Value = '';
s1.DataTipTemplate.DataTipRows(3).Label = '';
s1.DataTipTemplate.DataTipRows(3).Value = '';
dt2 = datatip(s2);
s2.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s2.DataTipTemplate.DataTipRows(2).Label = 'Compton edge';
s2.DataTipTemplate.DataTipRows(2).Value = '';
s2.DataTipTemplate.DataTipRows(3).Label = '';
s2.DataTipTemplate.DataTipRows(3).Value = '';
dt3 = datatip(s3);
s3.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s3.DataTipTemplate.DataTipRows(2).Label = 'Photopeak I';
s3.DataTipTemplate.DataTipRows(2).Value = '';
s3.DataTipTemplate.DataTipRows(3).Label = '';
s3.DataTipTemplate.DataTipRows(3).Value = '';
dt4 = datatip(s4);
s4.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s4.DataTipTemplate.DataTipRows(2).Label = 'Photopeak II';
s4.DataTipTemplate.DataTipRows(2).Value = '';
s4.DataTipTemplate.DataTipRows(3).Label = '';
s4.DataTipTemplate.DataTipRows(3).Value = '';

subplot(2,1,2)
semilogy(energy, spectrum, 'k', ...
    energy(260:340), spectrum(260:340), 'c', ...
    energy(1120:1230), spectrum(1120:1230), 'g', ...
    energy(1360:1555), spectrum(1360:1555), 'r', ...
    energy(1555:1755), spectrum(1555:1755), 'r', ...
    'LineWidth', 1)
xlim([0 1500])
sgtitle('Spectrum of Co60') 

%% Ba133
i = 5;
data = table2array(importfile_spe(file_name(i)));
data_norm = data./(max(data)*time_data(i));

spectrum = data_norm-noise_norm;

figure
subplot(2,1,1)
plot(energy, spectrum, 'k', ...
    energy(380:500), spectrum(380:500), 'r', ...
    energy(100:135), spectrum(100:135), 'r', ...
    energy(30:65), spectrum(30:65), 'b', ...
    'LineWidth', 1)
xlim([0 500])

hold on
s1 = scatter(energy(48), spectrum(48), 1)
s2 = scatter(energy(118), spectrum(118), 1)
s3 = scatter(energy(402), spectrum(402), 1)
s4 = scatter(energy(468), spectrum(468), 1)
hold off

dt1 = datatip(s1);
s1.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s1.DataTipTemplate.DataTipRows(2).Label = 'Cs K-line';
s1.DataTipTemplate.DataTipRows(2).Value = '';
s1.DataTipTemplate.DataTipRows(3).Label = '';
s1.DataTipTemplate.DataTipRows(3).Value = '';
dt2 = datatip(s2);
s2.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s2.DataTipTemplate.DataTipRows(2).Label = 'Photopeak I';
s2.DataTipTemplate.DataTipRows(2).Value = '';
s2.DataTipTemplate.DataTipRows(3).Label = '';
s2.DataTipTemplate.DataTipRows(3).Value = '';
dt3 = datatip(s3);
s3.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s3.DataTipTemplate.DataTipRows(2).Label = 'Photopeak II';
s3.DataTipTemplate.DataTipRows(2).Value = '';
s3.DataTipTemplate.DataTipRows(3).Label = '';
s3.DataTipTemplate.DataTipRows(3).Value = '';
dt4 = datatip(s4);
s4.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s4.DataTipTemplate.DataTipRows(2).Label = 'Photopeak III';
s4.DataTipTemplate.DataTipRows(2).Value = '';
s4.DataTipTemplate.DataTipRows(3).Label = '';
s4.DataTipTemplate.DataTipRows(3).Value = '';

subplot(2,1,2)
semilogy(energy, spectrum, 'k', ...
    energy(380:500), spectrum(380:500), 'r', ...
    energy(100:135), spectrum(100:135), 'r', ...
    energy(30:65), spectrum(30:65), 'r', ...
    'LineWidth', 1)
xlim([0 500])
sgtitle('Spectrum of Ba133') 
