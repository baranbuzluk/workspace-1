import pandas as pd
from sklearn.metrics import confusion_matrix

# Loading ve slicing dataframe
#   BEGIN
csv_dframe = pd.read_csv('Iris.csv')  # Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species
x_datas_np = csv_dframe.iloc[:, 1:5].values  # SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm
y_datas_np = csv_dframe.iloc[:, 5:].values  # Species
#   END


# Separating train and test datas
#   BEGIN
from sklearn.model_selection import train_test_split
train_x_np, test_x_np, train_y_np, test_y_np = train_test_split(x_datas_np, y_datas_np, random_state=0, test_size=0.33)
#   END

# Scaling train and test datas
#   BEGIN
from sklearn.preprocessing import StandardScaler

StandardScaler = StandardScaler()
StandardScaler.fit(train_x_np)
train_scaled_x_np = StandardScaler.transform(train_x_np)
test_scaled_x_np = StandardScaler.transform(test_x_np)
#   END


# Training the K-NN model
#   BEGIN
from sklearn.neighbors import KNeighborsClassifier
neighbors_number = 1  # komsuluk sayisi
distance_formul = "minkowski"  # uzaklik icin kullanilan formul
knn_classifier = KNeighborsClassifier(metric=distance_formul, n_neighbors=neighbors_number)
knn_classifier.fit(train_scaled_x_np, train_y_np)
predict_y_np = knn_classifier.predict(test_scaled_x_np)
#   END

# Confusion matrix of K-NN model
#   BEGIN
confusion_matrix_knn = confusion_matrix(test_y_np, predict_y_np)
print("K-NN model")
print(confusion_matrix_knn)
#   END

######################################################################

# Training the Decision Tree model
#   BEGIN
from sklearn.tree import DecisionTreeClassifier
decision_tree_classifier = DecisionTreeClassifier()
decision_tree_classifier.fit(train_scaled_x_np, train_y_np)
predict_y_np = decision_tree_classifier.predict(test_scaled_x_np)
#   END

# Confusion matrix of Decision Tree model
#   BEGIN
confusion_matrix_dtree = confusion_matrix(test_y_np, predict_y_np)
print("Decision Tree model")
print(confusion_matrix_dtree)
#   END

######################################################################
# Training the Random Forest model
#   BEGIN
from sklearn.ensemble import RandomForestClassifier
random_forest_classifier = RandomForestClassifier(random_state=5)
random_forest_classifier.fit(train_scaled_x_np, train_y_np)
predict_y_np = random_forest_classifier.predict(test_scaled_x_np)
#   END

# Confusion matrix of Random Forest model
#   BEGIN
confusion_matrix_rforest = confusion_matrix(test_y_np, predict_y_np)
print("Random Forest model")
print(confusion_matrix_rforest)
#   END

######################################################################

# Training the SVM model
#   BEGIN
from sklearn.svm import SVC
svm_classifier = SVC()
svm_classifier.fit(train_scaled_x_np, train_y_np)
predict_y_np =svm_classifier.predict(test_scaled_x_np)
#   END

# Confusion matrix of SVM model
#   BEGIN
confusion_matrix_svm = confusion_matrix(test_y_np, predict_y_np)
print("SVM Model")
print(confusion_matrix_svm)
#   END

######################################################################

# Training the Naive-Bayes model
#   BEGIN
from sklearn.naive_bayes import GaussianNB
naive_bayes_classifier = GaussianNB()
naive_bayes_classifier.fit(train_scaled_x_np, train_y_np)
predict_y_np =naive_bayes_classifier.predict(test_scaled_x_np)
#   END

# Confusion matrix of Naive-Bayes model
#   BEGIN
confusion_matrix_naivebayes = confusion_matrix(test_y_np, predict_y_np)
print("Naive Bayes Model")
print(confusion_matrix_naivebayes)

#   END
######################################################################