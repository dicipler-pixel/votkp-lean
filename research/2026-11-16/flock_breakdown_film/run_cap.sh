#!/bin/bash
# SCRIPT: RUN_CAP_V1 — records the five scenes one after another
cd /home/claude/balls/film/v1
for s in s12 s3 s4 s5 s6; do python3 -I ../work/p/capture_p.py $s.json > cap_$s.log 2>&1; done
echo done > cap_all.done
