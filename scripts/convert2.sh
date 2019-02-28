
for i in *.mp3 ; do
    echo "############## $i";
    basename "$i" .mp3 ;
    ffmpeg -y -i "$i" $(basename "$i" .mp3).wav ;
done
