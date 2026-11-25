// SCRIPT: STAR-COUNT-01
// Question (entry A1 of research/TWO_SESSIONS.md): on the 16 matrices of Mat_2(F_2), does any
// star with a centre and up to three legs, any grouping of the matrices onto the four nodes and
// any leg lengths theta >= 0, give D(2)^2/D(1)^2 above 5/3 ?
// KILL LINE (written in A1 before the run): a star above 5/3.
//
// WHY THE CHECK TESTS THE CLAIM.  In a star d(u,v) = 0 on the same node, theta_i between the
// centre and leg i, theta_i + theta_j between legs i and j.  So for each grouping the sum of d^2
// over rank-r pairs is a quadratic form theta^T Q_r theta with whole-number entries
// (Q_ii = pairs leaving leg i, Q_ij = pairs between legs i and j).  The ratio is above 5/3 for
// some theta >= 0 exactly when theta^T M theta < 0 somewhere on the positive octant, where
// M = 10 Q_1 - 9 Q_2 (unordered pairs: 72 of rank 1, 48 of rank 2, and (N2/48)/(N1/72) > 5/3
// iff 9 N2 > 10 N1).  "M is never negative on the positive octant" is copositivity, and for a
// 3 x 3 matrix Hadeler's criterion decides it in closed form.  Every grouping is visited once up
// to renaming the legs (depth-first, legs named in order of first use).
#include <stdio.h>
#include <math.h>
static int rk[16], lab[16];
static long long c[3][4], m[3][4][4];      // c[r][i]: centre-leg i pairs; m[r][i][j]: leg i - leg j pairs
static long long leaves=0, viol=0, border=0, unit_best_n=0, unit_best_d=1, unit_cnt=0;
static int viol_lab[16], have_viol=0;
static double worst=1e300;
static void upd(int k,int L,int s){        // add (s=+1) or remove (s=-1) matrix k with label L against matrices j<k
  for(int j=0;j<k;j++){ int r=rk[k^j], J=lab[j];
    if(L==J) continue;
    if(L==0) c[r][J]+=s; else if(J==0) c[r][L]+=s;
    else { int a=L<J?L:J, b=L<J?J:L; m[r][a][b]+=s; } } }
// returns -1 violation (not copositive), 0 borderline, +1 strictly copositive
static int hadeler(double M[4][4], double *q){
  double t=1e-9, lo=1e300, s[4];
  for(int i=1;i<=3;i++){ if(M[i][i]<-t) {*q=M[i][i]; return -1;} s[i]=sqrt(M[i][i]>0?M[i][i]:0); }
  for(int i=1;i<=3;i++) for(int j=i+1;j<=3;j++){ double v=M[i][j]+s[i]*s[j]; if(v<lo) lo=v; }
  if(lo<-t){*q=lo; return -1;}
  double det=M[1][1]*(M[2][2]*M[3][3]-M[2][3]*M[2][3])-M[1][2]*(M[1][2]*M[3][3]-M[2][3]*M[1][3])+M[1][3]*(M[1][2]*M[2][3]-M[2][2]*M[1][3]);
  double sum=M[1][2]*s[3]+M[1][3]*s[2]+M[2][3]*s[1]+s[1]*s[2]*s[3];
  if(det<-t && sum<-t){ *q=sum; return -1; }
  double edge = (det>sum?det:sum); if(edge<lo) lo=edge; *q=lo;
  return lo<t ? 0 : 1; }
static int classify(double *q){
  double M[4][4];
  for(int i=1;i<=3;i++){ long long q1=c[1][i], q2=c[2][i];
    for(int j=1;j<=3;j++) if(j!=i){ int a=i<j?i:j,b=i<j?j:i; q1+=m[1][a][b]; q2+=m[2][a][b]; }
    M[i][i]=(q1==0&&q2==0)?1.0:10.0*q1-9.0*q2; }   // an unused leg is given weight 1 so it cannot fake a tie
  for(int i=1;i<=3;i++) for(int j=i+1;j<=3;j++) M[i][j]=M[j][i]=10.0*m[1][i][j]-9.0*m[2][i][j];
  return hadeler(M,q); }
static void leaf(void){
  leaves++;
  long long n1=0,n2=0;
  for(int i=1;i<=3;i++){ n1+=c[1][i]; n2+=c[2][i]; for(int j=i+1;j<=3;j++){ n1+=4*m[1][i][j]; n2+=4*m[2][i][j]; } }
  if(n1>0){ if(n2*unit_best_d>unit_best_n*n1){unit_best_n=n2;unit_best_d=n1;unit_cnt=1;} else if(n2*unit_best_d==unit_best_n*n1) unit_cnt++; }
  double q; int k=classify(&q);
  if(k<0){ viol++; if(!have_viol){have_viol=1; for(int i=0;i<16;i++) viol_lab[i]=lab[i];} if(q<worst) worst=q; }
  else if(k==0) border++; }
static void dfs(int k,int used){
  if(k==16){ leaf(); return; }
  int top = used<3 ? used+1 : 3;
  for(int L=0;L<=top;L++){ lab[k]=L; upd(k,L,+1); dfs(k+1, L>used?L:used); upd(k,L,-1); } }
int main(void){
  for(int x=0;x<16;x++){ int a=x>>3&1,b=x>>2&1,cc=x>>1&1,d=x&1; rk[x]= x==0?0:(((a*d-b*cc)&1)?2:1); }
  // CONTROL: the known 5/3 star (rank-1 matrices on three legs by column space, the rest at the centre)
  for(int x=0;x<16;x++){ int a=x>>3&1,b=x>>2&1,cc=x>>1&1,d=x&1; int L=0;
    if(rk[x]==1){ int u0=a|b, u1=cc|d; L = (u0&&!u1)?1:((!u0&&u1)?2:3); }   // column space spanned by (u0,u1)
    lab[x]=L; upd(x,L,+1); }
  { long long n1=0,n2=0; for(int i=1;i<=3;i++){ n1+=c[1][i]; n2+=c[2][i]; for(int j=i+1;j<=3;j++){ n1+=4*m[1][i][j]; n2+=4*m[2][i][j]; } }
    double q; int k=classify(&q);
    printf("CONTROL known star: unit legs N2/N1 = %lld/%lld, ratio = %.6f (must be 1.666667); class = %d (must be 0, borderline), margin %.3g\n",
           n2,n1,(n2/48.0)/(n1/72.0),k,q); }
  for(int x=15;x>=0;x--) upd(x,lab[x],-1);
  dfs(0,0);
  printf("groupings visited (up to renaming legs): %lld\n",leaves);
  printf("unit legs: largest N2/N1 = %lld/%lld, ratio = %.6f, attained by %lld groupings\n",unit_best_n,unit_best_d,(unit_best_n/48.0)/(unit_best_d/72.0),unit_cnt);
  printf("free leg lengths: groupings above 5/3 (M not copositive): %lld ; groupings touching 5/3 exactly (borderline): %lld\n",viol,border);
  if(viol){ printf("most negative margin %.6g ; one violating grouping:",worst); for(int i=0;i<16;i++) printf(" %d",viol_lab[i]); printf("\n"); }
  printf(viol? "KILL LINE fired: a star above 5/3 exists\n" : "KILL LINE did not fire: no star with a centre and up to three legs is above 5/3\n");
  return 0; }
