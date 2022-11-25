peaks=importdata('peaks.txt'); 
x=[1,2,3,4,5,6];

c = polyfit(x,peaks(1,1:6),1);

disp(['Equation is y = ' num2str(c(1)) '*x + ' num2str(c(2))])

y_est = polyval(c,x);

hold on
plot(x,y_est,'r--','LineWidth',2)
plot(x,peaks(1,1:6))
hold off