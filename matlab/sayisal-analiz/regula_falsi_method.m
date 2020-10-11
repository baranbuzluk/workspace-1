function y=regula_falsi_method(func,x0,x1)
epsilon=0.000000000001;
x2=epsilon+1;
old_x2=0;
while (func(x0)*func(x1)<0)&&(abs(x2-old_x2)>epsilon)
    old_x2=x2;
    x2=regula_falsi(func,x0,x1);
    if func(x0)*func(x2)<0
        x1=x2;
    else
        x0=x2;
    end
end
y=x2;
end
function y=regula_falsi(func,a,b)
%%  c= a.f(b)-b.f(a) / f(b)-f(a)
y=( (a *func(b)) - (b * func(a)) ) /  ( func(b) - func(a));
end
