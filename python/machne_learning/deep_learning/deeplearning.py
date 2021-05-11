# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:48:25 2020
#   title
#   Begin
#   End

@author: User
"""
import pandas as pd
import numpy as np


#   Loading data_set
#   Begin
data_set = pd.read_csv('Churn_Modelling.csv')

#   End

#   Separating data_set  as X and Y
#   Begin
data_X = data_set.iloc[:,3:13].values
print(data_X.shape)
data_Y = data_set.iloc[:,13:].values
#   End


#   Converting categorical_data as numeric
#   Begin
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
data_X[:,1] = label_encoder.fit_transform(data_X[:,1])
data_X[:,2] = label_encoder.fit_transform(data_X[:,2])

from sklearn.preprocessing import OneHotEncoder
one_hot_encoder = OneHotEncoder(categorical_features=[1])
data_X = one_hot_encoder.fit_transform(data_X[:,1:]).toarray()
#   End



#   Separating data_X and data_Y as train_X,text_X, train_Y and test_Y
#   Begin
from sklearn.model_selection import train_test_split
(train_X,test_X,train_Y,test_Y) = train_test_split(data_X,data_Y,
                                test_size=0.30,random_state=0)
#   End



#   Scaling train_X and test_X with StandartScaler
#   Begin
from sklearn.preprocessing import StandardScaler

StandardScaler = StandardScaler()
train_scaled_X = StandardScaler.fit_transform(train_X)
test_scaled_X = StandardScaler.fit_transform(test_X)
#   End



#   Creating Model
#   Begin
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()

model.add(Dense(6,activation='relu',kernel_initializer='uniform',input_dim=10))
model.add(Dense(6,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(optimizer='adam',loss='binary_crossentropy',
              metrics=['accuracy'])
model.summary()
#   End



#   Training model
#   Begin
model.fit(train_scaled_X,train_Y,epochs=50)
predict_Y = model.predict(test_scaled_X)
predict_Y = (predict_Y > 0.5)
#   End

#   Confusion Matrix
#   Begin
from sklearn.metrics import confusion_matrix
conf_matrix = confusion_matrix(test_Y,predict_Y)
print(conf_matrix)
#   End

