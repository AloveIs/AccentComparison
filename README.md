# AccentComparison
Accent Comparison From Pitch


# The Script for Pitch Extraction

The list of sound files from where to perform the extraction should be in a file called "list.txt".
Then call the script. As output you will get 2 files, one with extension .f0 containing the information about the pitch, and another one having extension .frm that contains the informations about formanst.

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
 
Power(already in log scale):
 - untouched



# Classification

The classification can be performed using a recurrent neural network as it can deal with time series well. As a suggestion it is also possible to introduce a CNN as explored by [this paper](https://ieeexplore.ieee.org/document/8141873).

One particular flexible network could be the LSTM one, and for the setting of classification in Python we can refer to a tutorial [here](https://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/). 

Here is another [link](https://datascience.stackexchange.com/questions/32341/what-is-the-best-method-for-classification-of-time-series-datashould-i-use-lstm) still on the topic of LSTM networks.

[LSTM explaination](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

To use in python with Keras library we must start from this [page here ](https://keras.io/getting-started/sequential-model-guide/).
and [here](https://keras.io/layers/recurrent/)
