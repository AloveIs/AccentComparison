import numpy as np
import sys
import pickle as pk



if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.exit()

    name = sys.argv[1]

    f = open(name, "rb")
    a = pk.load(f)
    print("Lenghts is " , len(a))
    print("mean is : "+  str(np.mean(a)))
    print("std_dev is : ", np.sqrt(np.var(a)))
