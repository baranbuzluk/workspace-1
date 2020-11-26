
%% 1.Bolum Matrix logical islemleri
clc;clear all
sayilar=[7 2 3;
         2 5 10;
         1 8 12]

resultLogic= sayilar >=5 % matristeki 5'ten buyuk sayilari logical karsiligini verir (matris).
find(sayilar >=5) % indexleri verir

sayilar(sayilar >5)=0 %sayilar matrisindeki kosula uyan elemeanlari 0 atamasi  yapar

%% 2.Bolum categorical veri
clc; clear all
dizi=[1 2 2;3 2 1; 1 3 2]
kategori={'Kırmızı','Yeşil','Mavi'};
kategorikDizi=categorical(dizi,[1 2 3],kategori);
kategoriler=categories(kategorikDizi);

vasitalar=["Araba","Gemi","Ucak","Helikopter",missing,"Motosiklet"];
kategorikVasitalar=categorical(vasitalar)

x=[1:100];
x=x.';

y=discretize(x,[10 20 30])

%% 3.Bolum for dongusu
%sayi=input('Faktoriyel sayisini giriniz;');
sayi=1
faktoriyel=1;
for sayac=1:sayi
faktoriyel=faktoriyel*sayac;
end


%% 4.Bolum Function
clc; clear all;
Func(5,6)


%% 5.Bolum hata verme

%%error("Selamın Aleykum")
a=51
%assert(a>50)
assert(a>50,"A sayisi 50 üzerinde olmalı")

%% 6.Bolum uyarı verme

warning("Uyarı verme fonksiyonu")

%% 7.Bolum try-catch yapısı

try
    a=0;
    b=7;
    c=b/a;
    assert(c~=inf)
catch 
     disp("hata meydana geldi.")
end

a=[1 2 ;3 4];