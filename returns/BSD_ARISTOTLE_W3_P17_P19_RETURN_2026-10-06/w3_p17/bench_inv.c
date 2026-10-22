#include "ap.h"
#include <time.h>
int main(){ mont_t M; mont_init(&M, 70000000001ULL+2); u64 x=12345, acc=0; struct timespec t0,t1;
 clock_gettime(CLOCK_MONOTONIC,&t0); for(int i=0;i<1000000;i++){ x=inv_plain(x+1, M.p); acc+=x;} clock_gettime(CLOCK_MONOTONIC,&t1);
 printf("inv %.1f ns\n",((t1.tv_sec-t0.tv_sec)*1e9+(t1.tv_nsec-t0.tv_nsec))/1e6);
 clock_gettime(CLOCK_MONOTONIC,&t0); for(int i=0;i<10000000;i++){ x=m_mul(&M,x,x+1); } clock_gettime(CLOCK_MONOTONIC,&t1);
 printf("mul latency %.2f ns %lu\n",((t1.tv_sec-t0.tv_sec)*1e9+(t1.tv_nsec-t0.tv_nsec))/1e7, x+acc);}
