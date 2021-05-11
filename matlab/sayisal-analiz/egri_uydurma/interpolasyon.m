% Interpolasyon yontemi - egri uydurma
clc;clear;
%% PARAMETRELER
xi = [1 3 5 7 10 12 13 16 18 20];% x degerleri
yi = [4 5 6 5 8 7 6 9 12 11]; % y degerleri
n = length(xi);
%% Islemler
xi_sum = sum(xi); % x'lerin toplami
yi_sum = sum(yi); % y'lerin toplami
xi_yi_sum = sum(xi.*yi); % x*y'lerin toplami
xi_pow_2_sum = sum(xi.^2); % x^2'lerin toplami

%% A1 katsayisi
opr1 = (n * xi_yi_sum) - (xi_sum * yi_sum) ;
opr2 = (n * xi_pow_2_sum) - power(xi_sum,2);
a1 = opr1 / opr2;

%% A0 katsayisi
opr1 = yi_sum / n;
opr2 = a1 * (xi_sum / n);
a0= opr1 - opr2;
%% Y = A1*X + A0
y_predict = @(x)  a1*x + a0;