%INTEGRAL HESAPLAMA YAMUK YONTEMI
clc;clear;
%% INTEGRAL FONK.
% integrali hesaplanacak fonk.
func = @(x) exp(x)*(sin(x)^2); 
% uc duzeltme icin integrali hesaplanacak fonk. turevi 
func_derivative =@(x) (exp(x)*sin(x)^2) + (2*sin(x)*cos(x)*exp(x)); 

%% PARAMETRELER
b = pi; % integral fonk. ust  sinir
a = 0; % integral fonk. alt sinir

% Parca sayisi verilmisse
n = 4;  
h = (b -a) / n;
% Adim degeri verilmisse 
%h=0.5;
%n=(b -a) /h ;

fprintf('H degeri=%.4f \n',h);

%% YAMUK YONTEMI
ya = func(a); % integral alt sinirin fonk. deg. (baslangic)
yb = func(b); % integral ust sinirin fonk. deg. (bitis)
sum = (ya + yb)/2;

for i = 1 : n-1
    x_i  = a + i*h;
    y_i = func(x_i);
    sum = sum + y_i;
    fprintf('X(%d)= %.4f  |  Func(%.4f)=%.4f \n',i, x_i ,x_i ,y_i);
end

S_alan = h* sum;
fprintf('S_Alan = %.4f \n',S_alan);

%% UC DUZELTME
operation_1 = (h^2)/ 12;
operation_2 = func_derivative(b)-func_derivative(a);
result = operation_1 * operation_2;
S_alan_uc_duzeltme = S_alan - result;
fprintf('S_alan_uc_duzeltme = %.4f \n',S_alan_uc_duzeltme);



