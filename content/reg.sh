#!/bin/sh
# usage: reg.sh N id=file ...   (clip names without .wav, WAVs in ./clips)
# Builds clips/cN/ with hook.wav, cta.wav and vNN_<id>.wav for video N.
n=$1; shift
v=$(printf v%02d $n)
C=clips/c$n; mkdir -p $C
cp clips/c1/hook.wav clips/c1/cta.wav $C/
for pair in "$@"; do id=${pair%%=*}; f=${pair#*=}; cp "clips/$f.wav" "$C/${v}_$id.wav"; done
ls $C | wc -l
