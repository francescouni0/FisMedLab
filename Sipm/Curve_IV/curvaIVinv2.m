T = readtable("curvaIVinvill2.txt");

V = table2array(T(1:57,"Voltage_V_"));

I = table2array(T(1:57,"Current_nA_"));

s = semilogy(V, I);
dt = datatip(s,52,I(49));
title('I vs. V (Polarizzazione inversa)');
xlabel( 'V', 'Interpreter', 'none' );
ylabel( 'I', 'Interpreter', 'none' );
grid on

curvaIVinv_fit(V, I, 53, max(I));