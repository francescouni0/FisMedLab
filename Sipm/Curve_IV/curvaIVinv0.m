T = readtable("curvaIVinvdark.txt");

V = table2array(T(1:61,"Voltage_V_"));

I = table2array(T(1:61,"Current_nA_"));

s = semilogy(V, I);
dt = datatip(s,53,I(53));
title('I vs. V (Polarizzazione inversa)');
xlabel( 'V', 'Interpreter', 'none' );
ylabel( 'I', 'Interpreter', 'none' );
grid on

figure
curvaIVinv_fit(V, I, 53, max(I));

