function y=golden_section_method(func,a,b)
golden_rate=(sqrt(5)-1)/2;
epsilon=0.000000001;
iter=5;
x1=a+((1-golden_rate)*(b-a));
x2=b-(golden_rate*(b-a));
while iter
    
    if func(x1)>func(x2)
        a=x2;
        x2=x1;
        x1=a+((1-golden_rate)*(b-a));
    else 
         b=x1;
        x1=x2;
        x2=b-(golden_rate*(b-a));
    end
    iter=iter-1;
end
y=[x2 func(x2);x1 func(x1)];
end




