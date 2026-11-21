"""Download both PseudoDojo norm-conserving potentials from a fixed public mirror."""
import argparse
from pathlib import Path
from urllib.request import urlopen
from hashlib import sha256
from run_nc import HASHES

PIN='33528761f31e0e3a5d6c875f6174a17e69eb86e9'
ROOT=f'https://raw.githubusercontent.com/Quantum-MultiScale/KSPP/{PIN}/norm-conserving/nc-sr-04/PBE/standard/upf'
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('pps',type=Path);d=p.parse_args().pps
    d.mkdir(exist_ok=True,parents=True)
    for el,digest in HASHES.items():
        data=urlopen(f'{ROOT}/{el}.upf',timeout=60).read()
        if sha256(data).hexdigest()!=digest:
            raise ValueError(f'{el} checksum mismatch.')
        (d/f'{el}.upf').write_bytes(data)
        print(el,digest)
