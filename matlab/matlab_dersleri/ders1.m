
clear

%% 1.Bolum
adi="baran"
soyadi="buzluk"
adiSoyadi=char(adi+soyadi)
harf=adiSoyadi(3)

%% 2.Bolum

vector=uint64([1 1 2])
vector2=uint64([2 2 3])
vector2D=[vector;vector2]

vector2D(1,1:2)

vector2D=[(1:1:10);[10:10:100];[3:3:30]]

%% 3.Bolum
vector2D=[[(1:1:10);(1:1:10)];
          [(1:1:10);(1:1:10)];
          [(1:1:10);(1:1:10)];]
      
vector3D(:,:,2)=vector2D-10
vector3D(:,:,3)=vector2D+10
vector3D=cat(3,vector3D,vector3D,vector3D,vector3D,vector3D,vector3D)

%% 4.Bolum  cell veritipi
yaslar=uint8([23 25 15;
        18 25 48;
        20 7 65])
 isimler=["mahmut" "kemal" "baran";
          "hüseyin" "özcan" "mehmet";
          "oguzhan" "mirac" "ahmet"]   
 
cellTipi={yaslar,isimler,"avni",19877,1456,45,'ABZE'}
hucre1=cellTipi(1)
hucre1_yaslar=cellTipi{1}


%% 5. Bolum table veritipi
yaslar=[1,2,6,74,6,18,48];
isimler=["baran","ahmet","yasin","kısmet","hicran"]
meslekler={"tüpçü",'kuruyemişçi'}

tablo=table(yaslar,isimler,meslekler)