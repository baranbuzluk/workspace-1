clc;clear;
%% PARAMETRELER
func_g = @(x) 3*exp(-0.5*x);
x=8;
epsilon=0.00000001;
iter=100000;
%% BASIT ITERASYON
i=0;
x0=x;
x1=0;
error=epsilon+1;
while true
    if error< epsilon || iter < i
        break;
    end
    x1 = func_g(x0);
    error = abs(x1-x0);
   
    fprintf('%d.Iterasyon -> X:%.7f  Error:%.7f\n',i,x1,error);
    i=i+1;
    x0=x1;
end






