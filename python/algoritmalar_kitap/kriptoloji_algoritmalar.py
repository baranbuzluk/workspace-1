import numpy as np
"""
    asci tablosundaki baslangicindan x karakterin ascii kodu cıkarılarak
    0-25 arasinda bir sayi elde edilir.
    """
asciLetterInit=ord('a')
def mapping(x):
    return ord(x)-asciLetterInit

def caesarSifreleme(acikMetin,keyNum):
    """
    Caeser şifrelemede her harf, belirli bir kaydırma yapılarak başka bir harfle yer değiştirmektedir.
    :param acikMetin: girilen metinin harfleri ingiliz alfabesi ve küçük olmalıdır
    :param keyNum: caesar şifresindeki kaydırma değeri
    :return: şifreli metni geri döndürür
    """
    keyNum = 3
    alfabe_sayisi = 26

    """
    x degerinin sifrelenmis harfe donusturme islemidir.
    
    y=(x+k)mod N
    
    y=şifrelenmiş metinin harfi
    x=acik metinin harfi
    k=kaydirma sayisi
    N= alfabedeki harf sayisi
    """
    def encrypt (x):
        x = mapping(x)
        word=(x + keyNum) % alfabe_sayisi
        return chr (word+asciLetterInit)

    """
    kaydirilmis x degerini orjinal değere donusturme islemidir.
    
    x=(y-k+n) mod N
    
    y=şifrelenmiş metinin harfi
    x=acik metinin harfi
    k=kaydirma sayisi
    N= alfabedeki harf sayisi
    """
    def decrypt(x):
        x = mapping(x)
        word = (x - keyNum+alfabe_sayisi) % alfabe_sayisi
        return chr(word + asciLetterInit)

    sifreliMetin=""

    for harf in acikMetin:
        sifreliMetin=sifreliMetin+encrypt(x=harf)

    return sifreliMetin

def polybiusSifreleme(acikMetin):
    """
    Polybius şifreleme yöönteminde alfabedeki harfler, iki boyutlu bir tabloya yerleştirilerek satır ve sütun
    numaralarına göre şifreli bilgi oluşturulmaktadır.
    Bu şifrelemede her harfin yerine iki rakam konulmaktadır.
    Bu rakamlar, acik metin harflerinin tablodaki pozisyonunun satır ve sütun değerleridir.

    tablo oluşturulurken kolaylık olsun diye 25 harf alınmıştır
    z harfi tabloda yoktur.
    :param x: acik metin
    :return: şifreli metin geriye döner
    """


    """
    tablo olusturuluyor a-dan y'ye kadar
    [['a' 'b' 'c' 'd' 'e']
    ['f' 'g' 'h' 'i' 'j']
    ['k' 'l' 'm' 'n' 'o']
    ['p' 'q' 'r' 's' 't']
    ['u' 'v' 'w' 'x' 'y']]
    """
    table = [chr(ord('a') + i) for i in range(25)]
    table = np.array(table)
    table = table.reshape(5, 5)

    """
    metindeki harflerin tablodaki karşılık gelen index değerli listeye ekleniyor
    """
    sifreliMetin=[]
    index=None
    for harf in acikMetin:
        index=np.argwhere(table==harf)
        sifreliMetin.append(index.tolist()[0])

    return sifreliMetin




def dogrusalSifreleme(acikMetin):
    """
    doğrusal şifreleme yöntemi (afin dönüşümü), bir E(x)=(ax+b)mod N işlemidir
    a değeri ile N değeri aralarında asal olmalıdır
    ebob(a,N)=1
    x=sifrelenecek harf
    N=harf sayisi

    :param acikMetin: şifrelenecek mesaj (str)
    :return : sifrelenmiş mesaj (list)
    """

    "sifreleme fonksiyonu"
    (a, b, harfSayisi) = (7, 5, 29)
    def encrpytFunc(x):
        return (a*x+b) % harfSayisi

    """
    desifreleme fonksiyonu
    z=> ax==1(modN) (a'nin tersi olmalı yani a*z =1 modN) 
    D(y)=z(y-b) mod N
    """
    def decryptFunc(y):
        return (25)*(y-b) % harfSayisi

    "acikMetini sifreli metine donusturur"
    sifreliMetin=[ encrpytFunc( mapping(i) ) for i in acikMetin]


    "burada sifreli metnin elemanları zaten int değer olduğu için mapping işlemi yapılmadı"
    cozulenMetin=[ decryptFunc( i ) for i in sifreliMetin]

    print(sifreliMetin)
    print(cozulenMetin)
    return sifreliMetin



def rsaSifreleme():
    """
    RSA şifreleme yöntemi
    RSA anahtar uretimi; Algoritmalar (vasif nabiyev) syf 267.

    n=p*q  fi=(p-1)*(q-1)
    1< e < fi rasgele bir e sayisi secilir ebob(e,fi)=1
    1< d < fi aralidinda  ed=1 (mod fi) sartini saglayan d sayisi hesaplanir
    genel anahtar (n,e); ozel anahtar d dir;
    """
    # Anahtar uretimi BEGIN
    p=13
    q=23
    n=p*q
    fi=(p-1)*(q-1)
    e=35 # 35 sayisini sarta uygun sectik
    d=83 # e=35 olursa d sayisi 83 olur
    # Anahtar uretimi END

    # Sifreleme BEGIN
    mesaj=11;
    

    # Sfireleme END

