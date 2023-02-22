clear all
close all
clc

T = readtable("curvaIVinvill1take2.txt");

V = table2array(T(1:61,"Voltage_V_"));

I = table2array(T(1:61,"Current_nA_"));


s = semilogy(V, I);
dt = datatip(s,53,I(53));
s.DataTipTemplate.DataTipRows(1).Label = 'Voltage[V]:';
s.DataTipTemplate.DataTipRows(2).Label = 'Breakdown point';
s.DataTipTemplate.DataTipRows(2).Value = '';
title('LED on (A)');
xlabel( 'Voltage[V]', 'Interpreter', 'none' );
ylabel( 'Current[nA]', 'Interpreter', 'none' );
grid on

sigma = I.*0.03;
w = 1./sqrt(sigma);
curvaIVinv_fit(V, I, 53, max(I), w);