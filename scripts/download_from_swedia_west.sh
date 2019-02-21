#!/bin/bash

while read line
do
  echo "Downloading $line..."
  wget --directory-prefix=../west/ -c $line
done < "../west/west.txt"
