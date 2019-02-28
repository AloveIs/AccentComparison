#!/bin/sh

# print bitrate of the files in the 
# in the folders
echo "The dataset was recorded with these different rate (Hz):";

sox --i -r ./*/*.wav | uniq;
