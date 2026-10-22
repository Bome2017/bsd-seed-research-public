#include "ap.h"
#include <time.h>
static int isprime(u64 n){ if(n<2) return 0; for(u64 d=2;d*d<=n;d++) if(n%d==0) return 0; return 1; }
int main(int argc,char**argv){
  bsgs_ws W; ws_init(&W);
  u64 lim = argc>1? strtoull(argv[1],0,10):300000;
  long bad=0, n=0;
  for(u64 p=5;p<lim;p+=2){ if(!isprime(p)||p==2243||p==5843||p==4547) continue;
    i64 a=ap_naive(p); int ok; i64 b=ap_bsgs(p,&W,&ok);
    if(!ok||a!=b){ bad++; if(bad<10) printf("MISMATCH p=%lu naive=%ld bsgs=%ld ok=%d\n",p,a,b,ok);} n++; }
  printf("compared %ld primes, mismatches %ld\n",n,bad);
  /* benchmark near 7e10 */
  u64 start = 70000000000ULL; int cnt=0; double sum=0;
  struct timespec t0,t1; clock_gettime(CLOCK_MONOTONIC,&t0);
  for(u64 p=start+1; cnt<20000; p+=2){ if(!isprime(p)) continue; int ok; i64 b=ap_bsgs(p,&W,&ok); if(!ok){printf("FAIL %lu\n",p);} sum+=b; cnt++; }
  clock_gettime(CLOCK_MONOTONIC,&t1);
  double el=(t1.tv_sec-t0.tv_sec)+(t1.tv_nsec-t0.tv_nsec)*1e-9;
  printf("bench: %d primes near 7e10 in %.3f s (incl. trial-division primality) => %.2f us/prime; mean a_p %.2f\n",cnt,el,el/cnt*1e6,sum/cnt);
}
