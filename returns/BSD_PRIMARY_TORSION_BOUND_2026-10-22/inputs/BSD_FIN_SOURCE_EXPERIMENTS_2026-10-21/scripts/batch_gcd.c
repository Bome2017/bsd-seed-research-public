/* Exact product/remainder-tree batch GCD, using GMP. No factorization or guesses. */
#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
typedef struct {size_t n; mpz_t *v;} Level;
static mpz_t *allocz(size_t n){mpz_t *a=malloc(n*sizeof(mpz_t));if(!a){perror("malloc");exit(2);}for(size_t i=0;i<n;i++)mpz_init(a[i]);return a;}
static void freez(mpz_t *a,size_t n){for(size_t i=0;i<n;i++)mpz_clear(a[i]);free(a);}
int main(void){
 size_t n;if(scanf("%zu",&n)!=1||!n)return 2;
 Level t[64];t[0].n=n;t[0].v=allocz(n);
 for(size_t i=0;i<n;i++)if(mpz_inp_str(t[0].v[i],stdin,10)==0||mpz_sgn(t[0].v[i])<=0)return 3;
 int levels=1;
 while(t[levels-1].n>1){
   size_t k=t[levels-1].n;t[levels].n=(k+1)/2;t[levels].v=allocz(t[levels].n);
   for(size_t i=0;i<k;i+=2){if(i+1<k)mpz_mul(t[levels].v[i/2],t[levels-1].v[i],t[levels-1].v[i+1]);else mpz_set(t[levels].v[i/2],t[levels-1].v[i]);}
   levels++;
 }
 mpz_t *rem=allocz(1);mpz_set(rem[0],t[levels-1].v[0]);size_t nr=1;
 mpz_t sq,g,quot,priv,h;mpz_inits(sq,g,quot,priv,h,NULL);
 for(int l=levels-2;l>=0;l--){
   mpz_t *next=allocz(t[l].n);
   for(size_t i=0;i<t[l].n;i++){mpz_mul(sq,t[l].v[i],t[l].v[i]);mpz_mod(next[i],rem[i/2],sq);}
   freez(rem,nr);rem=next;nr=t[l].n;
 }
 for(size_t i=0;i<n;i++){
   if(!mpz_divisible_p(rem[i],t[0].v[i])){fprintf(stderr,"remainder divisibility failed\n");return 4;}
   mpz_divexact(quot,rem[i],t[0].v[i]);mpz_gcd(g,quot,t[0].v[i]);
   mpz_set(priv,t[0].v[i]);
   for(;;){mpz_gcd(h,priv,g);if(mpz_cmp_ui(h,1)==0)break;mpz_divexact(priv,priv,h);}
   mpz_out_str(stdout,10,g);putchar(' ');mpz_out_str(stdout,10,priv);putchar('\n');
 }
 fprintf(stderr,"GMP_VERSION=%s;ROWS=%zu;STATUS=COMPLETE\n",gmp_version,n);
 for(int l=0;l<levels;l++)freez(t[l].v,t[l].n);
 freez(rem,nr);mpz_clears(sq,g,quot,priv,h,NULL);return 0;
}
