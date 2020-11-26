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
datas=pd.read_csv("datas/veriler.csv")
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
missingData=pd.read_csv('datas/eksikveriler.csv')
mean_imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')
yas=missingData.iloc[:,1:4].values
#print(yas)
mean_imputer=mean_imputer.fit(yas[:,1:4])
yas[:,1:4]=mean_imputer.transform(yas[:,1:4])
print(yas)
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
#print(ulkeler

#   END

#DataFrame olusturma ve Verileri Birleştirme
#   BEGIN
sutunlarUlke=['fr','tr','us']
dframeUlke=pd.DataFrame(data=ulkeler,index=range(len(ulkeler)),columns=sutunlarUlke)
print(dframeUlke)

sutunlarYas=['boy','kilo','yas']
dframeYas=pd.DataFrame(data=yas,index=range(len(yas)),columns=sutunlarYas)
print(dframeYas)

cinsiyet=datas.iloc[:,-1].values
print(cinsiyet)

dframeCinsiyet=pd.DataFrame(data=cinsiyet,index=range(len(cinsiyet)),columns=['cinsiyet'])
print(dframeCinsiyet)

dframeUlkeYas=pd.concat([dframeUlke,dframeYas],axis=1)
print(dframeUlkeYas)
#   END

#Veri Bölme, Train set ve Test set ayristirilmasi
#   BEGIN
from sklearn.model_selection import  train_test_split

(xTrain,xTest,yTrain,yTest)=train_test_split(dframeUlkeYas,dframeCinsiyet,random_state=0,test_size=0.33)
print(xTrain,xTest)

#   END

#Verilerde Öznitelik ölçeklendirme , standartlaştırma normalizasyon
#   BEGIN
from sklearn.preprocessing import StandardScaler
std=StandardScaler()
xTrain=std.fit_transform(xTrain)
xTest=std.fit_transform(xTest)
print(xTrain)
#   END