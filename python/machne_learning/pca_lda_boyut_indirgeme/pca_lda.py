

import pandas as pd


data_set = pd.read_csv('Wine.csv')
X = data_set.iloc[:, 0:13].values
y = data_set.iloc[:, 13].values


from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size = 0.2, random_state = 0)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
train_x = sc.fit_transform(train_x)
test_x = sc.transform(test_x)


from sklearn.decomposition import PCA
pca = PCA(n_components = 2)

train_x_2 = pca.fit_transform(train_x)
test_x_2 = pca.transform(test_x)


from sklearn.linear_model import LogisticRegression
classifier_lr = LogisticRegression(random_state=0)
classifier_lr.fit(train_x,train_y)


classifier_lr2 = LogisticRegression(random_state=0)
classifier_lr2.fit(train_x_2,train_y)


predict_y = classifier_lr.predict(test_x)

predict_y_2 = classifier_lr2.predict(test_x_2)

from sklearn.metrics import confusion_matrix

print('gercek / PCAsiz')
conf_matrix = confusion_matrix(test_y,predict_y)
print(conf_matrix)


print("gercek / pca ile")
conf_matrix_2 = confusion_matrix(test_y,predict_y_2)
print(conf_matrix_2)


print('pcasiz ve pcali')
conf_matrix_3 = confusion_matrix(predict_y,predict_y_2)
print(conf_matrix_3)


from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

lda = LDA(n_components = 2)

train_x_lda = lda.fit_transform(train_x,train_y)
test_x_lda = lda.transform(test_x)


classifier_lr_lda = LogisticRegression(random_state=0)
classifier_lr_lda.fit(train_x_lda,train_y)


predict_y_lda = classifier_lr_lda.predict(test_x_lda)

print('lda ve orijinal')
conf_matrix_4 = confusion_matrix(predict_y,predict_y_lda)
print(conf_matrix_4)













