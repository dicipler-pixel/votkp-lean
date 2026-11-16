# SCRIPT: NEVER-TURN-03
# Predictions read off the nine-crossing census (NEVER-TURN-02) and written BEFORE this run:
#  family A  [a, 2, 2] with a odd:            17/5, 27/5 never  -> predict 37/7 [7,2,2]... i.e. p/q = a + 2/5: 37/5, 47/5 NEVER
#  family B  [a, 1, 1, 2] with a even:        13/5, 23/5 never  -> predict 33/5, 43/5 NEVER
#  family C  [a, m, 2]: m even never, m odd turns (17/5, 29/9 never; 23/7 turns) -> predict 41/13 [3,6,2], 47/9 [5,4,2] NEVER; 35/11 [3,5,2], 53/11? TURN
#  family D  golden [2,1^n,2]: n = 2, 5 never; n = 0, 3 turn -> predict n = 8 (233/89) NEVER, n = 6 (89/34) TURN
# Kill for each family: one member on the wrong side.
import mpmath as mp
exec(open('/home/claude/work/never_turn_02.py').read().split('rows=[]')[0].replace('MAXC=int(sys.argv[1])','MAXC=0'))
tests=[('A',37,5,'NEVER'),('A',47,5,'NEVER'),('B',33,5,'NEVER'),('B',43,5,'NEVER'),
       ('C',41,13,'NEVER'),('C',47,9,'NEVER'),('C',35,11,'TURN'),('C',45,7,'NEVER'),('C',31,9,'TURN'),
       ('D',89,34,'TURN'),('D',233,89,'NEVER')]
for fam,p,q,pred in tests:
    f=turns(p,q); got='NEVER' if f is None else 'TURN'
    print('family %s  %d/%d  cf %s  predicted %-5s  got %-5s %s'%(fam,p,q,cf(p,q),pred,got,'ok' if got==pred else 'WRONG'),flush=True)
