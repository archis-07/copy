# -*- coding: utf-8 -*-
"""Practical2 (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wzg0Zkiq5b9BjvCALr2IH9aWyPKsEiBI
"""

from tensorflow.keras.datasets import imdb

(train_data, train_label), (test_data, test_label) = imdb.load_data(num_words = 10000)

import numpy as np

def vectorize_sequences(sequences, dimensions = 10000):
  results = np.zeros((len(sequences), dimensions))
  for i,sequence in enumerate(sequences):
    results[i, sequence] = 1
  return results

x_train = vectorize_sequences(train_data)
y_train = vectorize_sequences(test_data)

y_train = np.asarray(train_label).astype('float32')
y_test = np.asarray(test_label).astype('float32')

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(16, input_shape=(10000, ), activation = "relu"))
model.add(Dense(16, activation = "relu"))
model.add(Dense(1, activation = "sigmoid"))

model.compile(optimizer='adam', loss = 'mse', metrics = ['accuracy'])

model.summary()

history = model.fit(x_train, y_train, validation_split = 0.3, epochs = 10, verbose = 1, batch_size = 512)

from sklearn.metrics import accuracy_score
x_test = vectorize_sequences(test_data)
y_pred = model.predict(x_test)
y_pred = [1 if pred > 0.5 else 0 for pred in y_pred]
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

