import numpy as np
import os


def gather(folder, features) :
    with open(os.path.join(folder,"name_list.txt")) as file :
        data = np.array([[np.load(os.path.join(folder,line[:-1]+f+".npy")) for f in features] for line in file])
    N_samples = min([d[0].shape[0] for d in data])
    print("cut each sequence to", N_samples, "samples")
    N_sequences, N_features = data.shape
    new_format = np.zeros((N_sequences, 814, N_features))
    for i in range(N_sequences) :
        for j in range(814) :
            for k in range(N_features) :
                new_format[i,j,k] = data[i,k][j]
    return new_format


if __name__ == '__main__':
    data = gather("norwegian", [ "pitch", "voice", "pwr" ])
    print(data.shape)