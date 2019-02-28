#!/bin/bash
echo "Downloading recordings in Swedish, Danish and Norwegian"
#sh ./download_from_lab.sh west
#sh ./download_from_lab.sh skane

echo "skane"
sh ./download_from_swedia_skane.sh
echo "west"
sh ./download_from_swedia_west.sh

echo "danish"
sh ./download_from_lab.sh danish
echo "norwegian"
sh ./download_from_lab.sh norwegian
echo "All recordings downloaded"
