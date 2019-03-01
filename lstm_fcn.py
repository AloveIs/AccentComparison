from __future__ import print_function
import numpy as np

from keras.models import Model
from keras.utils import np_utils
from keras.engine.input_layer import Input
from keras.layers import Dropout, BatchNormalization, Conv1D, GlobalAveragePooling1D, Concatenate
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM
from keras.callbacks import EarlyStopping, TensorBoard
from keras.optimizers import Adam

from get_data import get_data


### Seed for reproductibility
np.random.seed(123)


### Hyperparameters
batch_size = 20
hidden_units = 128


def generate_model(shape):
    
    print('Build model...')

    
    
    ####### Generating the model #########
    inp = Input(shape = (shape,1))


    ### LSTM part
    ls = LSTM(hidden_units)(inp)
    ls = Dropout(0.8)(ls)
    
    
    ### Convolutional part    
    conv = Conv1D(128, 8, padding='same')(inp)
    conv = BatchNormalization()(conv)
    conv = Activation('relu')(conv)
    
    conv = Conv1D(256, 5, padding='same')(conv)
    conv = BatchNormalization()(conv)
    conv = Activation('relu')(conv)
    
    conv = Conv1D(128, 3, padding='same')(conv)
    conv = BatchNormalization()(conv)
    conv = Activation('relu')(conv)
    
    conv = GlobalAveragePooling1D()(conv)
    
    
    ### Concatenation and FC network
    out = Concatenate()([conv, ls])
    out = Dense(2, activation = 'softmax')(out)
    
    
    model = Model(inp, out)


    ### Learning algorithm
    model.compile(loss='binary_crossentropy', optimizer=Adam(lr = 0.001), metrics=['accuracy'])
    
    return model


def train_model(model, X_train, X_test, y_train, y_test): 
    
    ### Preprocessing
    print('Preprocessing...')
    print("Mean of training set : ", np.mean(X_train))    
    #print("Mean of validation set : ", np.mean(X_val)) 
    print("Mean of test set : ", np.mean(X_test)) 
    Y_train = np_utils.to_categorical(np.clip(y_train, 0, 1), 2)
    #Y_val = np_utils.to_categorical(np.clip(y_val, 0, 1), nb_classes)
    Y_test = np_utils.to_categorical(np.clip(y_test, 0, 1), 2)
    
    ### Callbacks
    esCallBack = EarlyStopping(patience = 2, verbose = 1, restore_best_weights = True)
    tbCallBack = TensorBoard(log_dir='./logs', histogram_freq=0,     #To visualize the created files :
                             write_graph=True, write_images=True)    #tensorboard --logdir path_to_current_dir/logs 
 

    ### Training and evualuation
    print("Training ...")
    model.fit(X_train, Y_train,
              batch_size=batch_size, epochs=10,
              validation_split = 0.2,
              #validation_data=(X_val, Y_val), 
              callbacks = [esCallBack, tbCallBack],
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
    #X_train, X_test, y_train, y_test = get_data("test")
    X_train, X_test, y_train, y_test = get_data("west", "skane", balance = True)
    #model = generate_model(X_train.shape[1])
    train_model(model, X_train, X_test, y_train, y_test)
