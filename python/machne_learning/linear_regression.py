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

# Verilerin yuklenmesi ve Gosterilmesi
#   BEGIN
dframeSatis=pd.read_csv('satislar.csv')
aylar=dframeSatis[['Aylar']]
satislar=dframeSatis[['Satislar']]

#print(satislar,aylar)
varX=dframeSatis.iloc[:,0].values
varY=dframeSatis.iloc[:,1].values
#print(varX)
#plt.plot(varX,varY)
#plt.show()
#   END


#Verileri standartlastirma ve ayristirma
#   BEGIN
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

(x_train,x_test)=train_test_split(aylar,random_state=0,test_size=0.33)
(y_train,y_test)=train_test_split(satislar,random_state=0,test_size=0.33)

std=StandardScaler()
aylar=std.fit_transform(aylar) # standartlastirma
satislar=std.fit_transform(satislar)# standartlastirma

(x_std_train,x_std_test)=train_test_split(aylar,random_state=0,test_size=0.33)
(y_std_train,y_std_test)=train_test_split(satislar,random_state=0,test_size=0.33)

#   END


#Linear regression modeli olusturma
#   BEGIN
from sklearn.linear_model import LinearRegression

linearReg=LinearRegression()
x_train=x_train.sort_index()
y_train=y_train.sort_index()
#x_test=x_test.sort_index()

linearReg.fit(x_train,y_train) # data is training
y_predictions=linearReg.predict(x_test)

#   END

#Modeli gorsellestirme
#   BEGIN
plt.plot(x_train,y_train)
plt.plot(x_test,y_predictions)
plt.ylabel("Satislar")
plt.xlabel("Aylar")
plt.title("Aylar-Satislar Grafigi")
plt.show()
#   END