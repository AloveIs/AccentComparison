import csv
import sys
import numpy as np
import matplotlib.pyplot as plt


# as input to this script you can pass the list of .f0 files
# to analize as inputs:
# 
# > python read_pitch_file.py file1.f0 file2.f0
#
# Or a stream in stdin using a file like f0_list.txt with all
# the names of the .f0 files to analyze:
#
# > python read_pitch_file-py < f0_list.txt




def file_process(file):

    data = np.genfromtxt(file,delimiter=' ')

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
