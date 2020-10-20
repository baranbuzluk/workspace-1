"""
Kod yazma şablonu
#Baslik
#   BEGIN
...
KODLAR
...
#   END
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Verilerin yuklenmesi
#   BEGIN
dfVeriler=pd.read_csv('veriler.csv')
dfCinsiyet=dfVeriler[['cinsiyet']]
#   END



# Cinsiyet kolonunu ayristirma ve numerik formata donusturme
#   BEGIN
from sklearn.preprocessing import LabelEncoder
labelEncoder=LabelEncoder()

dfCinsiyet=dfCinsiyet.iloc[:,:].values
dfCinsiyet[:,0]=labelEncoder.fit_transform(dfCinsiyet[:,0]) # erkek:0 kadin:1
dfCinsiyet=pd.DataFrame(data=dfCinsiyet,index=range(len(dfCinsiyet)),columns=['cinsiyet'])
dfVeriler=dfVeriler.drop('cinsiyet',axis=1) #cinsiyet kolonunu sil
#print(dfVeriler)
#   END


# Ulke kolonunu kategorilere (numeric) ayirma ve tekrar verilerle birlestirme
#   BEGIN
from sklearn.preprocessing import OneHotEncoder
oneEncoder=OneHotEncoder(categories='auto')
dfUlkeler=dfVeriler[['ulke']]

dfUlkeler=oneEncoder.fit_transform(dfUlkeler).toarray()
dfUlkeler=pd.DataFrame(data=dfUlkeler,columns=['fr','tr','us'],index=range(len(dfUlkeler)))

dfVeriler=dfVeriler.drop('ulke',axis=1)
dfVeriler=pd.concat([dfUlkeler,dfVeriler],axis=1)
#print(dfVeriler)
#   END


#Verileri  Train set ve Test set ayristirilmasi
#   BEGIN
from sklearn.model_selection import  train_test_split
(x_train,x_test,y_train,y_test)=train_test_split(dfVeriler,dfCinsiyet,random_state=0,test_size=0.33)
#print(x_train)
#print(y_train)
#   END


# Model olusturma
#   BEGIN
from sklearn.linear_model import LinearRegression
linearReg=LinearRegression()
linearReg.fit(x_train,y_train)

y_prediction=linearReg.predict(x_test)
print(y_prediction)
#   END