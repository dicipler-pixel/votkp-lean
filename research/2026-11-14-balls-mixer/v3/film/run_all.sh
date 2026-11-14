#!/bin/bash
# SCRIPT: BALLFILM-RUN-01 (voice must be finished; then record every segment, render the narrator two at a time, compose)
cd /home/claude/ballfilm
while pgrep -f make_voice.py >/dev/null; do sleep 5; done
python3 cues.py && python3 record.py > record.log 2>&1
( for s in field close thomas chain; do python3 narrator_ball.py v_$s.wav narr_$s.mp4 cue_$s.json; done ) > rigA.log 2>&1 &
( for s in pair line tree intro outro; do python3 narrator_ball.py v_$s.wav narr_$s.mp4 cue_$s.json; done ) > rigB.log 2>&1 &
wait
python3 compose.py > compose.log 2>&1; echo FINISHED >> compose.log
