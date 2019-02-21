#!/bin/bash
echo "Downloading recordings in Swedish, Danish and Norwegian"
sh ./download_from_swedia_skane.sh
sh ./download_from_swedia_west.sh
sh ./download_from_tekstlab.sh
echo "All recordings downloaded"