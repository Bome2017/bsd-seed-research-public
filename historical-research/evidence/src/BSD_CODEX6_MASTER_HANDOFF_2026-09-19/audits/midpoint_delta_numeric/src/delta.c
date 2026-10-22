/* Bounded midpoint residual enclosure. The included upstream engine is used
   only for its exact coefficient reconstruction, input hashes, and tail_ms.
   See ../../MIDPOINT_DELTA_INTERVAL.md for every analytic error bound. */
#define main upstream_main
#include "/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19/src/arbcore.c"
#undef main
#include <time.h>
#include <math.h>

#define NT 150000000ULL
#define DEG 7
#define MAXBIN 4096
#define NG 20
#define PANELS 96
#define NF 24
#define TAIL_DEN 256
typedef struct { u64 lo, len; i128 m[8]; } Raw;
typedef struct { u64 lo, len; arb_struct center, cf[8], cq[8]; } Bin;
static Bin *bins; static long nb; static slong prec;
static int reuse128;
static arb_t cc, pp, kap, ltwo, rone, rbnd, rcbnd, rerr;
static arb_t dbnd, dcbnd, derr;
static arb_struct sig[NF+1], kn[NF+1];
static const u64 odd[8]={1,3,2243,6729,5843,17529,13105849,39317547};
static const int scale4[4]={1,2,4,8};
static int inv8[8], keep[8][4];

