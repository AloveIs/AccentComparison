#!/bin/bash
echo "Downloading recordings in Swedish, Danish and Norwegian"
sh ./download_from_lab.sh west
sh ./download_from_lab.sh skane

sh ./download_from_lab.sh danish
sh ./download_from_lab.sh norwegian
echo "All recordings downloaded"
