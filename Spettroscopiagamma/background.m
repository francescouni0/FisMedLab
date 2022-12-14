%% Pulisci tutto
clear
close all

%% Import spectrum
bkg = table2array(importfile_spe("fondo.Spe"));
bkg_norm = bkg./max(bkg);
channel = linspace(1, length(bkg), length(bkg));
energy = (channel.*0.8093598329870725)-10.902148156778575;

%% Peak analysis
x1 = [435 295 720 1110 1350 1720];
x2 = [500 350 850 1270 1515 1930];

peak_chn = [113];
sigma = [0];

for i = 1:6
    [m, s] = peak_analysis_background(bkg_norm, x1(i), x2(i));
    peak_chn = [peak_chn round(m)];
    sigma = [sigma s];
end

peak_energy = (peak_chn.*0.8093598329870725)-10.902148156778575;

%% Plot
figure
plot(energy, bkg_norm, 'k', ...
    energy(80:120), bkg_norm(80:120), 'r', ...
    energy(435:500), bkg_norm(435:500), 'r', ...
    energy(295:350), bkg_norm(295:350), 'r', ...
    energy(730:850), bkg_norm(730:850), 'r', ...
    energy(1110:1270), bkg_norm(1110:1270), 'r', ...
    energy(1350:1515), bkg_norm(1350:1515), 'r', ...
    energy(1720:1930), bkg_norm(1720:1930), 'r', ...
    'LineWidth', 1)
xlim([0 1600])
hold on
s1 = scatter(peak_energy(1), bkg_norm(peak_chn(1)), 25, 'blue', 'filled') %Pb82 K-line
s2 = scatter(peak_energy(2), bkg_norm(peak_chn(2)), 25, 'blue', 'filled') %Pb214
s3 = scatter(peak_energy(3), bkg_norm(peak_chn(3)), 25, 'blue', 'filled') %Pb214
s4 = scatter(peak_energy(4), bkg_norm(peak_chn(4)), 25, 'blue', 'filled') %Bi214
s5 = scatter(peak_energy(5), bkg_norm(peak_chn(5)), 25, 'blue', 'filled') %Convoluzione Ac228
s6 = scatter(peak_energy(6), bkg_norm(peak_chn(6)), 25, 'blue', 'filled') %Bi214
s7 = scatter(peak_energy(7), bkg_norm(peak_chn(7)), 25, 'blue', 'filled') %K40
hold off

dt1 = datatip(s1);
s1.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s1.DataTipTemplate.DataTipRows(2).Label = 'Pb82 K-line';
s1.DataTipTemplate.DataTipRows(2).Value = '';
s1.DataTipTemplate.DataTipRows(3).Label = '';
s1.DataTipTemplate.DataTipRows(3).Value = '';
dt2 = datatip(s2);
s2.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s2.DataTipTemplate.DataTipRows(2).Label = 'Pb214';
s2.DataTipTemplate.DataTipRows(2).Value = '';
s2.DataTipTemplate.DataTipRows(3).Label = '';
s2.DataTipTemplate.DataTipRows(3).Value = '';
dt3 = datatip(s3);
s3.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s3.DataTipTemplate.DataTipRows(2).Label = 'Pb214';
s3.DataTipTemplate.DataTipRows(2).Value = '';
s3.DataTipTemplate.DataTipRows(3).Label = '';
s3.DataTipTemplate.DataTipRows(3).Value = '';
dt4= datatip(s4);
s4.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s4.DataTipTemplate.DataTipRows(2).Label = 'Bi214';
s4.DataTipTemplate.DataTipRows(2).Value = '';
s4.DataTipTemplate.DataTipRows(3).Label = '';
s4.DataTipTemplate.DataTipRows(3).Value = '';
dt5 = datatip(s5);
s5.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s5.DataTipTemplate.DataTipRows(2).Label = 'Convoluzione Ac228';
s5.DataTipTemplate.DataTipRows(2).Value = '';
s5.DataTipTemplate.DataTipRows(3).Label = '';
s5.DataTipTemplate.DataTipRows(3).Value = '';
dt6 = datatip(s6);
s6.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s6.DataTipTemplate.DataTipRows(2).Label = 'Bi214';
s6.DataTipTemplate.DataTipRows(2).Value = '';
s6.DataTipTemplate.DataTipRows(3).Label = '';
s6.DataTipTemplate.DataTipRows(3).Value = '';
dt7 = datatip(s7);
s7.DataTipTemplate.DataTipRows(1).Label = 'Energy[KeV]:';
s7.DataTipTemplate.DataTipRows(2).Label = 'K40';
s7.DataTipTemplate.DataTipRows(2).Value = '';
s7.DataTipTemplate.DataTipRows(3).Label = '';
s7.DataTipTemplate.DataTipRows(3).Value = '';

figure
semilogy(energy, bkg_norm, 'k', ...
    energy(80:120), bkg_norm(80:120), 'r', ...
    energy(435:500), bkg_norm(435:500), 'r', ...
    energy(295:350), bkg_norm(295:350), 'r', ...
    energy(720:850), bkg_norm(720:850), 'r', ...
    energy(1110:1270), bkg_norm(1110:1270), 'r', ...
    energy(1350:1515), bkg_norm(1350:1515), 'r', ...
    energy(1720:1930), bkg_norm(1720:1930), 'r', ...
    'LineWidth', 1)
xlim([0 1600])
ylim([0.004 1])
hold on
s1_ = scatter(peak_energy(1), bkg_norm(peak_chn(1)), 25, 'blue', 'filled')
s2_ = scatter(peak_energy(2), bkg_norm(peak_chn(2)), 25, 'blue', 'filled')
s3_ = scatter(peak_energy(3), bkg_norm(peak_chn(3)), 25, 'blue', 'filled')
s4_ = scatter(peak_energy(4), bkg_norm(peak_chn(4)), 25, 'blue', 'filled')
s5_ = scatter(peak_energy(5), bkg_norm(peak_chn(5)), 25, 'blue', 'filled')
s6_ = scatter(peak_energy(6), bkg_norm(peak_chn(6)), 25, 'blue', 'filled')
s7_ = scatter(peak_energy(7), bkg_norm(peak_chn(7)), 25, 'blue', 'filled')
hold off