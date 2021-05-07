clc;clear;
%% PARAMETRELER
func=@(x)exp(-x)-x;
a =0;
b =1;
epsilon=0.00001;
iter=5;
%% SECAND 
i=1;
x0=a;
x1=b;
x2=0;
error=epsilon+1;
if func(a)*func(b)>0
    fprintf('Bu aralikta kok yok\n');
else
    while true
        if iter < i || error < epsilon
                break;
        end
        opr1 = func(x1)*(x0-x1);
        opr2 = func(x0)-func(x1);
        opr3 = opr1/opr2;
        x2 = x1 - opr3;
        error=abs(x2-x1);
        fprintf('%d.Iterasyon -> X0= %.7f X1= %.7f X2= %.7f Error=%.7f \n',i,x0,x1,x2,error);
        x0=x1;
        x1=x2;
        
        i=i+1;
    end
end