static void show(const char *name,const arb_t v) {
  printf("%s ",name); arb_printn(v,30,0); char *s=arb_dump_str(v);
  printf("\n%s_DUMP %s\n",name,s); flint_free(s); fflush(stdout);
}
static void set128(arb_t v,i128 x) {
  int neg=x<0; __uint128_t u=neg?-(__uint128_t)x:(__uint128_t)x;
  arb_set_ui(v,(u64)(u>>64)); arb_mul_2exp_si(v,v,64);
  arb_add_ui(v,v,(u64)u,prec); if(neg)arb_neg(v,v);
}
static void prepare(const char *path) {
  T=NT;SEGQ=1ULL<<24;RT=12247;NSEG=9;NBLK=36;
  APDIR="/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19/runs/seed150M/ap";
  /* Use the exact original decimal. */
  DISC=0; const char *ds="16586638656786071143743744";
  for(;*ds;ds++)DISC=DISC*10+(*ds-'0');
  small_primes();APSH=calloc(9,32);load_table(T);
  unsigned char dg[32],leaves[36][32];char hx[65];
  CC_SHA256(APSH,9*32,dg);hexs(dg,hx);printf("AP_ROOT %s\n",hx);
  if(strcmp(hx,"916155fe549e9323e8cdc63ecdbc8c190b6cfe9c9c2e6f7554c6a6214d4617f6"))fatal("ap custody mismatch");
  FILE *f=fopen(path,"wb");if(!f)fatal("moment output");
  u64 *rem=malloc(BLK*8);i64 *an=malloc(BLK*8);Raw v={0};
  u64 start=1,len=1,stop=2;long count=0;
  for(long b=0;b<NBLK;b++) {
    u64 lo=b*BLK+1,hi=lo+BLK;if(hi>T+1)hi=T+1;
    gen_block(lo,hi,rem,an,1);CC_SHA256(an,(CC_LONG)((hi-lo)*8),leaves[b]);
    for(u64 n=lo;n<hi;n++) {
      if(n==start){memset(&v,0,sizeof v);len=1+start/64;if(len>MAXBIN)len=MAXBIN;if(len>T+1-start)len=T+1-start;stop=start+len;v.lo=start;v.len=len;}
      i128 j=2*(i128)n-(2*(i128)start+len-1),pw=1,aa=an[n-lo];
      for(int k=0;k<8;k++){v.m[k]+=aa*pw;pw*=j;}
      if(n+1==stop){if(fwrite(&v,sizeof v,1,f)!=1)fatal("moment write");count++;start=stop;}
    }
  }
  fclose(f);CC_SHA256(leaves,36*32,dg);hexs(dg,hx);printf("AN_ROOT %s\nBINS %ld\n",hx,count);
  if(strcmp(hx,"8c0b71ccac2dd538d043ea34f4d4bbbf41459c72f7444371f43f7c58ded8cc94"))fatal("a_n independent root mismatch");
  free(rem);free(an);free(A);free(APK);free(SP);free(APSH);
}
static void readbins(const char *path) {
  FILE *f=fopen(path,"rb");if(!f)fatal("moment input");
  fseek(f,0,SEEK_END);long sz=ftell(f);rewind(f);if(sz%sizeof(Raw))fatal("moment size");nb=sz/sizeof(Raw);
  bins=calloc(nb,sizeof(Bin));Raw r;arb_t v,den,pow;arb_init(v);arb_init(den);arb_init(pow);u64 next=1;
  for(long j=0;j<nb;j++) {
    if(fread(&r,sizeof r,1,f)!=1)fatal("moment read");
    if(r.lo!=next||!r.len||r.len>MAXBIN||64*(r.len-1)>r.lo)fatal("bin geometry");next+=r.len;
    Bin *b=bins+j;b->lo=r.lo;b->len=r.len;arb_init(&b->center);arb_set_ui(&b->center,2*r.lo+r.len-1);arb_mul_2exp_si(&b->center,&b->center,-1);
    arb_set_ui(den,2*r.lo+r.len-1);arb_one(pow);
    for(int k=0;k<8;k++) {arb_init(b->cf+k);arb_init(b->cq+k);set128(v,r.m[k]);arb_div(b->cf+k,v,pow,prec);arb_fac_ui(v,k,prec);arb_div(b->cf+k,b->cf+k,v,prec);if(k%2)arb_neg(b->cf+k,b->cf+k);arb_mul(pow,pow,den,prec);}
    for(int k=7;k>=0;k--){arb_div(b->cq+k,b->cf+k,&b->center,prec);if(k<7){arb_mul_ui(v,b->cq+k+1,k+1,prec);arb_add(b->cq+k,b->cq+k,v,prec);}}
  }
  if(next!=NT+1)fatal("moment coverage");fclose(f);arb_clear(v);arb_clear(den);arb_clear(pow);
}
/* Geometric sums of n^j q^n, n>=1; a tail starts at L+1. */
static void geom(arb_t s0,arb_t s1,arb_t s2,const arb_t q,long L) {
  arb_t d,a,b,v;arb_init(d);arb_init(a);arb_init(b);arb_init(v);
  arb_one(d);arb_sub(d,d,q,prec);arb_div(s0,q,d,prec);
  arb_div(s1,s0,d,prec);arb_add_ui(v,q,1,prec);arb_mul(s2,s1,v,prec);arb_div(s2,s2,d,prec);
  if(L){arb_pow_ui(a,q,L,prec);arb_mul_ui(b,s0,L,prec);arb_add(b,b,s1,prec);
    arb_mul_ui(v,s1,2*L,prec);arb_add(s2,s2,v,prec);arb_mul_ui(v,s0,L*L,prec);arb_add(s2,s2,v,prec);
    arb_mul(s2,s2,a,prec);arb_mul(s1,b,a,prec);arb_mul(s0,s0,a,prec);}
  arb_clear(d);arb_clear(a);arb_clear(b);arb_clear(v);
}
static void residual_bound(arb_t out,const arb_t nu,long L) {
  arb_t x,q,s0,s1,s2,v;arb_init(x);arb_init(q);arb_init(s0);arb_init(s1);arb_init(s2);arb_init(v);
  arb_mul(x,pp,nu,prec);arb_mul_2exp_si(x,x,1);arb_neg(q,x);arb_exp(q,q,prec);geom(s0,s1,s2,q,L);
  arb_mul_ui(v,kap,5,prec);arb_addmul_ui(v,ltwo,12,prec);arb_mul(out,v,s1,prec);arb_addmul_ui(out,s2,5,prec);
  arb_mul_2exp_si(x,x,1);arb_div(s0,s0,x,prec);arb_addmul_ui(out,s0,5,prec);arb_mul_ui(out,out,8,prec);
  arb_clear(x);arb_clear(q);arb_clear(s0);arb_clear(s1);arb_clear(s2);arb_clear(v);
}
/* Bound d/du of the residual (u=log t). For x>=2*pi*nu*n>1,
   x*exp(-x) decreases. For complex x, |arg x|<=1/4 and sec(arg x)<25/24. */
