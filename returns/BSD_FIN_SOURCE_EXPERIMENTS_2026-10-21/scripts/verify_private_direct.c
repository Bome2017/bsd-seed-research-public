/* Independent direct-product verification of the private-support certificate. */
#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
int main(int argc,char **argv){
 if(argc!=3)return 2;
 FILE *in=fopen(argv[1],"r"),*cert=fopen(argv[2],"r");if(!in||!cert)return 3;
 size_t n;if(fscanf(in,"%zu",&n)!=1||!n)return 4;
 mpz_t *a=malloc(n*sizeof(mpz_t));if(!a)return 5;
 mpz_t P,g,priv,mod,r,h,tmp;mpz_inits(P,g,priv,mod,r,h,tmp,NULL);mpz_set_ui(P,1);
 for(size_t i=0;i<n;i++){mpz_init(a[i]);if(mpz_inp_str(a[i],in,10)==0||mpz_sgn(a[i])<=0)return 6;mpz_mul(P,P,a[i]);}
 for(size_t i=0;i<n;i++){
  if(mpz_inp_str(g,cert,10)==0||mpz_inp_str(priv,cert,10)==0)return 7;
  if(mpz_cmp_ui(priv,1)<=0||!mpz_divisible_p(a[i],priv))return 8;
  mpz_mul(mod,a[i],priv);mpz_mod(r,P,mod);
  if(!mpz_divisible_p(r,a[i]))return 9;
  mpz_divexact(tmp,r,a[i]);mpz_gcd(h,priv,tmp);
  if(mpz_cmp_ui(h,1)!=0){fprintf(stderr,"private witness fails at %zu\n",i);return 10;}
 }
 printf("PASS_DIRECT_PRODUCT_VERIFIER rows=%zu GMP=%s\n",n,gmp_version);
 for(size_t i=0;i<n;i++){mpz_clear(a[i]);}
 free(a);mpz_clears(P,g,priv,mod,r,h,tmp,NULL);fclose(in);fclose(cert);return 0;
}
