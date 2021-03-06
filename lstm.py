from __future__ import print_function
import numpy as np

from sklearn.model_selection import train_test_split

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam

from gather import gather

### Seed for reproductibility
np.random.seed(123)


### Hyperparameters
batch_size = 1
hidden_units = 16
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

    elif label=="west_skane":
        #data1 = gather("norwegian", ["pitch", "voice", "pwr"])#N_sequences, N_samples, N_features
        #data2 = gather("west", ["pitch", "voice", "pwr"])
        data1 = gather("skane", ["pitch"])
        data2 = gather("west", ["pitch"])[:12, : , :]
        X = np.concatenate((data1, data2))
        y = np.concatenate(([1] * len(data1), [0] * len(data2)))
        #y_label = np.concatenate((np.ones(data1.shape[0]), -1 * np.ones(data2.shape[0])))
        print("Skåne Dataset : ", data1.shape)
        print("Western Sweden Dataset : ", data2.shape)
        ## Shuffle and split the data to train validation and test
        X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle = True)


    elif label=="west":
        data1 = gather("skane", ["pitch", "voice", "pwr"])
        data2 = gather("danish", ["pitch", "voice", "pwr"])
        

    else:
        data1 = gather("skane", ["pitch", "voice", "pwr"])
        data2 = gather("west", ["pitch", "voice", "pwr"])


    print(len(X_train), 'train sequences', len(X_test), 'test sequences')
    print('X_train shape:', X_train.shape)
    print('X_test shape:', X_test.shape)
    print('y_train shape:', y_train.shape)
    print('y_test shape:', y_test.shape)
    #print(y_test)

    return X_train,  X_test,y_train, y_test


def train_model(X_train, X_test, y_train, y_test):
    print('Preprocessing...')
    
    print("Mean of training set : ", np.mean(X_train))    
    #print("Mean of validation set : ", np.mean(X_val)) 
    print("Mean of test set : ", np.mean(X_test)) 
    
    print('Build model...')

    Y_train = np_utils.to_categorical(np.clip(y_train, 0, 1), nb_classes)
    #Y_val = np_utils.to_categorical(np.clip(y_val, 0, 1), nb_classes)
    Y_test = np_utils.to_categorical(np.clip(y_test, 0, 1), nb_classes)
    


    ### LSTM
    model = Sequential()
    model.add(LSTM(hidden_units, 
                   batch_input_shape = (batch_size, X_train.shape[1], X_train.shape[2]), 
                   kernel_initializer = 'random_uniform' ))


    ### Classification
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))


    ### Learning algorithm
    model.compile(loss='binary_crossentropy', optimizer=Adam(lr = 0.001), metrics=['accuracy'])


    ### Training and evualuation
    print("Training ...")
    model.fit(X_train, Y_train,
              batch_size=batch_size, epochs=10,
              validation_split = 1./6,
              #validation_data=(X_val, Y_val), 
              #callbacks = [EarlyStopping(patience = 2, verbose = 1)],
              verbose = 1)
    [score, acc] = model.evaluate(X_test, Y_test,
                                batch_size=batch_size,
                                verbose = 0)
    #prediction = model.predict(X_test, batch_size = batch_size)
    #print(prediction)
    print('Test score : %.3f' % score)
    print('Test accuracy : %.2f %%' % (acc*100))
    #print('Test accuracy: %.2f %%' % (100 - len(y_test[np.nonzero(np.argmax(prediction, axis = 1) - y_test)]) *100 / 50))
    
if __name__ == "__main__":
    #X_train, X_val, X_test, y_train, y_val, y_test = get_data("test")
    X_train, X_test, y_train, y_test = get_data("west_skane")
    train_model(X_train, X_test, y_train, y_test)
