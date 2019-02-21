#!/bin/bash

while read line
do
  echo "Downloading $line..."
  wget --directory-prefix=../swedish/ -c $line
done < "../swedish/audio_urls_clean.txt"
