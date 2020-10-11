function y=basit_iterasyon_method(g_func,x0)
epsilon=0.1;
sayac=0;

while(abs(g_func(x0)-x0)>epsilon)
    
    x0=g_func(x0);
    sayac=sayac+1;
end
y=x0;
end

