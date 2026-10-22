#include "ap_dbg.h"
#include <time.h>
int main(){
  bsgs_ws W; ws_init(&W);
  u64 start = 70000000000ULL, len=4000000; char *c=calloc(len,1);
  for(u64 d=2; d*d<start+len; d++){ u64 s=(start+d-1)/d*d; for(u64 m=s;m<start+len;m+=d) c[m-start]=1; }
  int cnt=0; double sum=0; struct timespec t0,t1; clock_gettime(CLOCK_MONOTONIC,&t0);
  for(u64 i=0;i<len && cnt<50000;i++){ if(c[i]) continue; u64 p=start+i; int ok; i64 b=ap_bsgs(p,&W,&ok); if(!ok) printf("FAIL %lu\n",p); sum+=b; cnt++; }
  clock_gettime(CLOCK_MONOTONIC,&t1);
  double el=(t1.tv_sec-t0.tv_sec)+(t1.tv_nsec-t0.tv_nsec)*1e-9;
  printf("%d primes: %.2f us, calls/prime %.3f\n",cnt,el/cnt*1e6,(double)g_calls/cnt);
}
