%% Pulisci tutto
clear
close all

%% Calcola l'altezza dei picchi dall'indice 1 a 11 (poi diventano troppo rumorosi)
file_name = ["Am241_12V_240s.Spe" "Am241_12V_240s_0.5mmCu.Spe" "Am241_12V_240s_1mmCu.Spe" "Am241_12V_240s_1.5mmCu.Spe" "Am241_12V_240s_2mmCu.Spe" "Am241_12V_240s_2.5mmCu.Spe" "Am241_12V_240s_3mmCu.Spe" "Am241_12V_240s_3.5mmCu.Spe" "Am241_12V_240s_4mmCu.Spe" "Am241_12V_240s_4.5mmCu.Spe" "Am241_12V_240s_5mmCu.Spe" "Am241_12V_240s_5.5mmCu.Spe" "Am241_12V_240s_6.5mmCu.Spe"];
counts = [];
err_counts = [];

for i = 1:11
[c, e] = peak_analysis_att(file_name(i));
counts = [counts c];
err_counts = [err_counts e];
end

%% Verificare se aggiungere ultimi due picchi facendo media o max

%% Plot/fit
thick = reshape([0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5], 11, 1);

fit = fit(thick, transpose(counts), 'exp1');
plot(fit, thick, counts)
hold on
errorbar(thick, counts, err_counts, 'b.')
hold off
title('Attenuazione');
ylabel( 'Peak height[a.u.]');
xlabel( 'Thickness[mm]');

mu = -fit.b

