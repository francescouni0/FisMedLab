clear all
close all
clc

T = readtable("curvaIVinvill2.txt");

V_txt = table2array(T(1:57,"Voltage_V_"));
V = [0; 1; 2; 3; V_txt]

I_txt = table2array(T(1:57,"Current_nA_"));
I = [0; 0; 0; 0; I_txt]


s = semilogy(V, I);
dt = datatip(s,52,I(49));
s.DataTipTemplate.DataTipRows(1).Label = 'Voltage[V]:';
s.DataTipTemplate.DataTipRows(2).Label = 'Breakdown point';
s.DataTipTemplate.DataTipRows(2).Value = '';
title('LED on (B)');
xlabel( 'Voltage[V]', 'Interpreter', 'none' );
ylabel( 'Current[nA]', 'Interpreter', 'none' );
grid on

sigma = I.*0.03;
w = 1./sqrt(sigma);
curvaIVinv_fit(V, I, 53, max(I), w);