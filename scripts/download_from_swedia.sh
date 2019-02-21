#!/bin/bash

while read line
do
  echo "Downloading $line..."

  wget --directory-prefix=/swedish_audio/ -c $line
done < "../swedish/audio_urls_clean.txt"