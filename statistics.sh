#!/bin/bash
echo "# Data Statistics"
echo "## Total Statistics"
echo "Number of recordings  $(ls -w1 ./*/*.wav | wc -l)"
echo "Total duration of data $(soxi -Td ./*/*.wav)"
echo "Size of data (numpy files only)  $(du -hc ./*/*.npy | tail -1| head -c4)"
echo "Size of recordings $(du -hc ./*/*.wav|tail -1| head -c4)"

for element in west skane norwegian danish
do
  echo "## $element"
  cd $element;
  echo "Number of recordings  $(ls -w1 *.wav | wc -l)"
  echo "Total duration of data $(soxi -Td *.wav)"
  echo "Size of data (numpy files only) $(du -hc ./*.npy | tail -1| head -c4)"
  echo "Size of recordings $(du -hc ./*.wav|tail -1| head -c5)"
  cd ..;
done


