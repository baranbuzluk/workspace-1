%%func-> function and derivative function for work on. you must give a function adress , x0-> init
%%value
function y=newton_raphson_method(func,d_func,x0)
epsilon=0.000000001;
%%default value
while true
    x1= x0-(func(x0)/ d_func(x0));
    if(abs( x1-x0) < epsilon )
        break;
    end
    x0=x1;  
end
y=x1;
end



