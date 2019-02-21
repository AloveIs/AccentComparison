#!/bin/bash

while read line
do
  echo "Downloading $line..."
  wget --directory-prefix=../swedish/west/ -c $line
done < "../swedish/west.txt"
