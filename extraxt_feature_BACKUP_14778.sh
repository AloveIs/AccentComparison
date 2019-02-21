#!/bin/bash

<<<<<<< HEAD
for element in west skane norwegian danish
=======

for element in swedish skane norwegian danish
>>>>>>> 9183cb481c0c8b6efced5226aa361f721a92ceac
do
  echo "Extractiong for: $element ..."
  cd $element;
  ./../scripts/convert.sh;
  rm -f *.mp3;
  ./../scripts/extract_filenames.sh;
  ls --width=1 *.wav > list.txt;
  ./../scripts/extract_pitch.sh;
  python3 ./../scripts/preprocessing.py < name_list.txt;
  echo "done"
  cd ..;
done
