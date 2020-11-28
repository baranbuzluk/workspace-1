"""
Kod yazma şablonu
#Baslik
#   BEGIN
...
KODLAR
...
#   END
"""

import matplotlib.pyplot as plt
import pandas as pd

"""
egitim_seviyesi == x;
maas == y;

"""

# Loading and slicing dataframe
#   BEGIN
csv_dframe = pd.read_csv('../datas/maaslar.csv')

egitim_seviyesi_df = csv_dframe.iloc[:, 1:2]
maas_df = csv_dframe.iloc[:, 2:]
# print(egitim_seviyesi_df,maas_df)

egitim_seviyesi_np = egitim_seviyesi_df.values
maas_np = maas_df.values
# print(egitim_seviyesi_np,maas_np)
#   END


# Transforming to polynomial_feature
#   BEGIN
from sklearn.preprocessing import PolynomialFeatures

x_degree = 3  # degree of polynomial
polynomial_feature = PolynomialFeatures(degree=x_degree)
egitim_seviyesi_poly_np = polynomial_feature.fit_transform(egitim_seviyesi_df)
print(egitim_seviyesi_poly_np)
#   END


# Creating Polynomial Regression model
#   BEGIN
from sklearn.linear_model import LinearRegression

polynomial_reg_model = LinearRegression()
polynomial_reg_model.fit(egitim_seviyesi_poly_np, maas_df)
maas_predict_np = polynomial_reg_model.predict(egitim_seviyesi_poly_np)
# print(polynomial_reg_model.predict(egitim_seviyesi_poly_np))
#   END

# Creating visualization of the model
#   BEGIN
plt.scatter(egitim_seviyesi_df, maas_df)
plt.plot(egitim_seviyesi_df, maas_predict_np)
plt.show()
#   END

# Evaluation with R2_score
#   BEGIN
from sklearn.metrics import r2_score

score = r2_score(maas_np, maas_predict_np)
print(score)
#   END
