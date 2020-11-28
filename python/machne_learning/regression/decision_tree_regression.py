import matplotlib.pyplot as plt
import pandas as pd

# Loading and slicing dataframe
#   BEGIN
csv_dframe = pd.read_csv('../datas/maaslar.csv')

egitim_seviyesi_df = csv_dframe.iloc[:, 1:2]
maas_df = csv_dframe.iloc[:, 2:]  # y data
# print(egitim_seviyesi_df,maas_df)

egitim_seviyesi_np = egitim_seviyesi_df.values
maas_np = maas_df.values  # x data
# print(egitim_seviyesi_np,maas_np)
#   END


# Creating decision-tree reg model
#   BEGIN
from sklearn.tree import DecisionTreeRegressor

dtree_model = DecisionTreeRegressor(random_state=0)
dtree_model.fit(egitim_seviyesi_np, maas_np)
maas_predict_np = dtree_model.predict(egitim_seviyesi_np)
#   END


# Creating visualization of the model
#   BEGIN
plt.scatter(egitim_seviyesi_np, maas_np, color='red')
plt.plot(egitim_seviyesi_np, maas_predict_np, color='black')
plt.show()
#   END


# Evaluation with R2_score
#   BEGIN
from sklearn.metrics import r2_score

score = r2_score(maas_np, maas_predict_np)
print(score)
#   END
