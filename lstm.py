from __future__ import print_function
import numpy as np

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM

### Seed for reproductibility
np.random.seed(1234)


### Hyperparameters
batch_size = 5
hidden_units = 32
nb_classes = 2

### Data
print('Loading data...')
(X_train, y_train), (X_test, y_test) = GET_THE_DATA

print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)
print('y_train shape:', y_train.shape)
print('y_test shape:', y_test.shape)
print(y_test)
print('Build model...')

Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)


### LSTM
model = Sequential()
model.add(LSTM(hidden_units, batch_input_size = (50, X_train.shape[1], X_train.shape[2]) ))


### Classification
model.add(Dense(nb_classes))
model.add(Activation('softmax'))


### Learning algorithm
model.compile(loss='categorical_crossentropy', optimizer='adam')


### Training and evualuation
print("Training ...")
model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=3, validation_data=(X_test, y_test), show_accuracy=True)
score, acc = model.evaluate(X_test, y_test,
                            batch_size=batch_size,
                            show_accuracy=True)
print('Test score:', score)
print('Test accuracy:', acc)