%INTEGRAL HESAPLAMA DIKDORTGENLER YONTEMI
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
%% DIKDORTGENLER YONTEMI
sum=0;
xi = a;
for i = 1:n
    yi = func(xi);
    sum= sum + yi;
    fprintf('X(%d)= %.4f  |  Func(%.4f)=%.4f \n',i, xi ,xi ,yi);
    xi  = a + i*h;
end
S = h*sum;
fprintf('S_Alan = %.4f \n',S);