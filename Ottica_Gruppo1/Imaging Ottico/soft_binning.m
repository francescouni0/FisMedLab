function image_rebinned = soft_binning(image, binning_factor)

bin_size = [binning_factor binning_factor];

image_rebinned = mat2cell(image, repmat(bin_size(1),[1 size(image,1)/bin_size(1)]), ...
                                 repmat(bin_size(2),[1 size(image,2)/bin_size(2)]));
image_rebinned = cellfun(@(x) sum(x,'all'), image_rebinned);

end