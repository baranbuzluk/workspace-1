%INTEGRAL HESAPLAMA 3/8 SIMPSON YONTEMI
clc;clear;
%% INTEGRAL FONK.
func = @(x) exp(x)*(sin(x)^2); % integrali hesaplanacak fonk.

%% PARAMETRELER
b = pi; % integral fonk. ust  sinir
a = 0; % integral fonk. alt sinir

% Parca sayisi verilmisse
n = 4;  
h = (b-a) / n;

% Adim degeri verilmisse 
%h=0.5;
%n=(b-a) / h; ;
fprintf('H degeri=%.4f \n',h);
%% 3/8 SIMPSON YONTEMI


ya = func(a); % integral alt sinirin fonk. deg. (baslangic)
yb = func(b); % integral ust sinirin fonk. deg. (bitis)
total = ya + yb;
for i = 1 : n-1
    x_i  = a + i*h;
    y_i = func(x_i);
    if mod(i,3)==0
        total = total+2*y_i;
    else
         total = total+3*y_i;
    end
    fprintf('X(%d)= %.4f  |  Func(%.4f)=%.4f \n',i, x_i ,x_i ,y_i);
    
end

S = 3*h*total / 8;
fprintf('S = %.4f \n',S);