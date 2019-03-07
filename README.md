# AccentComparison
Accent Comparison From Pitch

# Data Statistics
## Total Statistics
Number of recordings  148</br>
Total duration of data 46:36:57.26</br>
Size of data (numpy files only)  78M	</br>
Size of recordings 14G	</br>
## west
Number of recordings  51</br>
Total duration of data 09:13:55.38</br>
Size of data (numpy files only) 16M	</br>
Size of recordings 2,7G	</br>
## skane
Number of recordings  26</br>
Total duration of data 06:34:45.97</br>
Size of data (numpy files only) 12M	</br>
Size of recordings 1,8G	</br>
## norwegian
Number of recordings  25</br>
Total duration of data 11:39:47.27</br>
Size of data (numpy files only) 20M	</br>
Size of recordings 3,5G	</br>
## danish
Number of recordings  46</br>
Total duration of data 19:08:28.64</br>
Size of data (numpy files only) 32M	</br>
Size of recordings 5,7G	</br>

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

###### 30 epochs, 200sec, 10 loops, globaly normalized

 - skane danish 			59.1% +/- 3.6% </br>
 - west norwegian		57.0% +/- 5.1% 	<!--previously 58.8% +/- 4.5% (20 epoch, 5 loops) --></br>
 - west skane 				63.5% +/- 4.6% </br>
 - danish norwegian 67.2% +/- 6.2%</br>

###### 30 epochs, 200sec, 10 loops, sequencialy normalized


 - skane danish 			58.2% +/- 3.8%</br>
 - west norwegian		69.35%  +/- 2.5%</br>
 - west skane	65.1%  +/- 1.1%</br>
 - danish norwegian 56.3% +/- 3.8%</br>
 

###### 30 epochs, 50sec, 10 loops, sequencialy normalized


 - skane danish 			56.1% +/- 2.6%</br>
 - west norwegian		56.6%  +/- 4.2%</br>
 - west skane	49.3%  +/- 6.1%</br>      
 - danish norwegian 49.4% +/- 6.0 %</br>
 
 ###### 5 epochs, 200sec, 10 loops, sequencialy normalized
 
 - skane danish 58.0 +/- 4.1%	</br>
 - west norwegian		69.6%  +/- 3.4% </br>
 - west skane  62.87% +/- 5.89% </br>
 - danish norwegian 57.7% +/- 3.7%</br>
 
 
 ##### Experiments
 ###### NO CONV
LSTM(64) + DENSE(2) -> skane danish 57.3 +/- 2.8%	</br>
LSTM(32) + DENSE(2) -> skane danish 49.4 +/- 6.0%	</br>

LSTM(64) + DENSE(2) -> skane danish 55.7 +/- 7.5%	</br>
LSTM(32) + DENSE(2) -> skane danish 53.1 +/- 10.3%	</br>
###### NO LSTM
CONV + DENSE(128) + DENSE(2) -> skane west 71.3 +/- 3.1%	</br>
0.5\*CONV + DENSE(128) + DENSE(2) -> skane west 71.4 +/- 2.6%	</br>
0.25\*CONV + DENSE(128) + DENSE(2) -> skane west 69.9 +/- 3.7%	</br>
0.25\*CONV + DENSE(256) + DENSE(64) + DENSE(2) -> skane west 72.1 +/- 4.1%	</br>
CONV + DENSE(64) + DENSE(2) -> skane west 69.8 +/- 3.6%	</br>
CONV + DENSE(256) + DENSE(64) + DENSE(2) -> skane west 67.0 +/- 6.2%	</br>

CONV + DENSE(64) + DENSE(2) -> skane danish 60.7 +/- 3.8%	</br>

###### BOTH
LSTM(64) + CONV + DENSE(64) + DENSE(2) -> skane west 69.7 +/- 5.7%	</br>
LSTM(64) + CONV + DENSE(32) + DENSE(2) -> skane west 70.9 +/- 4.5%	</br>
LSTM(64) + DENSE(32) + DENSE(2) -> skane west 56.4 +/- 8.3%	</br>
LSTM(64) + CONV + DENSE(64) + DENSE(32) + DENSE(2) -> skane west 67.9 +/- 4.3%	</br>
LSTM(8) + 0.5\*CONV + DENSE(256) + DENSE(64) + DENSE(2) -> skane west 72.2 +/- 1.8%	</br>

LSTM(8) + 0.5\*CONV + DENSE(256) + DENSE(64) + DENSE(2) -> skane danish 61.1 +/- 2.7%	</br>

###### CONVOLUTION IN SERIES WITH LSTM
0.5\*CONV + LSTM(16) +  DENSE(256) + DENSE(64) + DENSE(2) -> skane west 67.0 +/- 3.8%	</br>


