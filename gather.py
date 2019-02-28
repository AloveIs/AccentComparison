import numpy as np
import os
from random import shuffle


# This function extract the data and return it as an array of shape [N_sequences, N_samples, N_features]

# folder should be the name of the dialec from where you want to extract the data 
# feature should be the liste of features names (pitch, voice or pwr)
# N_sample is the number of samples in a sequence (1 sample = 0.05s)
# N_lim is the maximum number of sequences from the same speaker (can be useful to limit the bias)
# verbose enable to print the number of sequences extracted from each file

def gather(folder, features = ["pitch"], N_samples=200, N_lim = 1000, verbose=False) :
    data_split = []
    for j,f in enumerate(features) :
        #read data  
        with open(os.path.join(folder,"name_list.txt")) as file :
            data = [np.load(os.path.join(folder,line[:-1]+f+".npy")) for line in file]
        
        #split data into as many sequences as possible
        data_split.append([])
        for d in data :
            i = 0
            while i*N_samples < d.size-N_samples and i < N_lim :
                data_split[j].append(d[i:i+N_samples])
                i+= 1
            if verbose :
                print("cut into",i,"sequences")

       
    N_features = len(features)         
    N_sequences = len(data_split[0])

    #put into an numpy array with right indices
    array = np.zeros((N_sequences, N_samples, N_features))
    for i in range(N_sequences) :
        for j in range(N_samples) :
            for k in range(N_features) :
                array[i,j,k] = data_split[k][i][j]

    #return mixed mix sequences
    indexes = list(range(N_sequences))
    shuffle(indexes)
    return array[indexes,:,:]



#run to see how many sequences can be obtained
if __name__ == '__main__':
    for dialect in ["norwegian", "skane", "danish", "west"] :
        data = gather(dialect, [ "pitch", "voice", "pwr" ], verbose = True)
        print(dialect, ':', data.shape)