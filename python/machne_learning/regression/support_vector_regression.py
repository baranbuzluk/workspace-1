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



# Loading and slicing dataframe
#   BEGIN
csv_dframe=pd.read_csv('../datas/maaslar.csv')

egitim_seviyesi_df=csv_dframe.iloc[:,1:2]
maas_df=csv_dframe.iloc[:,2:] # y data
#print(egitim_seviyesi_df,maas_df)

egitim_seviyesi_np=egitim_seviyesi_df.values
maas_np=maas_df.values # x data
#print(egitim_seviyesi_np,maas_np)
#   END



# Converting datas to standard-scaled datas
#   BEGIN
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
maas_scaler_np=scaler.fit_transform(maas_np)
egitim_seviyesi_scaler_np=scaler.fit_transform(egitim_seviyesi_np)

print(type(maas_scaler_np))
#   END


# Creating SVR  model
#   BEGIN
from sklearn.svm import SVR
svr_model=SVR(kernel='rbf')
svr_model.fit(egitim_seviyesi_scaler_np,maas_scaler_np)
maas_scaler_predict=svr_model.predict(egitim_seviyesi_scaler_np)
#   END

# Creating visualization of the model
#   BEGIN
plt.scatter(egitim_seviyesi_scaler_np,maas_scaler_np,color='red')
plt.plot(egitim_seviyesi_scaler_np,maas_scaler_predict,color='black')
plt.show()
#   END


# Evaluation with R2_score
#   BEGIN
from sklearn.metrics import r2_score
score=r2_score(maas_scaler_np,maas_scaler_predict)
print(score)
#   END