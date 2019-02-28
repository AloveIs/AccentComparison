import csv
import sys
import numpy as np
import matplotlib.pyplot as plt


# as input to this script you can pass the list of the files
# names to analize as inputs, with no extension:
# 
# > python read_pitch_file.py TR1 TR2 
#
# Or a stream in stdin using a file like f0_list.txt with all
# the names of the files:
#
# > python read_pitch_file-py < name_list.txt

PADDING = 0.0001
BASE = 2


def process_power(file):
    data = np.genfromtxt(file + ".pwr",delimiter=' ')
    np.save(file+"pwr", data[1:-1])


def process_pitch(file):
    data = np.genfromtxt(file + ".f0",delimiter=' ')
    pitch = data[:,0]
    prob_voice = data[:,1]

    # compute log
    pitch = np.log(pitch+PADDING) / np.log(BASE)

    #center the pitch
    pitch = pitch - np.mean(pitch)


    np.save(file+"pitch", pitch)	
    np.save(file+"voice", prob_voice)	
	

def process_formants(file):
    pass

def file_process(file):

    process_power(file)
    process_pitch(file)
    process_formants(file)


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
