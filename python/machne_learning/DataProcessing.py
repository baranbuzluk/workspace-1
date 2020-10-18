import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
"""
Kod yazma şablonu
#Baslik
#   BEGIN
...
KODLAR
...
#   END
"""

# Verileri csv dosyasından okuma#
#   BEGIN
datas=pd.read_csv("veriler.csv")
#print(datas)
#   END



#Verilerin işlenmesi
#   BEGIN
boyDatas=datas[['boy']]
boyKiloDatas=datas[['boy','kilo']]
#print(boyDatas)
#print(boyKiloDatas['boy'].tolist())
#print(type(boyKiloDatas['boy']))
#   END



#Eksik Verilerin Düzenlenmesi
#   BEGIN
from sklearn.impute import SimpleImputer
missingData=pd.read_csv('eksikveriler.csv')
mean_imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')
yas=missingData.iloc[:,1:4].values
#print(yas)
mean_imputer=mean_imputer.fit(yas[:,1:4])
yas[:,1:4]=mean_imputer.transform(yas[:,1:4])
#print(yas)
#   END



#Kategorik veriler olusturma
#   BEGIN
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
ulkeler=missingData.iloc[:,0:1]
"""
print(ulkeler)
labelEncoder=LabelEncoder()
ulkeler['ulke']=labelEncoder.fit_transform(ulkeler['ulke'])
print(ulkeler)
"""
oneHotEncoder=OneHotEncoder(categories='auto')
ulkeler=oneHotEncoder.fit_transform(ulkeler).toarray()
print(ulkeler)
#   END
