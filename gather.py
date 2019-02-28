import numpy as np
import os


def gather(folder, features = ["pitch"], N_samples=200) :
    data_split = []
    for j,f in enumerate(features) : 
        with open(os.path.join(folder,"name_list.txt")) as file :
            data = [np.load(os.path.join(folder,line[:-1]+f+".npy")) for line in file]
        
        data_split.append([])
        for d in data :
            i = 0
            while i < d.size-N_samples :
                data_split[j].append(d[i:i+N_samples])
                i+= N_samples
       
    N_features = len(features)         
    N_sequences = len(data_split[0])

    array = np.zeros((N_sequences, N_samples, N_features))
    for i in range(N_sequences) :
        for j in range(N_samples) :
            for k in range(N_features) :
                array[i,j,k] = data_split[k][i][j]
    return array


if __name__ == '__main__':
    data = gather("norwegian", [ "pitch", "voice", "pwr" ])
    print(data.shape)