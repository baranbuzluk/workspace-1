
function y=bisection_method(func,x0,x1)
epsilon=0.00000000001;
x2=epsilon+1;
old_x2=0;
while (func(x0)*func(x1)<0) && abs(x2-old_x2)>epsilon
    old_x2=x2;
    x2=(x0+x1) / 2;
    if(func(x0)*func(x2)<0)
        x1=x2;
    else
        x0=x2;
    end
end
y=x2;
end