#!/bin/bash

while read line
do
  echo "Downloading $line..."
  wget --directory-prefix=../swedish/skane/ -c $line
done < "../swedish/skane.txt"
