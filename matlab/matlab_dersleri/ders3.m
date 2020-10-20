clc
clear
%% 1.Bolum Matrix logical islemleri
sayilar=[7 2 3;
         2 5 10;
         1 8 12]

resultLogic= sayilar >=5 % matristeki 5'ten buyuk sayilari logical karsiligini verir (matris).
find(sayilar >=5) % indexleri verir

sayilar(sayilar >5)=0 %sayilar matrisindeki kosula uyan elemeanlari 0 atamasi  yapar


