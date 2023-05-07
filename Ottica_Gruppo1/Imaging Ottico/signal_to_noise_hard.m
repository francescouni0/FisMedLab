function [SNR, error_SNR] = signal_to_noise_hard(image, dark, binning)

im = importdata(image);
im = im(:,2:end);

noise = importdata(dark);
noise = noise(:,2:end);

im = im-noise;

if binning==1
    crop = im(475:594, 445:564);
    crop_2 = im(75:194, 445:564);
elseif binning==2
    crop = im(240:299, 225:284);
    crop_2 = im(40:99, 225:284);
elseif binning==4
    crop = im(120:149, 112:141);
    crop_2 = im(20:49, 112:141);
else
    crop = im(60:74, 56:70);
    crop_2 = im(10:24, 56:70);
end

n = numel(crop);

mean = mean2(crop)-mean2(crop_2);
error_mean = sqrt((std2(crop)/sqrt(n)).^2+(std2(crop_2)/sqrt(n)).^2);

sigma = std2(crop_2);
error_sigma = sigma./sqrt(2*(n-1));

SNR = mean/sigma;
error_SNR = sqrt((error_mean./sigma).^2+(-(mean.*error_sigma)./(sigma.^2)).^2);

end