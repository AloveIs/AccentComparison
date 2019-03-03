from gather import gather

import numpy as np
from sklearn.model_selection import train_test_split

def get_data(label1, label2 = "", balance = False):
    print('Loading data...')
    if label1=="test":
        train_data = np.genfromtxt('toy_data/ECG200_TRAIN.tsv',delimiter='\t')
        y_train = train_data[:,0]
        X_train = train_data[:,1:][:,:, np.newaxis]

        test_data = np.genfromtxt('toy_data/ECG200_TEST.tsv',delimiter='\t')
        y_test = test_data[:,0]
        X_test = test_data[:,1:][:,:, np.newaxis]

    else: 
        #data1 = gather("norwegian", ["pitch", "voice", "pwr"])#N_sequences, N_samples, N_features
        #data2 = gather("west", ["pitch", "voice", "pwr"])
        data1_train, data1_val, data1_test = gather(label1, ["pitch"], N_lim=200, divide = [64,16,20])
        data2_train, data2_val, data2_test = gather(label2, ["pitch"], N_lim=200, divide = [64,16,20])
        if balance:
            n = min(len(data1_train), len(data2_train))
            data1_train = data1_train[:n,:, :]
            data2_train = data2_train[:n,:, :]
            n = min(len(data1_val), len(data2_val))
            data1_val = data1_val[:n,:, :]
            data2_val = data2_val[:n,:, :]
            n = min(len(data1_test), len(data2_test))
            data1_test = data1_test[:n,:, :]
            data2_test = data2_test[:n,:, :]

        X_train = np.concatenate((data1_train, data2_train))
        y_train = np.concatenate(([1] * len(data1_train), [0] * len(data2_train)))
        X_val = np.concatenate((data1_val, data2_val))
        y_val = np.concatenate(([1] * len(data1_val), [0] * len(data2_val)))
        X_test = np.concatenate((data1_test, data2_test))
        y_test = np.concatenate(([1] * len(data1_test), [0] * len(data2_test)))
        print(label1 + " Dataset : ", data1_train.shape, data1_val.shape, data1_test.shape)
        print(label2 + " Dataset : ", data2_train.shape, data2_val.shape, data2_test.shape)
    
    ## Shuffle and split the data to train validation and test
    ##X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle = True)
    
    index = np.arange(len(X_train))
    np.random.shuffle(index)
    X_train = X_train[index]
    y_train = y_train[index]

    index = np.arange(len(X_test))
    np.random.shuffle(index)
    X_test = X_test[index]
    y_test = y_test[index]

    index = np.arange(len(X_val))
    np.random.shuffle(index)
    X_val = X_val[index]
    y_val = y_val[index]

    print(len(X_train), 'train sequences', len(X_test), 'test sequences')
    print('X_train shape:', X_train.shape)
    print('X_val shape:', X_val.shape)
    print('X_test shape:', X_test.shape)
    print('y_train shape:', y_train.shape)
    print('y_val shape:', y_val.shape)
    print('y_test shape:', y_test.shape)

    return X_train,X_val,X_test,y_train,y_val,y_test