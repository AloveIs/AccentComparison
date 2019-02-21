#!/bin/bash

url='http://www.tekstlab.uio.no/glossa2/media/ndc/audio/'

while read line
do
  echo "Downloading $line..."
  wget --directory-prefix=../$1/ -c $url$line.mp3
done < "../$1/download_list.txt"
