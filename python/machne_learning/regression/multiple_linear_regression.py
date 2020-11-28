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
import pandas as pd

# Verilerin yuklenmesi
#   BEGIN
csv_dframe = pd.read_csv('../datas/veriler.csv')
#   END


# Cinsiyet kolonunu ayristirma ve numerik formata donusturme
#   BEGIN
from sklearn.preprocessing import LabelEncoder

labelEncoder = LabelEncoder()

gender_dframe = csv_dframe[['cinsiyet']]
gender_nparray = gender_dframe.iloc[:, :].values
gender_nparray[:, 0] = labelEncoder.fit_transform(gender_nparray[:, 0])  # erkek:0 kadin:1

gender_dframe = pd.DataFrame(data=gender_nparray, index=range(len(gender_nparray)), columns=['cinsiyet'])
csv_without_gender_dframe = csv_dframe.drop('cinsiyet', axis=1)  # cinsiyet kolonunu sil
#   END


# Ulke kolonunu kategorilere (numeric) ayirma ve tekrar verilerle birlestirme
#   BEGIN
from sklearn.preprocessing import OneHotEncoder

oneEncoder = OneHotEncoder(categories='auto')
country_dframe = csv_without_gender_dframe[['ulke']]

country_nparray = oneEncoder.fit_transform(country_dframe).toarray()
country_dframe = pd.DataFrame(data=country_nparray, columns=['fr', 'tr', 'us'], index=range(len(country_nparray)))

csv_without_gender_country_dframe = csv_without_gender_dframe.drop('ulke', axis=1)
csv_without_gender_dframe = pd.concat([country_dframe, csv_without_gender_country_dframe], axis=1)
print(csv_without_gender_dframe)
#   END


# Verileri  Train set ve Test set ayristirilmasi --cinsiyet tahmini
#   BEGIN
from sklearn.model_selection import train_test_split

(x_train_gender, x_test_gender, y_train_gender, y_test_gender) = train_test_split(csv_without_gender_dframe,
                                                                                  gender_dframe, random_state=0,
                                                                                  test_size=0.33)
# print(x_train_gender)
# print(y_train_gender)
#   END


# Model olusturma -- cinsiyet tahmini
#   BEGIN
from sklearn.linear_model import LinearRegression

linearReg = LinearRegression()
linearReg.fit(x_train_gender, y_train_gender)
y_prediction = linearReg.predict(x_test_gender)
# print(y_prediction)
#   END


# Veri setini duzenleme -- boy tahmini
#   BEGIN

csv_concated_gender_dframe = pd.concat([csv_without_gender_dframe, gender_dframe], axis=1)
height_dframe = csv_concated_gender_dframe['boy']  # boy verisi
csv_without_height_dframe = csv_concated_gender_dframe.drop('boy', axis=1)  # kalan veriler
# print(csv_without_height_dframe)

## train ve test datalarini ayirma
(x_train_height, x_test_height, y_train_height, y_test_height) = train_test_split(csv_without_height_dframe,
                                                                                  height_dframe, random_state=0,
                                                                                  test_size=0.33)
#   END


# Model olusturma -- boy tahmini
#   BEGIN
from sklearn.linear_model import LinearRegression

linearReg = LinearRegression()
linearReg.fit(x_train_height, y_train_height)
y_prediction = linearReg.predict(x_test_height)
print(y_prediction)
#   END


# Model olusturma -- boy tahmini
#   BEGIN
import statsmodels.regression.linear_model as sm

X = np.append(arr=np.ones((22, 1)).astype(int), values=csv_without_height_dframe, axis=1)
X_l = csv_without_height_dframe.iloc[:, [0, 1, 2, 3, 4]].values

height_np = height_dframe.values
r_ols = sm.OLS(endog=height_np, exog=X_l)
r = r_ols.fit()
print(r.summary())
#   END
