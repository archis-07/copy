# -*- coding: utf-8 -*-
"""DL-boston.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gFaADeJFyWDpZspJ7vtO51itGzA7gIOg
"""

from google.colab import drive
drive.mount("/content/gdrive")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("/content/gdrive/MyDrive/Prac_datasets/boston.csv")

data.head()

x= data.iloc[:,:-1]
y= data.MEDV

y.shape

from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=42)

from sklearn.linear_model import LinearRegression
lr =LinearRegression()

lr.fit(x_train, y_train)

y_pred=lr.predict(x_test)

from sklearn.metrics import r2_score
acc = r2_score(y_test, y_pred)
print(acc)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

from keras.models import Sequential
from keras.layers import Dense

model= Sequential()
model.add(Dense(128, activation ='relu', input_dim = 13))
model.add(Dense(64, activation = 'relu'))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(16, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(x_train,y_train, batch_size = 42, epochs = 200)

y2_pred= model.predict(x_test)

print(r2_score(y_test, y2_pred))