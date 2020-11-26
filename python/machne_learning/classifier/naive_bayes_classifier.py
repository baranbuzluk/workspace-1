import pandas as pd

# Loading ve slicing dataframe
#   BEGIN
csv_dframe = pd.read_csv('../datas/veriler.csv')  # ulke,boy,kilo,yas,cinsiyet
x_datas_np = csv_dframe.iloc[:, 1:4].values  # boy,kilo,yas
y_datas_np = csv_dframe.iloc[:, 4:].values  # cinsiyet

#   END


# Separating train and test datas
#   BEGIN
from sklearn.model_selection import train_test_split

x_train_np, x_test_np, y_train_np, y_test_np = train_test_split(x_datas_np, y_datas_np, random_state=0, test_size=0.33)

#   END


# Training the model
#   BEGIN
from sklearn.naive_bayes import GaussianNB

gaussian_nb = GaussianNB()
gaussian_nb.fit(x_train_np, y_train_np)
y_predict_np = gaussian_nb.predict(x_test_np)
#   END


# Confusion matrix of the model
#   BEGIN
from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(y_test_np, y_predict_np)
print(conf_matrix)
#   END
