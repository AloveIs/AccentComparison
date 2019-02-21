#!/bin/bash

url='http://www.tekstlab.uio.no/glossa2/media/ndc/audio/'

while read line
do
  echo "Downloading $line..."

  wget -c $url$line.mp3
done < "./download_list.txt"