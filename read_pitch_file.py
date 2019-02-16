import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

def file_process(file):
    data = np.genfromtxt(file, delimiter=' ')

    # print(data)

    plt.plot(data[:,0])
    plt.show()


def main_args():

    for file in sys.argv[1:]:
        file_process(file)

def main_stdin():

    for file in sys.stdin:
        print(file[:-1])
        file_process(file[:-1])


if __name__ == "__main__":

    if len(sys.argv) > 1:
        main_args()
    else:
        main_stdin()