static void derivative_bound(arb_t out,const arb_t nu,long L,int complex_bound) {
  arb_t x,q,s0,s1,s2,s3,d,v,w,pow;
  arb_init(x);arb_init(q);arb_init(s0);arb_init(s1);arb_init(s2);arb_init(s3);arb_init(d);arb_init(v);arb_init(w);arb_init(pow);
  arb_mul(x,pp,nu,prec);arb_mul_2exp_si(x,x,1);arb_one(v);if(!arb_gt(x,v))fatal("derivative monotonicity guard");
  arb_neg(q,x);arb_exp(q,q,prec);geom(s0,s1,s2,q,0);arb_one(d);arb_sub(d,d,q,prec);
  arb_sqr(v,q,prec);arb_addmul_ui(v,q,4,prec);arb_add_ui(v,v,1,prec);arb_mul(s3,q,v,prec);arb_pow_ui(v,d,4,prec);arb_div(s3,s3,v,prec);
  if(L){arb_pow_ui(pow,q,L,prec);arb_mul_ui(v,s2,3*L,prec);arb_add(s3,s3,v,prec);arb_mul_ui(v,s1,3*L*L,prec);arb_add(s3,s3,v,prec);arb_mul_ui(v,s0,L*L*L,prec);arb_add(s3,s3,v,prec);arb_mul(s3,s3,pow,prec);geom(s0,s1,s2,q,L);}
  arb_mul_ui(v,kap,5,prec);arb_addmul_ui(v,ltwo,12,prec);arb_mul(out,v,s2,prec);arb_addmul_ui(out,s3,5,prec);arb_mul(out,out,x,prec);
  if(complex_bound){arb_mul_ui(out,out,25,prec);arb_div_ui(out,out,24,prec);arb_addmul_ui(out,s1,10,prec);}
  else {arb_mul_ui(v,s1,15,prec);arb_mul_2exp_si(v,v,-1);arb_add(out,out,v,prec);}
  arb_mul_ui(out,out,8,prec);
  arb_clear(x);arb_clear(q);arb_clear(s0);arb_clear(s1);arb_clear(s2);arb_clear(s3);arb_clear(d);arb_clear(v);arb_clear(w);arb_clear(pow);
}
static void initialize(void) {
  arb_init(cc);arb_init(pp);arb_init(kap);arb_init(ltwo);arb_init(rone);arb_init(rbnd);arb_init(rcbnd);arb_init(rerr);arb_init(dbnd);arb_init(dcbnd);arb_init(derr);
  arb_const_pi(pp,prec);arb_mul_2exp_si(cc,pp,1);arb_t v,g;arb_init(v);arb_init(g);
  arb_sqrt_ui(v,6503188012738584ULL,prec);arb_div(cc,cc,v,prec);
  arb_mul_2exp_si(kap,pp,2);arb_log(kap,kap,prec);arb_const_euler(g,prec);arb_sub(kap,kap,g,prec);arb_log_ui(ltwo,2,prec);
  arb_set_ui(v,3);arb_div_ui(v,v,10,prec);residual_bound(rbnd,v,0);residual_bound(rerr,v,NF);derivative_bound(dbnd,v,0,0);derivative_bound(derr,v,NF,0);
  arb_set_ui(v,16);residual_bound(g,v,0);arb_add(rerr,rerr,g,prec);derivative_bound(g,v,0,0);arb_add(derr,derr,g,prec);
  arb_one(v);arb_div_ui(v,v,5,prec);residual_bound(rcbnd,v,0);derivative_bound(dcbnd,v,0,1);
  /* These guards certify the chosen real and complex convergence radii. */
  arb_set_si(v,-1);arb_div_ui(v,v,8,prec);arb_exp(v,v,prec);arb_sqrt_ui(g,8,prec);arb_div(v,v,g,prec);arb_set_ui(g,3);arb_div_ui(g,g,10,prec);if(!arb_gt(v,g))fatal("real strip guard");
  arb_set_si(v,-3);arb_div_ui(v,v,8,prec);arb_exp(v,v,prec);arb_sqrt_ui(g,8,prec);arb_div(v,v,g,prec);arb_one(g);arb_mul_2exp_si(g,g,-2);arb_cos(g,g,prec);arb_mul(v,v,g,prec);arb_one(g);arb_div_ui(g,g,5,prec);if(!arb_gt(v,g))fatal("complex strip guard");
  arb_one(v);arb_mul_2exp_si(v,v,-2);arb_cos(v,v,prec);arb_one(g);arb_mul_2exp_si(g,g,-7);arb_sub(v,v,g,prec);arb_set_ui(g,585);arb_div_ui(g,g,640,prec);if(!arb_gt(v,g))fatal("compressed Fourier complex bound");
  for(int n=1;n<=NF;n++) {arb_init(sig+n);arb_init(kn+n);arb_zero(sig+n);arb_zero(kn+n);
    for(int d=1;d<=n;d++)if(n%d==0){arb_add_ui(sig+n,sig+n,d,prec);arb_log_ui(v,d,prec);arb_addmul_ui(kn+n,v,d,prec);}
    arb_mul_2exp_si(kn+n,kn+n,1);arb_div(kn+n,kn+n,sig+n,prec);arb_log_ui(v,n,prec);arb_sub(kn+n,kn+n,v,prec);arb_add(kn+n,kn+n,kap,prec);arb_div_ui(sig+n,sig+n,n,prec);}
  arb_clear(v);arb_clear(g);
}
/* A panel uses one fixed analytic branch and one fixed omission mask. */
static void select_residual(const arb_t umid,const arb_t uhalf) {
  arb_t t,v,w,low;arb_init(t);arb_init(v);arb_init(w);arb_init(low);arb_exp(t,umid,prec);
  arb_sqrt_ui(w,6503188012738584ULL,prec);arb_div_ui(w,w,4547,prec);
  arb_neg(low,uhalf);arb_exp(low,low,prec);
  arb_t one,test;arb_init(one);arb_init(test);arb_one(one);
  for(int j=0;j<8;j++) {arb_mul_ui(v,t,odd[j],prec);arb_div(v,v,w,prec);arb_sqr(test,v,prec);arb_mul_ui(test,test,8,prec);inv8[j]=arb_lt(test,one);
    if(inv8[j]){arb_mul_ui(v,v,8,prec);arb_inv(v,v,prec);}arb_mul(v,v,low,prec);
    for(int h=0;h<4;h++){arb_mul_ui(test,v,scale4[h],prec);arb_set_ui(one,16);keep[j][h]=!arb_gt(test,one);}arb_one(one);}
  arb_clear(one);arb_clear(test);arb_clear(t);arb_clear(v);arb_clear(w);arb_clear(low);
}
static void residual(arb_t out,arb_t du,const arb_t t,int wantdu) {
  arb_t v,w,x,e,q,a,b,tmp,one;arb_init(v);arb_init(w);arb_init(x);arb_init(e);arb_init(q);arb_init(a);arb_init(b);arb_init(tmp);arb_init(one);arb_one(one);
  arb_sqrt_ui(w,6503188012738584ULL,prec);arb_div_ui(w,w,4547,prec);arb_zero(out);arb_zero(du);
  for(int j=0;j<8;j++) {arb_mul_ui(v,t,odd[j],prec);arb_div(v,v,w,prec);if(inv8[j]){arb_mul_ui(v,v,8,prec);arb_inv(v,v,prec);}
    for(int h=0;h<4;h++)if(keep[j][h]) {int outer=(h==0||h==3);arb_set_si(b,outer?-1:3);if(!outer)arb_mul_2exp_si(b,b,-1);
      for(int n=1;n<=NF;n++) {arb_mul_ui(x,v,2*scale4[h]*n,prec);arb_mul(x,x,pp,prec);arb_neg(e,x);arb_exp(e,e,prec);
        arb_mul_2exp_si(tmp,x,1);arb_hypgeom_expint(q,one,tmp,prec);arb_exp(tmp,tmp,prec);arb_mul(q,q,tmp,prec); /* q=exp(2x) E1(2x) */
        arb_mul(a,b,kn+n,prec);arb_mul_si(tmp,ltwo,outer?3:-3,prec);arb_add(a,a,tmp,prec);
        arb_mul(tmp,b,q,prec);arb_add(tmp,tmp,a,prec);arb_mul(tmp,tmp,e,prec);arb_addmul(out,tmp,sig+n,prec);
        if(wantdu){arb_sub(tmp,q,one,prec); /* overwritten with x*q-1 */ arb_mul(tmp,x,q,prec);arb_sub_ui(tmp,tmp,1,prec);arb_mul(tmp,tmp,b,prec);arb_submul(tmp,x,a,prec);arb_mul(tmp,tmp,e,prec);if(inv8[j])arb_neg(tmp,tmp);arb_addmul(du,tmp,sig+n,prec);}
      }
    }
  }
  arb_clear(v);arb_clear(w);arb_clear(x);arb_clear(e);arb_clear(q);arb_clear(a);arb_clear(b);arb_clear(tmp);arb_clear(one);
}
static void fsums(arb_t f,arb_t phi,const arb_t t,long nbin,int cross) {
  arb_t z,k,e,step,p,q,prev,delta;arb_init(z);arb_init(k);arb_init(e);arb_init(step);arb_init(p);arb_init(q);arb_init(prev);arb_init(delta);arb_mul(k,cc,t,prec);
  arb_mul_ui(step,k,MAXBIN,prec);arb_neg(step,step);arb_exp(step,step,prec);arb_zero(f);arb_zero(phi);
  for(long j=0;j<nbin;j++){Bin *b=bins+j;arb_mul(z,k,&b->center,prec);
    if(j&&b->len==MAXBIN&&bins[j-1].len==MAXBIN)arb_mul(e,e,step,prec);else{arb_neg(e,z);arb_exp(e,e,prec);}
    arb_set(p,b->cf+7);if(cross)arb_set(q,b->cq+7);
    for(int d=6;d>=0;d--){arb_mul(p,p,z,prec);arb_add(p,p,b->cf+d,prec);if(cross){arb_mul(q,q,z,prec);arb_add(q,q,b->cq+d,prec);}}
    arb_addmul(f,e,p,prec);if(cross)arb_addmul(phi,e,q,prec);
  }
  arb_clear(z);arb_clear(k);arb_clear(e);arb_clear(step);arb_clear(p);arb_clear(q);arb_clear(prev);arb_clear(delta);
}
/* Pointwise tail sum_{n>T} d(n)sqrt(n) exp(-k*n), decreasing in k. */
static void ftail(arb_t out,const arb_t k) {
  arb_t v,a,b,c,s,lg;arb_init(v);arb_init(a);arb_init(b);arb_init(c);arb_init(s);arb_init(lg);
  arb_sqrt_ui(s,NT,prec);arb_log_ui(lg,NT,prec);arb_mul_ui(out,s,2*NT,prec);
  arb_add_ui(a,lg,2,prec);arb_mul(a,a,s,prec);arb_div(a,a,k,prec);arb_add(out,out,a,prec);
  arb_add_ui(a,lg,4,prec);arb_sqr(b,k,prec);arb_mul(b,b,s,prec);arb_mul_2exp_si(b,b,1);arb_div(a,a,b,prec);arb_add(out,out,a,prec);
  arb_pow_ui(b,k,3,prec);arb_mul(b,b,s,prec);arb_mul_ui(b,b,NT,prec);arb_inv(b,b,prec);arb_add(out,out,b,prec);
  arb_mul_ui(v,k,NT,prec);arb_neg(v,v);arb_exp(v,v,prec);arb_mul(out,out,v,prec);
  arb_clear(v);arb_clear(a);arb_clear(b);arb_clear(c);arb_clear(s);arb_clear(lg);
}
static void data_tail(arb_t out,arb_t out2) {
  arb_t a,b,t,u,h,r,dr,bd,v,k,er;arb_init(a);arb_init(b);arb_init(t);arb_init(u);arb_init(h);arb_init(r);arb_init(dr);arb_init(bd);arb_init(v);arb_init(k);arb_init(er);arb_zero(out);
  arb_zero(out2);
  /* Rational cells cover t in [1,4], width 1/TAIL_DEN. */
  for(int j=0;j<3*TAIL_DEN;j++) {arb_set_ui(a,TAIL_DEN+j);arb_div_ui(a,a,TAIL_DEN,prec);arb_set_ui(b,TAIL_DEN+j+1);arb_div_ui(b,b,TAIL_DEN,prec);arb_union(t,a,b,prec);
    arb_log(u,t,prec);arb_get_mid_arb(h,u);arb_t half;arb_init(half);arb_get_rad_arb(half,u);select_residual(h,half);arb_clear(half);
    residual(r,dr,t,1);arb_sub(r,r,rone,prec);arb_get_abs_ubound_arf(arb_midref(bd),r,prec);mag_zero(arb_radref(bd));arb_mul_2exp_si(er,rerr,1);arb_add(bd,bd,er,prec);
    arb_mul(k,cc,a,prec);ftail(v,k);arb_mul(v,v,bd,prec);arb_mul(v,v,cc,prec);arb_div_ui(v,v,TAIL_DEN,prec);arb_add(out,out,v,prec);
    arb_get_abs_ubound_arf(arb_midref(bd),dr,prec);mag_zero(arb_radref(bd));arb_add(bd,bd,derr,prec);tail_ms(v,k,NT);arb_mul(v,v,bd,prec);arb_div(v,v,a,prec);arb_div_ui(v,v,TAIL_DEN,prec);arb_add(out2,out2,v,prec);
  }
  arb_mul_ui(k,cc,4,prec);tail_ms(v,k,NT);arb_mul(v,v,rbnd,prec);arb_mul_2exp_si(v,v,1);arb_add(out,out,v,prec);
  tail_ms(v,k,NT);arb_mul(v,v,dbnd,prec);arb_mul_ui(er,k,NT,prec);arb_div(v,v,er,prec);arb_add(out2,out2,v,prec);
  arb_clear(a);arb_clear(b);arb_clear(t);arb_clear(u);arb_clear(h);arb_clear(r);arb_clear(dr);arb_clear(bd);arb_clear(v);arb_clear(k);arb_clear(er);
}
static void evaluate(const char *path,int cross) {
  initialize();readbins(path);arb_t zero,t,r,rd,u,mid,half,f,phi,v,w,tot,tot2,cuterr,err,tail,comp,quad,k,Rmass;
  arb_init(zero);arb_init(t);arb_init(r);arb_init(rd);arb_init(u);arb_init(mid);arb_init(half);arb_init(f);arb_init(phi);arb_init(v);arb_init(w);arb_init(tot);arb_init(tot2);arb_init(cuterr);arb_init(err);arb_init(tail);arb_init(comp);arb_init(quad);arb_init(k);arb_init(Rmass);arb_zero(zero);arb_one(t);select_residual(zero,zero);residual(rone,rd,t,0);
  show("R_ONE_FINITE",rone);show("R_GLOBAL_BOUND",rbnd);show("R_COMPLEX_BOUND",rcbnd);show("R_FOURIER_OMISSION",rerr);
  printf("PRECISION %ld\nTAIL_GRID_DEN %d\nGAUSS_ORDER %d\n",prec,TAIL_DEN,NG);
  arb_t tail2,err2,comp2,cut2,quad2,rem2,gam,k2;
  arb_init(tail2);arb_init(err2);arb_init(comp2);arb_init(cut2);arb_init(quad2);arb_init(rem2);arb_init(gam);arb_init(k2);arb_set_ui(gam,64);arb_div_ui(gam,gam,65,prec);
  show("R_DERIVATIVE_BOUND",dbnd);show("R_DERIVATIVE_COMPLEX_BOUND",dcbnd);show("R_DERIVATIVE_OMISSION",derr);
  arb_sqrt_ui(v,NT,prec);arb_log_ui(w,NT,prec);arb_add_ui(w,w,1,prec);arb_mul(Rmass,v,w,prec);arb_mul_2exp_si(Rmass,Rmass,1); /* sum |a_n|/n <= Rmass */
  arb_mul(comp,Rmass,rbnd,prec);arb_mul_2exp_si(comp,comp,2-56);arb_mul_ui(comp,comp,65,prec);arb_div_ui(comp,comp,64,prec); /* twice compression, eta^8=2^-56 */
  arb_mul(err,rerr,Rmass,prec);arb_mul_2exp_si(err,err,1);show("COMPRESSION_ERROR",comp);show("RESIDUAL_SERIES_ERROR",err);
  arb_mul_ui(comp2,dbnd,81,prec);arb_div(comp2,comp2,cc,prec);arb_mul_2exp_si(comp2,comp2,-56);arb_sqr(v,gam,prec);arb_div(comp2,comp2,v,prec);
  arb_mul(k2,cc,gam,prec);arb_one(v);arb_hypgeom_expint(err2,v,k2,prec);arb_mul(err2,err2,Rmass,prec);arb_mul(err2,err2,derr,prec);arb_div(err2,err2,gam,prec);
  show("IBP_COMPRESSION_ERROR",comp2);show("IBP_RESIDUAL_SERIES_ERROR",err2);
  data_tail(tail,tail2);show("COEFFICIENT_TAIL",tail);show("IBP_COEFFICIENT_TAIL",tail2);
  if(reuse128) {
    /* Exact Arb dumps from the completed, retained interval128.log.
       Replay without reuse regenerates these finite quadratures. */
    if(prec!=128)fatal("reuse precision");
    if(arb_load_str(tot,"af428896d5b1993d6c1338bb9f237737 -8a 10883ee3 -6c")||
       arb_load_str(tot2,"15e85112dab63330fe29c0a0cf9387f3 -87 892c74b -6a"))fatal("reuse dump");
    printf("REUSED_FINITE_QUADRATURE interval128.log\n");
  }
  arb_struct nodes[NG],weights[NG];for(int j=0;j<NG;j++){arb_init(nodes+j);arb_init(weights+j);arb_hypgeom_legendre_p_ui_root(nodes+j,weights+j,NG,j,prec);}
  arb_zero(v);for(int j=0;j<NG;j++)arb_add(v,v,weights+j,prec);arb_set_ui(w,2);if(!arb_contains(v,w))fatal("Gauss weight sum");
  for(int i=0;i<PANELS;i++) {
    arb_set_ui(mid,2*i+1);arb_div_ui(mid,mid,8,prec);arb_one(half);arb_div_ui(half,half,8,prec);select_residual(mid,half);
    arb_set_ui(u,i);arb_div_ui(u,u,4,prec);arb_exp(t,u,prec);arb_mul(k,cc,t,prec);long count=nb;
    for(long j=0;j<nb;j++){arb_mul_ui(v,k,bins[j].lo,prec);arb_set_ui(w,40);if(arb_gt(v,w)){count=j;break;}}
    if(count<nb){u64 K=bins[count].lo-1;if(K)tail_ms(v,k,K);else{arb_neg(v,k);arb_exp(v,v,prec);arb_one(w);arb_sub(w,w,v,prec);arb_div(v,v,w,prec);arb_mul_2exp_si(v,v,1);}arb_mul(v,v,rbnd,prec);arb_mul_2exp_si(v,v,1);arb_add(cuterr,cuterr,v,prec);
      arb_mul(k2,k,gam,prec);if(K)tail_ms(v,k2,K);else{arb_neg(v,k2);arb_exp(v,v,prec);arb_one(w);arb_sub(w,w,v,prec);arb_div(v,v,w,prec);arb_mul_2exp_si(v,v,1);}arb_mul(v,v,dbnd,prec);arb_div(v,v,gam,prec);arb_mul_2exp_si(v,v,-2);arb_add(cut2,cut2,v,prec);}
    for(int j=0;j<(reuse128?0:NG);j++) {
      arb_mul(u,nodes+j,half,prec);arb_add(u,u,mid,prec);arb_exp(t,u,prec);residual(r,rd,t,cross);arb_sub(r,r,rone,prec);fsums(f,phi,t,count,cross);
      arb_mul(v,f,r,prec);arb_mul(v,v,t,prec);arb_mul(v,v,cc,prec);arb_mul(v,v,weights+j,prec);arb_mul(v,v,half,prec);arb_add(tot,tot,v,prec);
      if(cross){arb_mul(v,phi,rd,prec);arb_mul(v,v,weights+j,prec);arb_mul(v,v,half,prec);arb_add(tot2,tot2,v,prec);}
    }
    if(i%8==0){printf("PANEL %d BINS %ld\n",i,count);show("PARTIAL",tot);}
  }
  /* Cauchy plus exact Gauss-Legendre error: discs radius 1/4,
     length 1/4, M=2*Bc*(10/9)*Rmass. */
  arb_mul(v,Rmass,rcbnd,prec);arb_mul_ui(v,v,20,prec);arb_div_ui(v,v,9,prec);
  arb_fac_ui(quad,NG,prec);arb_pow_ui(quad,quad,4,prec);arb_fac_ui(w,2*NG,prec);arb_sqr(w,w,prec);arb_mul_ui(w,w,2*NG+1,prec);arb_div(quad,quad,w,prec);arb_mul(quad,quad,v,prec);arb_mul_ui(quad,quad,24,prec);
  arb_div(quad2,quad,rcbnd,prec);arb_mul(quad2,quad2,dcbnd,prec);arb_mul_2exp_si(quad2,quad2,-1);
  /* Integral beyond e^24: |R-R1| <=2Br, exact f tail via n<=T
     plus universal d(n)sqrt(n)<=2n. Sum_{n>=1} 2 exp(-c U n). */
  arb_set_ui(u,24);arb_exp(t,u,prec);arb_mul(k,cc,t,prec);arb_neg(v,k);arb_exp(v,v,prec);arb_one(w);arb_sub(w,w,v,prec);arb_div(v,v,w,prec);arb_mul(v,v,rbnd,prec);arb_mul_ui(v,v,4,prec);
  arb_div(rem2,v,rbnd,prec);arb_mul_2exp_si(rem2,rem2,-1);arb_mul(rem2,rem2,dbnd,prec);arb_div(rem2,rem2,k,prec);
  show("FINITE_INTEGRAL",tot);if(cross)show("IBP_FINITE_INTEGRAL",tot2);show("ADAPTIVE_COEFFICIENT_CUTOFF",cuterr);show("GAUSS_QUADRATURE_ERROR",quad);show("INFINITE_INTEGRAL_TAIL",v);
  arb_get_rad_arb(w,tot);show("BALL_ARITHMETIC_RADIUS",w);arb_get_rad_arb(w,tot2);show("IBP_BALL_ARITHMETIC_RADIUS",w);show("IBP_ADAPTIVE_COEFFICIENT_CUTOFF",cut2);show("IBP_GAUSS_QUADRATURE_ERROR",quad2);show("IBP_INFINITE_INTEGRAL_TAIL",rem2);
  arb_add(err,err,comp,prec);arb_add(err,err,tail,prec);arb_add(err,err,cuterr,prec);arb_add(err,err,quad,prec);arb_add(err,err,v,prec);show("TOTAL_ANALYTIC_ERROR",err);
  arb_add_error(tot,err);show("DELTA_INTERVAL",tot);printf("ZERO_EXCLUDED %d\n",!arb_contains_zero(tot));fflush(stdout);
  arb_add(err2,err2,comp2,prec);arb_add(err2,err2,tail2,prec);arb_add(err2,err2,cut2,prec);arb_add(err2,err2,quad2,prec);arb_add(err2,err2,rem2,prec);show("IBP_TOTAL_ANALYTIC_ERROR",err2);arb_add_error(tot2,err2);show("IBP_DELTA_INTERVAL",tot2);printf("INDEPENDENT_REPRESENTATIONS_OVERLAP %d\n",arb_overlaps(tot,tot2));
  if(!arb_overlaps(tot,tot2))fatal("representations disagree");
}
int main(int argc,char **argv) {
  if(argc<3)fatal("usage: delta prep moments | delta eval moments [precision] [cross]");
  if(!strcmp(argv[1],"prep")){prepare(argv[2]);return 0;}
  prec=argc>3?atol(argv[3]):128;if(prec!=128&&prec!=256)fatal("precision budget");
  reuse128=argc>5?atoi(argv[5]):0;evaluate(argv[2],argc>4?atoi(argv[4]):0);return 0;
}
