#!/bin/bash
# SCRIPT: BALLFILM2-RUN-01 (voice, cues, recording, narrator two at a time, compose)
cd /home/claude/ballfilm2
python3 make_voice.py > voice.log 2>&1 && python3 cues.py && python3 record.py > record.log 2>&1
( for s in knot outro; do python3 narrator_ball.py v_$s.wav narr_$s.mp4 cue_$s.json; done ) > rigA.log 2>&1 &
( for s in sum intro; do python3 narrator_ball.py v_$s.wav narr_$s.mp4 cue_$s.json; done ) > rigB.log 2>&1 &
wait
python3 compose.py > compose.log 2>&1; echo FINISHED >> compose.log
