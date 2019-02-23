from __future__ import print_function
import numpy as np

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM

from gather import gather

### Seed for reproductibility
np.random.seed(1234)


### Hyperparameters
batch_size = 10
hidden_units = 32
nb_classes = 2

### Data
def get_data(label):
    print('Loading data...')
    if label=="test":
        train_data = np.genfromtxt('toy_data/ECG200_TRAIN.tsv',delimiter='\t')
        y_train = train_data[:,0]
        X_train = train_data[:,1:]

        test_data = np.genfromtxt('toy_data/ECG200_TEST.tsv',delimiter='\t')
        y_test = test_data[:,0]
        X_test = test_data[:,1:]
        
        X_val = X_test[:50, :]
        X_test = X_test[:50, :]
        
        y_val = y_test[:50]
        y_test = y_test[50:]

    elif label=="south":
        #data1 = gather("norwegian", ["pitch", "voice", "pwr"])#N_sequences, N_samples, N_features
        #data2 = gather("west", ["pitch", "voice", "pwr"])
        data1 = gather("norwegian", ["pitch"])
        data2 = gather("west", ["pitch"])
        data = np.concatenate((data1, data2))
        y_label = np.concatenate((np.ones(data1.shape[0]), -1 * np.ones(data2.shape[0])))
        print(data1.shape, data2.shape, data.shape)
        ## shuffle and split the data to train validation and test


    elif label=="west":
        data1 = gather("skane", ["pitch", "voice", "pwr"])
        data2 = gather("danish", ["pitch", "voice", "pwr"])

    else:
        data1 = gather("skane", ["pitch", "voice", "pwr"])
        data2 = gather("west", ["pitch", "voice", "pwr"])


    print(len(X_train), 'train sequences', len(X_val), 'validation sequences', len(X_test), 'test sequences')
    print('X_train shape:', X_train.shape)
    print('X_test shape:', X_test.shape)
    print('y_train shape:', y_train.shape)
    print('y_test shape:', y_test.shape)
    #print(y_test)

    return X_train[:, :, np.newaxis], X_val[:, :, np.newaxis], X_test[:, :, np.newaxis],y_train, y_val, y_test


def train_model(X_train, X_val, X_test, y_train,y_val, y_test):
    print('Build model...')

    Y_train = np_utils.to_categorical(y_train, nb_classes)
    Y_val = np_utils.to_categorical(y_val, nb_classes)
    Y_test = np_utils.to_categorical(y_test, nb_classes)
    


    ### LSTM
    model = Sequential()
    model.add(LSTM(hidden_units, batch_input_shape = (batch_size, X_train.shape[1], X_train.shape[2]) ))


    ### Classification
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))


    ### Learning algorithm
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


    ### Training and evualuation
    print("Training ...")
    model.fit(X_train, Y_train, batch_size=batch_size, epochs=5, validation_data=(X_val, Y_val), verbose = 1)
    '''[score, acc] = model.evaluate(X_test, Y_test,
                                batch_size=batch_size,
                                verbose = 1)'''
    prediction = model.predict(X_test, batch_size = batch_size)
    #print('Test score:', score)
    print('Test accuracy:', 1 - len(np.nonzero(np.argmax(prediction, axis = 1) - y_test)[0]) / 50)
    
if __name__ == "__main__":
    X_train, X_val, X_test, y_train, y_val, y_test = get_data("test")
    #X_train, X_val, X_test, y_train, y_val, y_test = get_data("south")
    #train_model(X_train, X_val, X_test, y_train, y_val, y_test)
