/* SCRIPT: RELATION_SEARCH
   usage: ./relation_search gensfile n dmax
   KILL CONDITION (written before the run): the search reports FOUND if (a) two distinct non-backtracking words of
   length n or n-1 (n-1 vs n included) give the same matrix mod p (hash of all 16 entries) -> relation candidate,
   later verified exactly in Python; or (b) a non-backtracking word of length <= dmax maps e0 to e0 mod p.
   If nothing is found the groups survive this search up to relation length 2n (collision search) and dmax (origin search).
   Positive control: gens_ctrl.txt contains B_i(4)=B_i(2)^2, so the search MUST report a relation of length 3.
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u64;
static const u64 P = 2147483647ULL; /* 2^31-1 */
static int NL; static u64 G[12][16]; static u64 CK[16];
static u64 pw(u64 a,u64 e){u64 r=1;a%=P;while(e){if(e&1)r=r*a%P;a=a*a%P;e>>=1;}return r;}
typedef struct {u64 key; u64 code;} Rec;  /* code = len<<56 | base-NL digits */
static Rec *R; static size_t nR=0, capR=0; static int N;
static void push(u64 key,u64 code){ if(nR==capR){capR=capR?capR*2:1<<20;R=realloc(R,capR*sizeof(Rec));if(!R){fprintf(stderr,"oom\n");exit(1);}} R[nR].key=key;R[nR].code=code;nR++; }
static u64 hashm(const u64*M){u64 k=0;for(int j=0;j<16;j++)k+=M[j]*CK[j];return k;}
static void mulm(const u64*A,const u64*B,u64*C){
  for(int i=0;i<4;i++)for(int j=0;j<4;j++){
    u64 s=A[i*4]*B[j]+A[i*4+1]*B[4+j]+A[i*4+2]*B[8+j]+A[i*4+3]*B[12+j]; /* each <2^62, sum of 4 < 2^64 */
    C[i*4+j]=s%P; } }
static void dfs(int depth,const u64*M,int last,u64 code){
  if(depth>=N-1){ push(hashm(M),((u64)depth<<56)|code); }
  if(depth==N) return;
  for(int l=0;l<NL;l++){ if(depth>0 && l==(last^1)) continue;
    u64 C[16]; mulm(M,G[l],C); dfs(depth+1,C,l,code*NL+l); } }
static int cmp(const void*a,const void*b){u64 x=((Rec*)a)->key,y=((Rec*)b)->key;return x<y?-1:x>y;}
static int dmax; static long long nodes=0, fixed=0;
static u64 E0v[4];
/* origin search: prepend letters; vector v = (word) e0, 4 entries */
static void dfs2(int depth,const u64*v,int first,u64 code){
  nodes++;
  if(depth>0 && v[0]==1 && v[1]==0 && v[2]==0 && v[3]==0){ fixed++; if(fixed<=10) printf("ORIGIN-FIXED len %d code(base %d, leftmost last digit) %llu\n",depth,NL,(unsigned long long)code); }
  if(depth==dmax) return;
  for(int l=0;l<NL;l++){ if(depth>0 && l==(first^1)) continue;
    u64 w[4]; for(int i=0;i<4;i++){ u64 s=0; for(int j=0;j<4;j++) s+=G[l][i*4+j]*v[j]; w[i]=s%P; }
    dfs2(depth+1,w,l,code+ (u64)l*0 + 0) ; } }
int main(int argc,char**argv){
  FILE*f=fopen(argv[1],"r"); N=atoi(argv[2]); dmax=atoi(argv[3]);
  if(fscanf(f,"%d",&NL)!=1) return 1;
  for(int l=0;l<NL;l++){ long long D; if(fscanf(f,"%lld",&D)!=1) return 1; u64 iD=pw((u64)D%P,P-2);
    for(int j=0;j<16;j++){ long long q; if(fscanf(f,"%lld",&q)!=1) return 1; long long qm=((q%(long long)P)+(long long)P)%(long long)P; G[l][j]=(u64)qm*iD%P; } }
  u64 s=88172645463325252ULL; for(int j=0;j<16;j++){ s^=s<<13;s^=s>>7;s^=s<<17; CK[j]=s|1; }
  u64 I[16]={0}; for(int i=0;i<4;i++) I[i*5]=1;
  dfs(0,I,-1,0);
  qsort(R,nR,sizeof(Rec),cmp);
  long long ncoll=0; size_t i=0;
  while(i<nR){ size_t j=i; while(j<nR && R[j].key==R[i].key) j++;
    if(j-i>1){ ncoll++; if(ncoll<=10){ printf("COLLISION group:"); for(size_t t=i;t<j&&t<i+4;t++){ printf(" [len %d code %llu]",(int)(R[t].code>>56),(unsigned long long)(R[t].code&((1ULL<<56)-1))); } printf("\n"); } }
    i=j; }
  printf("records %zu (lengths %d and %d), collision groups %lld\n",nR,N-1,N,ncoll);
  /* origin search */
  u64 e[4]={1,0,0,0}; dfs2(0,e,-1,0);
  printf("origin search nodes %lld, origin-fixing nonbacktracking words (len<=%d) mod p: %lld\n",nodes,dmax,fixed);
  return 0; }
