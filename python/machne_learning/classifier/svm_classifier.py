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

# Scaling train and test datas
#   BEGIN
from sklearn.preprocessing import StandardScaler

StandardScaler = StandardScaler()
StandardScaler.fit(x_train_np)
x_scaled_train = StandardScaler.transform(x_train_np)
x_scaled_test = StandardScaler.transform(x_test_np)
#   END


# Training the model
#   BEGIN
from sklearn.svm import SVC

model_kernel = 'rbf'

svc = SVC(kernel=model_kernel)
svc.fit(x_scaled_train, y_train_np)
y_predict_np = svc.predict(x_scaled_test)
#   END

# Confusion matrix of the movdel
#   BEGIN
from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(y_test_np, y_predict_np)
print(conf_matrix)
#   END
