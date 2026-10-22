/* independent brute-force reference: a_n by smallest-prime-factor sieve, a_p by naive counting */
#include "ap.h"
int main(int argc,char**argv){
  double Tf=atof(argv[1]); u64 m=strtoull(argv[2],0,10);
  long double X=(long double)m*sqrtl((long double)6503188012738584ULL);
  u64 T=(u64)(Tf*X); double c2=(double)(2.0L*3.14159265358979323846264338327950288L/X);
  u64 *spf=calloc(T+1,8); i64 *a=calloc(T+1,8); i64 *apv=calloc(T+1,8);
  for(u64 i=2;i<=T;i++) if(!spf[i]){ for(u64 j=i;j<=T;j+=i) if(!spf[j]) spf[j]=i; apv[i]=ap_naive(i); }
  a[1]=1;
  for(u64 n=2;n<=T;n++){ u64 p=spf[n],r=n; int e=0; while(r%p==0){r/=p;e++;}
    int bad=(p==2||p==3||p==2243||p==4547||p==5843);
    i64 a0=1,a1=apv[p]; for(int j=1;j<e;j++){ i64 nx= bad? a1*apv[p] : apv[p]*a1-(i64)p*a0; a0=a1;a1=nx;} a[n]=a[r]*a1; }
  long double S[400]={0};
  for(u64 n=1;n<=T;n++) if(a[n]) S[n%m]+=(long double)a[n]/n*expl(-(long double)n*c2);
  printf("T %lu\n",T); for(u64 b=0;b<m;b++) printf("S %lu %lu %.24Le\n",m,b,S[b]);
}
