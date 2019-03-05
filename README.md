# AccentComparison
Accent Comparison From Pitch

# Data Statistics
## Total Statistics
Number of recordings  148
Total duration of data 46:36:57.26
Size of data (numpy files only)  78M	
Size of recordings 14G	
## west
Number of recordings  51
Total duration of data 09:13:55.38
Size of data (numpy files only) 16M	
Size of recordings 2,7G	
## skane
Number of recordings  26
Total duration of data 06:34:45.97
Size of data (numpy files only) 12M	
Size of recordings 1,8G	
## norwegian
Number of recordings  25
Total duration of data 11:39:47.27
Size of data (numpy files only) 20M	
Size of recordings 3,5G	
## danish
Number of recordings  46
Total duration of data 19:08:28.64
Size of data (numpy files only) 32M	
Size of recordings 5,7G	

# The Script for Pitch Extraction

The list of sound files from where to perform the extraction should be in a file called "list.txt".
Then call the script. As output you will get 2 files, one with extension .f0 containing the information about the pitch, and another one having extension .frm that contains the informations about formants.

The information abouth the pitch can be in two formats, see [here](http://www.speech.kth.se/snack/man/snack2.2/tcl-man.html#spitch)


 - [Manual](http://www.speech.kth.se/snack/man/snack2.2/tcl-man.html)
 - [Snack Homepage](http://www.speech.kth.se/snack/)
 - [Tcl/Tk scripting language](https://www.tcl.tk/software/tcltk/)
 - [Examples with Snack](https://www.speech.kth.se/snack/tutorial.html#gettingstarted)

# Preprocessing

Pitch values will be:
 - log scale
 - centered

Probablility of voicing:
 - untouched
 
Power (already in log scale):
 - untouched

If using only pitch won't be enough to make any conclusive arguments about our hypothesis that the neighboring dialects are more similar than the dialects spoken in more distant areas from each other, despite the corresponding dialects' belonging to different official languages, we will encorporate formants data as part of our features. This decision was based on the fact that after pitch varition the next most prominent feature characterizing a dialect is the differences in the pronunciation of the vowels, which would be captured by their respective formants.

# Classification

The classification can be performed using a recurrent neural network as it can deal with time series well. As a suggestion it is also possible to introduce a CNN as explored by [this paper](https://ieeexplore.ieee.org/document/8141873).

One particular flexible network could be the LSTM one, and for the setting of classification in Python we can refer to a tutorial [here](https://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/). 

Here is another [link](https://datascience.stackexchange.com/questions/32341/what-is-the-best-method-for-classification-of-time-series-datashould-i-use-lstm) still on the topic of LSTM networks.

[LSTM explaination](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

To use in python with Keras library we must start from this [page here ](https://keras.io/getting-started/sequential-model-guide/).
and [here](https://keras.io/layers/recurrent/)



# DATA

Dimensions : 

X -> (number of sequences in the dataset, number of samples per sequence, number of features : 1 if only pitch)

y -> (number of sequences in the dataset) : 0 or 1


# Results

30 epochs, 200sec, 10 loops, globaly normalized

skane danish 			59.1% +/- 3.6% 
west norwegian			58.8% +/- 4.5% (20 epoch, 5 loops)
west skane 				63.5% +/- 4.6% 
danish norwegian


30 epochs, 50sec, 10 loops, sequencialy normalized

skane danish 			56.1% +/- 2.6%
west norwegian		
west skane 			
danish norwegian
