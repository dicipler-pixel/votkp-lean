# SCRIPT: L4-RUN-SWEEP2 (driver: runs every line of jobs2.txt through l4_sync_02.js, two at a time, appends to sweep2.jsonl)
import subprocess, json, shlex
from concurrent.futures import ThreadPoolExecutor
jobs=[shlex.split(l)[0] for l in open('jobs2.txt')]
def run(j):
    return subprocess.run(['node','l4_sync_02.js',j],capture_output=True,text=True).stdout.strip()
with ThreadPoolExecutor(2) as ex, open('sweep2.jsonl','w') as f:
    for out in ex.map(run,jobs):
        f.write(out+'\n'); f.flush()
