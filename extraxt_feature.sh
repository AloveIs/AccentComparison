#!/bin/bash

for element in west skane norwegian danish
do
  echo "##### Extraction for: $element ..."
  cd $element;
  
  # check if there are some mp3 and in case convert them
  if ls | grep '*.mp3'; then
    echo "$element:\t converting mp3 files"
    ./../scripts/convert.sh;
    rm -f *.mp3;
  fi

  # extract filenames with and without extension
  ./../scripts/extract_filenames.sh;
  ls --width=1 *.wav > list.txt;

  # perform the extraction of all the feature
  # from the .wav files
  echo -e "$element:\t extract feature"
  ./../scripts/extract_pitch.sh;

  echo -e "$element:\t preprocess"
  # apply the preprocessing to the data
  python3 ./../scripts/preprocessing.py < name_list.txt;

  echo "##### Finished with $element"
  cd ..;
done
