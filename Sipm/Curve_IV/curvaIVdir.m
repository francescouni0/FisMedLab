cd 'C:\Users\simol\Desktop\Laboratorio FisMed\SiPM\curva IV diretta'

T = readtable("curvaIVdiretta.txt");

V = -table2array(T(2:20,"Voltage_V_"));

I = -table2array(T(2:20,"Current_nA_"));

sigma = I.*0.03;
w = 1./sqrt(sigma);

curvaIVdir_fit(V, I, w)