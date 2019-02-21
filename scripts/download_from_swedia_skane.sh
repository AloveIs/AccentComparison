#!/bin/bash

while read line
do
  echo "Downloading $line..."
  wget --directory-prefix=../skane/ -c $line
done < "../skane/skane.txt"
