%%func-> function for work on. you must give a function adress
%% x0,x1 -> {x0,x1} closed range
function y=secand_method(func,x0,x1)
epsilon=0.0000000001;
while abs(secand(func,x0,x1)-x0) > epsilon
x0=secand(func,x0,x1);
end
y=x0;
end
function y = secand(func,x0,x1)
y= x1-(func(x1) * (x1 - x0)) / (func(x1) - func(x0));
end