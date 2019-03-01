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
        data1 = gather(label1, ["pitch"])
        data2 = gather(label2, ["pitch"])
        if balance:
            n = min(len(data1), len(data2))
            data1 = data1[:n,:, :]
            data2 = data2[:n,:, :]
        X = np.concatenate((data1, data2))
        y = np.concatenate(([1] * len(data1), [0] * len(data2)))
        print(label1 + " Dataset : ", data1.shape)
        print(label2 + " Dataset : ", data2.shape)
    
    ## Shuffle and split the data to train validation and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle = True)
    
    print(len(X_train), 'train sequences', len(X_test), 'test sequences')
    print('X_train shape:', X_train.shape)
    print('X_test shape:', X_test.shape)
    print('y_train shape:', y_train.shape)
    print('y_test shape:', y_test.shape)

    return X_train,  X_test,y_train, y_test