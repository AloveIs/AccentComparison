#!/bin/bash

for element in west skane norwegian danish
do
  echo "Extractiong for: $element ..."
  cd $element;
  ./../scripts/extract_filenames.sh;
  ls --width=1 *.wav > list.txt;
  ./../scripts/extract_pitch.sh;
  python3 ./../scripts/preprocessing.py < name_list.txt;
  echo "done"
  cd ..;
done
