function [e_mean, e_sigma] = fit_error(fit)

% ci = confint(fit, 0.6827);
ci = confint(fit);

e_mean = (ci(2,2)-ci(1,2))/2;

e_sigma = (ci(2,3)-ci(1,3))/(2*sqrt(2));

end

