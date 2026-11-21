"""Resolve filled-subshell openings and reclosures by the actual source configurations."""
import csv
from pathlib import Path
import sys

DIR=Path(__file__).resolve().parent
sys.path.insert(0,str(DIR.parents[1]/'batch11/independent'))
from assign_openings import occupation


def read(path):
    with path.open() as f:
        return list(csv.DictReader(f))


def scan():
    states={(int(r['Z']),int(r['q'])):r['ground_shells'] for r in read(DIR/'asd_states_20261121.csv')}
    data=read(DIR/'rungs_detailed.csv')
    out=[]
    for r in data:
        n,k=int(r['Z']),int(r['k'])
        if not k:
            continue
        b=states[n,k]
        a=states.get((n,k+1),'')
        before,after=occupation(b),occupation(a)
        for key,cap in [('4f',14),('5d',10)]:
            if before[key]==cap and after[key]<cap:
                event='opening'
            elif before[key]<cap and after[key]==cap:
                event='closure'
            else:
                continue
            survive=sum((before & after).values())
            reassign=sum((after-before).values())
            assert survive+reassign==n-k-1
            out.append([n,r['symbol'],k,key,event,b,a,r['ASD_earlier_loss'],r['ASD_later_loss'],
                        survive,reassign,r['z'],r['z_lo'],r['z_hi'],r['box_wall'],r['start_grade'],r['end_grade']])
    with (DIR/'subshell_events.csv').open('w',newline='') as f:
        w=csv.writer(f,lineterminator='\n')
        w.writerow(['Z','symbol','k','subshell','event_in_removal_k_plus_one','state_at_k','state_at_k_plus_one',
                    'previous_change','next_change','K_next','R_next','z','lower','upper','whole_box','start_grade','end_grade'])
        w.writerows(out)
    assert [(r[2],r[4]) for r in out if r[1]=='Os' and r[3]=='4f']==[(12,'opening'),(13,'closure'),(14,'opening')]
    assert [(r[1],r[2]) for r in out if r[3]=='5d' and r[4]=='opening']==[('Au',1),('Hg',2)]
    assert all(r[14]=='inside' for r in out)
    print('4f/5d opening and closing rows',len(out))
    for r in out:
        print(r[1],r[2],r[3],r[4],r[8],r[9],r[10],r[11])


if __name__=='__main__':
    scan()
