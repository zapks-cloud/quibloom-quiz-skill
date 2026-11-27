#!/bin/bash
# usage: pack.sh VID NAME QNUM...  (frames of reveals)
v=$1; n=$2; shift 2; cd /tmp/t/rp2; export QUIBLOOM_LOGO=/tmp/t/rp2/quibloom-logo.png
M=final/Quibloom-Short-$n-5Q-native.mp4
python3 qa2.py $v Quibloom-Short-$n-5Q-native.mp4 >/dev/null 2>&1
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames,width,height -of csv=p=0 $M; ffprobe -v error -show_entries format=duration,size -of csv=p=0 $M; ffmpeg -v error -i $M -f null - && echo decode_ok; sha256sum $M
rm -rf /downloads/p$v; mkdir /downloads/p$v; cp parts/*$n-5Q-native*part0* /downloads/p$v/; (cd /downloads/p$v; ls; sha256sum *; cat *part* | sha256sum)
for q in "$@"; do python3 - $v $n $q <<'PY'
import json,subprocess,sys
v,n,q=sys.argv[1:4]
d=json.load(open(f'/tmp/t/rp2/out/v{v}.tl.json'))
s=[x for x in d['scenes'] if x[0]=='q'][int(q)-1]
subprocess.run(['ffmpeg','-v','error','-y','-ss',str(s[2]-0.4),'-i',f'/tmp/t/rp2/final/Quibloom-Short-{n}-5Q-native.mp4','-frames:v','1',f'/downloads/p{v}_q{q}_reveal_full.png'])
PY
done; ls /downloads/p${v}_*
