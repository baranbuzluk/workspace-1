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

train_x_np, test_x_np, y_train_np, y_test_np = train_test_split(x_datas_np, y_datas_np, random_state=0, test_size=0.33)

#   END

# Scaling train and test datas
#   BEGIN
from sklearn.preprocessing import StandardScaler

StandardScaler = StandardScaler()
StandardScaler.fit(train_x_np)
train_scaled_x_np = StandardScaler.transform(train_x_np)
test_scaled_x_np = StandardScaler.transform(test_x_np)
#   END


# Training the model
#   BEGIN
from sklearn.tree import DecisionTreeClassifier

dt_classifier = DecisionTreeClassifier(criterion='entropy')
dt_classifier.fit(train_scaled_x_np, y_train_np)
predict_y_np = dt_classifier.predict(test_scaled_x_np)
#   END


# Confusion matrix of the model
#   BEGIN
from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(y_test_np, predict_y_np)
print(conf_matrix)
#   END
