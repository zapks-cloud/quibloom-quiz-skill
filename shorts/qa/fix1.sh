#!/bin/bash
# usage: fix1.sh VID NAME(e.g. D11-2-Dinosaurs) QNUM  (reveal already edited in video json)
v=$1; n=$2; q=$3; cd /tmp/t/rp2; export QUIBLOOM_LOGO=/tmp/t/rp2/quibloom-logo.png
cp out/v$v.tl.json /tmp/v$v.tl.old
python3 main2.py /tmp/t/video$v.json /tmp/t/c$v out/v$v mix|tail -1; cmp out/v$v.tl.json /tmp/v$v.tl.old && echo tl_same
read s e <<<$(python3 -c "
import json;d=json.load(open('out/v$v.tl.json'));sc=[x for x in d['scenes'] if x[0]=='q'][$q-1]
rv=sc[1]+d['opt'][$q-1][1]['rev'];print(int(rv*30)-30,int(sc[2]*30)+1)")
for a in $(seq 0 900 6000); do if [ $a -lt $e ] && [ $((a+900)) -gt $s ]; then python3 main2.py /tmp/t/video$v.json /tmp/t/c$v out/v$v chunk $a $((a+900)) >/dev/null 2>&1; echo chunk $a; fi; done
bash fin.sh $v Quibloom-Short-$n-5Q-native.mp4 2>&1|tail -1
python3 chk.py $v final/Quibloom-Short-$n-5Q-native.mp4
