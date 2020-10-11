import numpy as np

def caesarSifreleme(acikMetin,keyNum):
    """
    Caeser şifrelemede her harf, belirli bir kaydırma yapılarak başka bir harfle yer değiştirmektedir.

    :param acikMetin: girilen metinin harfleri ingiliz alfabesi ve küçük olmalıdır
    :param keyNum: caesar şifresindeki kaydırma değeri
    :return: şifreli metni geri döndürür
    """
    keyNum = 3
    ascii_baslangic = ord('a')
    alfabe_sayisi = 26

    def normalize(x):
        return ord(x)-ascii_baslangic
    def encrypt (x):
        x = normalize(x)
        word=(x + keyNum) % alfabe_sayisi
        return chr (word+ascii_baslangic)

    def decrypt(x):
        x = normalize(x)
        word = (x - keyNum+alfabe_sayisi) % alfabe_sayisi
        return chr(word + ascii_baslangic)

    sifreliMetin=""

    for harf in acikMetin:
        sifreliMetin=sifreliMetin+encrypt(x=harf)

    return sifreliMetin

def polybiusSifreleme(acikMetin):
    """
    Yöntemde alfabedeki harfler, iki boyutlu bir tabloya yerleştirilerek satır ve sütun
    numaralarına göre şifreli bilgi oluşturulmaktadır.
    Bu şifrelemede her harfin yerine iki rakam konulmaktadır.
    Bu rakamlar, acik metin harflerinin tablodaki pozisyonunun satır ve sütun değerleridir.

    tablo oluşturulurken kolaylık olsun diye 25 harf alınmıştır
    z harfi tabloda yoktur.
    :param x: acik metin
    :return: şifreli metin geriye döner
    """

    table = [chr(ord('a') + i) for i in range(25)]
    table = np.array(table)
    table = table.reshape(5, 5)

    sifreliMetin=[]
    index=None
    for harf in acikMetin:
        index=np.argwhere(table==harf)
        sifreliMetin.append(index.tolist()[0])

    return sifreliMetin

