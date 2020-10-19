
clear


%% 1.Bolum variable
clear
adi="baran"
soyadi="buzluk"
adiSoyadi=char(adi+soyadi)
harf=adiSoyadi(3)

%% 2.Bolum vectors
clear
vector=uint64([1 1 2])
vector2=uint64([2 2 3])
vector2D=[vector;vector2]

vector2D(1,1:2)

vector2D=[(1:1:10);[10:10:100];[3:3:30]]

%% 3.Bolum multi vector
vector2D=[[(1:1:10);(1:1:10)];
          [(1:1:10);(1:1:10)];
          [(1:1:10);(1:1:10)];]
      
vector3D(:,:,2)=vector2D-10
vector3D(:,:,3)=vector2D+10
vector3D=cat(3,vector3D,vector3D,vector3D,vector3D,vector3D,vector3D)

%% 4.Bolum  cell veritipi
clear
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
clear
yaslar=[74;6;8];
isimler=["baran";"ahmet";"yasin"]
meslekler={"tüpçü";'kuruyemişçi';"elektrikçi"}

tablo=table(yaslar,isimler,meslekler)

tablo=sortrows(tablo,'yaslar',"ascend")
tablo=sortrows(tablo,"isimler","descend")

yas=tablo.yaslar
isim=tablo.meslekler


%% 6.Bolum table özellikleri
clear
load patients.mat
hastaTable=table(Age,Height,Weight,Gender,'RowNames',LastName);

satirlar=hastaTable.Row(1:6)
ilk5kisi=head(hastaTable,5)
bilgiler=hastaTable({'Davis';'Miller'},:)

%% 7.Bolum degiskenlerde yararlı fonksiyonlar
clear
ifade1="for";
ifade2="findik";

d1=iskeyword(ifade1) 
d2=iskeyword(ifade2)

var1=isvarname(ifade1)
var2=isvarname(ifade2)

ifade3=2.54;
sonuc=isa(ifade3,'double')
sonuc=isa(ifade1,'double')

sayi=4
sonuc1=isinteger(sayi)
sonuc=isnumeric(sayi)

a="3.14"
b="Saw"
casting=double(a)
casting1=double(b)
isnan(casting1)


%%8.Bolum Map veritipi
clear

keySet=[6 34 35]
valueSet={"Ankara" "İstanbul" "İzmir"}

map=containers.Map(keySet,valueSet)

map(6)
map.Count
map.ValueType

%boş map yapısı
map=containers.Map()
map("baran")=18
map('Ahmet')="152"
degerler=map.values({"baran","Ahmet"})
map.remove("baran")
