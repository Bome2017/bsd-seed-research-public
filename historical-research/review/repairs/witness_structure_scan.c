/* Supplemental check for the omitted distinct-factor condition in legacy wverify.
   Does NOT rerun group arithmetic or primality. Input hashes bind this check to
   the retained witness files. Uses <64 MiB address space per input segment. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#include <CommonCrypto/CommonDigest.h>
typedef uint64_t u64; typedef unsigned __int128 u128;
static u64 get64(const unsigned char *p){u64 x=0;for(int i=7;i>=0;i--)x=(x<<8)|p[i];return x;}
static u64 sq(u64 v){u64 r=0;for(int b=31;b>=0;b--){u64 t=r|((u64)1<<b);if((u128)t*t<=v)r=t;}return r;}
#define REQUIRE(a) do{if(!(a)){fprintf(stderr,"FAIL %s offset=%llu: %s\n",argv[1],(unsigned long long)o,#a);return 2;}}while(0)
int main(int argc,char **argv){
 if(argc!=2)return 1;int fd=open(argv[1],O_RDONLY);if(fd<0)return 1;
 struct stat st;if(fstat(fd,&st)||st.st_size<24||st.st_size>(1ULL<<26))return 1;
 size_t n=st.st_size;const unsigned char *p=mmap(NULL,n,PROT_READ,MAP_PRIVATE,fd,0);if(p==MAP_FAILED)return 1;
 size_t o=24;u64 lo=get64(p),hi=get64(p+8),num=get64(p+16),prev=0,maxq=0,maxD=0;unsigned maxk=0;
 REQUIRE(lo<hi && hi<=55046045696ULL);
 for(u64 i=0;i<num;i++){
  REQUIRE(o+14<=n);u64 q=get64(p+o);unsigned k=p[o+13];o+=14;
  REQUIRE(q>=4096 && q>=lo && q<hi && q>prev);prev=q;if(q>maxq)maxq=q;
  REQUIRE(o+9*k<=n);u64 ls[256];u128 D=1;u64 cap=q+1+sq(4*q);
  for(unsigned j=0;j<k;j++){
   u64 l=get64(p+o);unsigned e=p[o+8];o+=9;
   REQUIRE(l>=2 && e>=1);for(unsigned h=0;h<j;h++)REQUIRE(l!=ls[h]);ls[j]=l;
   for(unsigned h=0;h<e;h++){D*=l;REQUIRE(D<=cap);}
  }
  if(k>maxk)maxk=k;if((u64)D>maxD)maxD=(u64)D;
 }
 REQUIRE(o==n);unsigned char digest[32];CC_SHA256(p,(CC_LONG)n,digest);char hex[65];for(int i=0;i<32;i++)sprintf(hex+2*i,"%02x",digest[i]);
 printf("%s\t%llu\t%llu\t%llu\t%llu\t%u\t%llu\t%s\n",hex,(unsigned long long)n,(unsigned long long)lo,(unsigned long long)hi,(unsigned long long)num,maxk,(unsigned long long)maxD,argv[1]);
 munmap((void*)p,n);close(fd);return 0;
}
