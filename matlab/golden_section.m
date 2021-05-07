clc;clear;

%% PARAMETRELER
func=@(x) x*exp(-x) + power(x,3)+1;
a=-1;
b=0;
epsilon=0.0001;
iter=20;
%% GOLDEN SECTION
golden_ratio=(sqrt(5)-1)/2;
x1=a+((1-golden_ratio)*(b-a));
x2=b-(golden_ratio*(b-a));
while iter
    if func(x1)>func(x2)
        a=x2;
        x2=x1;
        x1=a+((1-golden_ratio)*(b-a));
    else 
        b=x1;
        x1=x2;
        x2=b-(golden_ratio*(b-a));
    end
    iter=iter-1;
end
fprintf('X1:%.7f Y1:%.7f\n',x1,func(x1));
fprintf('X2:%.7f Y2:%.7f\n',x2,func(x2));




