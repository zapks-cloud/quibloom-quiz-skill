#!/bin/bash
# usage: fin.sh NN OutName.mp4
# Run from the video project dir that contains out/ (chunks out/vNN.c*.mp4
# and the mix out/vNN.wav). Joins chunks with stream copy (no re-encode),
# muxes AAC 192k audio, checks frame count, duration and sha256, and
# splits the master into 18 MB delivery parts under parts/.
set -e
n=$1; name=$2
mkdir -p final parts
rm -f out/concat$n.txt
for f in $(ls out/v$n.c*.mp4 | xargs -n1 basename); do echo "file '$PWD/out/$f'" >> out/concat$n.txt; done
echo chunks $(wc -l < out/concat$n.txt)
ffmpeg -y -loglevel error -f concat -safe 0 -i out/concat$n.txt -i out/v$n.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart final/$name
ffprobe -v error -count_frames -select_streams v -show_entries stream=nb_read_frames,width,height -of csv=p=0 final/$name
ffprobe -v error -show_entries stream=codec_type,duration -of csv=p=0 final/$name
sha256sum final/$name
stat -c %s final/$name
split -b 18000000 -d final/$name parts/$name.part
ls parts | grep $name
