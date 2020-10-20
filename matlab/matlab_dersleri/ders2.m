%% 1.Bolum matris carpimi
clear
matris1=[3 3 3;
         3 6 3;
         3 3 3];
matris2=[1 0 0;
         0 2 0;
         0 0 1];
matris3=matris1.*matris2 % birebir çarpım
matris4=matris1*matris2 %% matris çarpımı

%% 2.Bolum cell islemi
clear
isimlerChrCell={'Hüseyin','Ahmet','Mehmet','Nisa'};
soyisimlerChrCell={'Fındık','Kenal','Topuz','Kınık'};

isimlerChrCell=string(isimlerChrCell)
soyisimlerChrCell=string(soyisimlerChrCell)

isimlerChrCell=isimlerChrCell+soyisimlerChrCell

isimler=char(isimlerChrCell)
soyisimlerChr=char(soyisimlerChrCell)

%isimSoyisimChar=isimlerChr+soyisimlerChr hata verir

%% 3.Bolum kullanici input ve output fonksiyonları
%sayi=input('Bir sayi giriniz; '); %bir sayi almak icin
%kelime=input('Bir kelime yaziniz; ','s'); % bir char ifade almak icin
sayi=10;
mesaj='Merhaba Dunya'
disp(sayi)
disp('Merhaba')
disp(['Sayi:' num2str(sayi)])


message=sprintf("Sayi: %d \nMesajınız:%s",sayi,mesaj);
disp(message);

fprintf("Sayi: %d \nMesajınız:%s \n",sayi,mesaj); %outputu command satirana direk yazar