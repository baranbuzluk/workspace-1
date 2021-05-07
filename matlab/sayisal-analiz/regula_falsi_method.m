clc;clear;
%% PARAMETRELER
func=@(x) power(x,3)+4*power(x,2)-10;
x0 =1;
x1 = 2;
epsilon=0.0000;
iter=7;
%% REGULA FALSI
i=1;
a=x0;
b=x1;
c=0;
error=epsilon+1;
if func(a)*func(b)>0
    fprintf('Bu aralikta kok yok\n');
else
    while true
         if iter < i || error < epsilon
            break;
        end
        
        opr1 = a * func(b);
        opr2 = b * func(a);
        c = (opr1-opr2)/ (func(b)-func(a));
        error = abs(c-a);
        if func(a)*func(c)<0
            b=c;
        else
            a=c;
        end
        
        fprintf('%d.Iterasyon -> Xa: %.7f Xb: %.7f Xc: %.7f  Error: %.7f\n',i,a,b,c,error);
        i=i+1;
       
    end
end


