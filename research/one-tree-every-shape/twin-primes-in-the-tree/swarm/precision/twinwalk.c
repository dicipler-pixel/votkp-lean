/* SCRIPT: TWIN-WALK-SL2C-01
 * Segmented sieve over k (numbers 6k-1, 6k+1), streams twin starts a=6k-1 in [lo,hi),
 * multiplies SL(2,C) boosts B_s(r)=exp(r sigma_s/2), r=ln(a'/a), s from end digit of a' (1->x,7->y,9->z),
 * for consecutive starts INSIDE the chunk (boundary steps are added by the combiner).
 * Long double (80-bit) arithmetic. At every checkpoint X (grid 10^(j/40)) it prints the partial product
 * through the first start >= X, plus partial sums sum r, sum r^2, sum r*1[s]. Nothing stored but base primes.
 * Kill conditions (checked downstream in combine.py): (K1) combined turn at 1e8 must equal 12.204756 deg
 * to 1e-6 and at 1e9 12.269506 to 1e-6 (harness 40-digit values); (K2) |det M - 1| < 1e-12 at the end of
 * every chunk; (K3) twin counts pi2(1e9)=3424506, pi2(1e10)=27412679 (known values, incl. (3,5),(5,7)).
 * usage: twinwalk lo hi > file
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
typedef long double LD;
static LD M[8]; /* a=M0+iM1, b=M2+iM3, c=M4+iM5, d=M6+iM7 */
static void mulB(int s, LD r){
  LD ch=coshl(r/2), sh=sinhl(r/2); LD a[8]; memcpy(a,M,sizeof a);
  if(s==0){ /* [[ch,sh],[sh,ch]] */
    for(int row=0;row<2;row++){ LD *x=a+4*row; LD *y=M+4*row;
      y[0]=x[0]*ch+x[2]*sh; y[1]=x[1]*ch+x[3]*sh; y[2]=x[0]*sh+x[2]*ch; y[3]=x[1]*sh+x[3]*ch; }
  } else if(s==1){ /* [[ch,-i sh],[i sh,ch]] : col0 = x0*ch + x1col*(i sh); col1 = x0*(-i sh)+x1*ch */
    for(int row=0;row<2;row++){ LD *x=a+4*row; LD *y=M+4*row;
      /* (u+iv)*(i sh) = -v sh + i u sh */
      y[0]=x[0]*ch - x[3]*sh; y[1]=x[1]*ch + x[2]*sh;
      y[2]=x[1]*sh + x[2]*ch; y[3]=-x[0]*sh + x[3]*ch; }
  } else { LD ep=expl(r/2), em=expl(-r/2);
    for(int row=0;row<2;row++){ LD *y=M+4*row; y[0]*=ep; y[1]*=ep; y[2]*=em; y[3]*=em; }
  }
}
int main(int argc,char**argv){
  uint64_t lo=strtoull(argv[1],0,10), hi=strtoull(argv[2],0,10);
  uint64_t K0=(lo+1+5)/6, K1=(hi+1+5)/6; /* k with 6k-1 in [lo,hi): k>=ceil((lo+1)/6) */
  if(K0<2)K0=2;
  uint64_t lim=(uint64_t)sqrtl((LD)(6*K1+2))+2;
  char *bs=calloc(lim+1,1); uint32_t *pr=malloc(sizeof(uint32_t)*(lim/2+10)); uint64_t np=0;
  for(uint64_t i=2;i<=lim;i++) if(!bs[i]){ if(i>=5) pr[np++]=i; for(uint64_t j=i*i;j<=lim;j+=i) bs[j]=1; }
  uint64_t *nA=malloc(8*np), *nB=malloc(8*np);
  for(uint64_t t=0;t<np;t++){ uint64_t p=pr[t]; uint64_t inv=0; for(uint64_t v=1;v<p;v++) if((6*v)%p==1){inv=v;break;}
    /* 6k-1==0 -> k==inv ; 6k+1==0 -> k==p-inv */
    uint64_t rA=inv, rB=p-inv; uint64_t kA=K0+((rA+p-K0%p)%p), kB=K0+((rB+p-K0%p)%p);
    if(6*kA-1==p) kA+=p; if(6*kB+1==p) kB+=p; nA[t]=kA; nB[t]=kB; }
  const uint64_t S=1<<19; unsigned char *A=malloc(S), *B=malloc(S);
  /* checkpoints */
  static LD gridX[600]; int ng=0; for(int j=0;j<=520;j++){ LD X=powl(10.0L,(LD)j/40.0L); if(X>=lo && X<hi) gridX[ng++]=X;
    if(j%40==0){ LD Y=3.0L*powl(10.0L,(LD)(j/40)); if(Y>=lo && Y<hi) gridX[ng++]=Y; } }
  for(int u=1;u<ng;u++) for(int v=u;v>0 && gridX[v]<gridX[v-1];v--){ LD t=gridX[v]; gridX[v]=gridX[v-1]; gridX[v-1]=t; }
  int gi=0;
  memset(M,0,sizeof M); M[0]=1; M[6]=1;
  uint64_t first=0, prev=0, nsteps=0, cnt=0; LD sr=0, sr2=0, W[3]={0,0,0}; uint64_t C[3]={0,0,0};
  for(uint64_t base=K0;base<K1;base+=S){
    uint64_t len=(K1-base<S)?K1-base:S; memset(A,1,len); memset(B,1,len);
    for(uint64_t t=0;t<np;t++){ uint64_t p=pr[t]; if((uint64_t)p*p>6*(base+len)+1) break;
      uint64_t k=nA[t]; if(k<base) k+=((base-k+p-1)/p)*p; while(k<base+len){ A[k-base]=0; k+=p;} nA[t]=k;
      k=nB[t]; if(k<base) k+=((base-k+p-1)/p)*p; while(k<base+len){ B[k-base]=0; k+=p;} nB[t]=k; }
    for(uint64_t i=0;i<len;i++) if(A[i]&B[i]){
      uint64_t a=6*(base+i)-1; cnt++;
      if(!first){ first=a; prev=a; }
      else { LD r=log1pl((LD)(a-prev)/(LD)prev); int d=a%10; int s=(d==1)?0:(d==7)?1:2;
        mulB(s,r); nsteps++; sr+=r; sr2+=r*r; W[s]+=r; C[s]++; prev=a; }
      while(gi<ng && (LD)a>=gridX[gi]){
        printf("CP %.6Lf %llu %llu %llu",gridX[gi],(unsigned long long)a,(unsigned long long)cnt,(unsigned long long)nsteps);
        for(int q=0;q<8;q++) printf(" %.21Le",M[q]);
        printf(" %.21Le %.21Le %.21Le %.21Le %.21Le %llu %llu %llu\n",sr,sr2,W[0],W[1],W[2],
          (unsigned long long)C[0],(unsigned long long)C[1],(unsigned long long)C[2]);
        gi++; }
    }
  }
  /* note: un-hit checkpoints (no start >= X inside chunk) belong to next chunk */
  LD dr=(M[0]*M[6]-M[1]*M[7])-(M[2]*M[4]-M[3]*M[5]), di=(M[0]*M[7]+M[1]*M[6])-(M[2]*M[5]+M[3]*M[4]);
  printf("END %llu %llu %llu %llu",(unsigned long long)first,(unsigned long long)prev,(unsigned long long)cnt,(unsigned long long)nsteps);
  for(int q=0;q<8;q++) printf(" %.21Le",M[q]);
  printf(" %.21Le %.21Le %.21Le %.21Le %.21Le %llu %llu %llu\n",sr,sr2,W[0],W[1],W[2],
    (unsigned long long)C[0],(unsigned long long)C[1],(unsigned long long)C[2]);
  fprintf(stderr,"det-1 = %.3Le %+.3Le i\n",dr-1,di);
  return 0;
}
