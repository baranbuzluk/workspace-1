clc;clear;
%% PARAMETRELER
func = @(x) power(x,3) +4*power(x,2) -3;
func_derivate= @(x) 3*power(x,2) +8*x;
x=0.7;
epsilon=0.000005;
iter=10000;
error=epsilon+1;
%% NEWTON RAPHSON YONTEMI
i=0;
x0=x;
x1=0;
while true 
   x1 = x0 - (func(x0) / func_derivate(x0));
   error = abs( x1-x0);
   fprintf('%d. Iteration -> X0=%.4f X1=%.4f Y0=%.4f Y''=%.4f Error=%.7f\n',i,x0,x1,func(x0),func_derivate(x0),error); 
   if iter<i || error < epsilon
        break;
   end
   i=i+1;
   x0 = x1; 
end
fprintf('Sonuc=%.10f\n',x1); 





