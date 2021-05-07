clc;clear;
%% PARAMETRELER
func=@(x) x*exp(-x) + power(x,3)+1;
x0=-1;
x1=0;
epsilon=0.0001;
iter=20;
%% BISECTION
i=0;
xa =x0;
xb= x1;
xc= 0;
error=epsilon+1;
if func(x0)*func(x1) < 0
    while true
         if error < epsilon || iter < i
            break
         end 
        xc = (xa+xb) / 2;
        error = abs(xa-xb);
        if func(xa)*func(xc)<0
            xb=xc;
        elseif func(xb)*func(xc)<0
            xa=xc;
        elseif func(xb)*func(xc) == 0
            fprintf('%d.Iterasyon -> Xa: %.7f Xb: %.7f Xc: %.7f  Error: %.7f\n',i,xa,xb,xc,error);
            break;
        end
        fprintf('%d.Iterasyon -> Xa: %.7f Xb: %.7f Xc: %.7f  Error: %.7f\n',i,xa,xb,xc,error);
        i=i+1;
    end
    
else
    fprintf('Fonksiyonun koku yok.');
end
    

