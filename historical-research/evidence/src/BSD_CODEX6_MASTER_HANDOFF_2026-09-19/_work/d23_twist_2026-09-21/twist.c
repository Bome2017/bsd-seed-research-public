/* Isolated D=-23 first-derivative adapter. The included retained source is
 * byte-identical to the sealed C11 engine; its main is never called here.
 * See DESIGN.md for model remainder, traversal, and certificate boundaries. */
#define main retained_main
#include "retained_arbcore.c"
#undef main
#include <math.h>
#include <time.h>

#define TD 8
#define TH 8
#define TK (1 << TH)
#define EMIN (-32)
#define EMAX 8
#define NT ((EMAX - EMIN + 1) * TK)
static arb_ptr TC;
static mag_ptr TR;
static int chi[23];
static arb_t ONE;
static __thread arb_t EX, ET, EV, EW;
static long USTART, UEND;

/* E1(x+s*u). Same power-series recurrence as retained g2_node,
 * stopped before its extra integration to G2. All nodes/scales are dyadic. */
static void e1_node(arb_ptr out, const arb_t x, int scale_exp) {
  arb_t e, iv, s, z, acc; arb_init(e); arb_init(iv); arb_init(s);
  arb_init(z); arb_init(acc); arb_one(s); arb_mul_2exp_si(s,s,scale_exp);
  arb_ptr ex=_arb_vec_init(TD+1), inv=_arb_vec_init(TD+1);
  arb_neg(z,x); arb_exp(ex,z,NPREC); arb_inv(inv,x,NPREC);
  for (int k=1;k<=TD;k++) {
    arb_mul(ex+k,ex+k-1,s,NPREC); arb_div_si(ex+k,ex+k,-k,NPREC);
    arb_mul(inv+k,inv+k-1,s,NPREC); arb_div(inv+k,inv+k,x,NPREC);
    arb_neg(inv+k,inv+k);
  }
  arb_hypgeom_expint(out,ONE,x,NPREC);
  for (int k=0;k<=TD;k++) {
    arb_zero(acc);
    for(int i=0;i<=k;i++) arb_addmul(acc,ex+i,inv+k-i,NPREC);
    arb_mul(acc,acc,s,NPREC); arb_div_si(out+k+1,acc,-(k+1),NPREC);
  }
  _arb_vec_clear(ex,TD+1);_arb_vec_clear(inv,TD+1);
  arb_clear(e);arb_clear(iv);arb_clear(s);arb_clear(z);arb_clear(acc);
}
static void init_twist(void) {
  arb_init(ONE);arb_one(ONE);arb_init(CL2);
  arb_t x,y;arb_init(x);arb_init(y);arb_const_pi(x,NPREC);
  arb_sqrt_ui(y,6503188012738584ULL,NPREC);arb_mul_ui(y,y,23,NPREC);
  arb_div(CL2,x,y,NPREC);arb_mul_2exp_si(CL2,CL2,1);
  for(int r=1;r<23;r++)chi[r]=-1;
  for(int r=1;r<23;r++)chi[(r*r)%23]=1;
  TC=_arb_vec_init(NT*(TD+2));TR=_mag_vec_init(NT);
  arb_ptr left=_arb_vec_init(TD+2);
  for(int e=EMIN;e<=EMAX;e++)for(int j=0;j<TK;j++){
    int idx=(e-EMIN)*TK+j;
    arb_set_ui(x,TK+j);arb_mul_2exp_si(x,x,e-TH);
    e1_node(TC+idx*(TD+2),x,e);
    arb_set_ui(y,TK+j-1);arb_mul_2exp_si(y,y,e-TH);
    e1_node(left,y,e);
    arb_get_mag(TR+idx,left+TD+1);
    mag_mul_2exp_si(TR+idx,TR+idx,(1-TH)*(TD+1));
  }
  _arb_vec_clear(left,TD+2);arb_clear(x);arb_clear(y);
}
static void e1_eval(arb_t out,const arb_t x,arb_t t) {
  double xd=arf_get_d(arb_midref(x),ARF_RND_NEAR);int ee;
  double frac=frexp(xd,&ee);int e=ee-1,j=(int)((2*frac-1)*TK);
  if(e<EMIN||e>EMAX||j<0||j>=TK)fatal("E1 node outside covered range");
  int idx=(e-EMIN)*TK+j;
  arb_mul_2exp_si(t,x,TH-e);arb_sub_ui(t,t,TK+j,PREC);
  /* t here is TK times the normalized Taylor step. */
  arf_t lb,ub;arf_init(lb);arf_init(ub);
  arb_get_lbound_arf(lb,t,PREC);arb_get_ubound_arf(ub,t,PREC);
  if(arf_cmp_si(lb,-1)<0||arf_cmp_si(ub,2)>0)fatal("E1 Taylor range guard");
  arf_clear(lb);arf_clear(ub);arb_mul_2exp_si(t,t,-TH);
  arb_srcptr a=TC+idx*(TD+2);arb_set_round(out,a+TD,PREC);
  for(int k=TD-1;k>=0;k--){arb_mul(out,out,t,PREC);arb_add(out,out,a+k,PREC);}
  arb_add_error_mag(out,TR+idx);
}
static void tail_twist(arb_t out,u64 cutoff){
  /* B_D(T)=2 tail_MS(c,T)/(cT); inherited elementary tail_MS. */
  arb_t z;arb_init(z);tail_ms(out,CL2,cutoff);
  arb_mul_ui(z,CL2,cutoff,NPREC);arb_div(out,out,z,NPREC);
  arb_mul_2exp_si(out,out,1);arb_clear(z);
}
static void add_term(arb_t sum,u64 n,i64 a) {
  int ch=chi[n%23];if(!ch||!a)return;
  arb_mul_ui(EX,CL2,n,PREC);e1_eval(EV,EX,ET);
  arb_mul_si(EV,EV,a*ch,PREC);arb_div_ui(EV,EV,n,PREC);
  arb_add(sum,sum,EV,PREC);
}
static void twist_block(long b,u64 *rem,i64 *an,long u) {
  u64 lo=(u64)b*BLK+1,hi=lo+BLK;if(hi>T+1)hi=T+1;
  gen_block(lo,hi,rem,an,0);CC_SHA256_CTX hc;CC_SHA256_Init(&hc);
  u64 nsm=0,nnz=0;
  arb_ptr sum=_arb_vec_init(1);
  for(u64 n=lo;n<hi;n++){
    i64 v=rem[n-lo]==1?an[n-lo]:0;CC_SHA256_Update(&hc,&v,8);
    if(rem[n-lo]!=1)continue;nsm++;
    if(v&&chi[n%23]){nnz++;add_term(sum,n,v);}
  }
  unsigned char dg[32];char hx[65],tmp[2100],fn[2048];
  CC_SHA256_Final(dg,&hc);hexs(dg,hx);FILE*f=unit_open(u,tmp,fn);
  fprintf(f,"BLK %ld lo %llu hi %llu leaf %s nnz %llu smooth %llu\n",b,lo,hi,hx,nnz,nsm);
  put_sums(f,sum,1);unit_close(f,tmp,fn);_arb_vec_clear(sum,1);
}
static void twist_lseg(long s,unsigned char *comp,int32_t *buf,long u) {
  u64 lo,hi;seg_bounds(s,&lo,&hi);unsigned char dg[32];char hx[65];
  read_apseg(s,comp,buf,dg);hexs(dg,hx);
  arb_ptr sum=_arb_vec_init(1);u64 i=0,nq=0,pairs=0,nnz=0;
  for(u64 q=lo;q<hi;q++){
    if(comp[q-lo])continue;i64 aq=buf[i++];if(q<=RT)continue;
    u64 mmax=T/q;nq++;pairs+=mmax;if(!aq||!chi[q%23])continue;
    for(u64 m=1;m<=mmax;m++){
      if(!chi[m%23]||arb_is_zero(AMT+m))continue;
      u64 n=q*m;arb_mul_ui(EX,CL2,n,PREC);e1_eval(EV,EX,ET);
      arb_mul_si(EV,EV,aq*chi[n%23],PREC);arb_div_ui(EV,EV,q,PREC);
      arb_addmul(sum,EV,AMT+m,PREC);nnz++;
    }
  }
  char tmp[2100],fn[2048];FILE*f=unit_open(u,tmp,fn);
  fprintf(f,"LSEG %ld lo %llu hi %llu apsha %s bigprimes %llu pairs %llu nnz %llu\n",s,lo,hi,hx,nq,pairs,nnz);
  put_sums(f,sum,1);unit_close(f,tmp,fn);_arb_vec_clear(sum,1);
}
static void *twist_worker(void *arg){
  TID=(int)(long)arg;u64*rem=malloc(BLK*8);i64*an=malloc(BLK*8);
  unsigned char*comp=malloc(SEGQ);int32_t*buf=malloc(SEGQ*4);
  arb_init(EX);arb_init(ET);arb_init(EV);arb_init(EW);
  for(;;){
    long u=__atomic_fetch_add(&NEXTU,1,__ATOMIC_SEQ_CST);
    if(u>=UEND)break;if(unit_done(u))continue;
    if(u<NSEG)twist_lseg(u,comp,buf,u);else twist_block(u-NSEG,rem,an,u);
  }
  arb_clear(EX);arb_clear(ET);arb_clear(EV);arb_clear(EW);
  free(rem);free(an);free(comp);free(buf);flint_cleanup();return NULL;
}
static int kernel_test(void){
  arb_t x,a,b,t;arb_init(x);arb_init(a);arb_init(b);arb_init(t);
  long checked=0,bad=0;double maxrad=0;
  for(int e=-31;e<=7;e++)for(int j=0;j<TK;j+=7)for(int k=0;k<=2;k++){
    arb_set_ui(x,4*(TK+j)+k);arb_mul_2exp_si(x,x,e-TH-2);
    e1_eval(a,x,t);arb_hypgeom_expint(b,ONE,x,NPREC);
    checked++;bad+=!arb_overlaps(a,b);
    double rr=mag_get_d(arb_radref(a));if(rr>maxrad)maxrad=rr;
  }
  /* Actual cn values, including small x and later candidate cutoffs. */
  u64 bases[]={1,1000,1000000,16777000,100000000,295000000,1000000000,3450000000ULL,7000000000ULL,39000000000ULL};
  for(int q=0;q<10;q++)for(int k=0;k<128;k++){
    arb_mul_ui(x,CL2,bases[q]+k,PREC);e1_eval(a,x,t);
    arb_hypgeom_expint(b,ONE,x,NPREC);checked++;bad+=!arb_overlaps(a,b);
  }
  printf("E1_TEST checked %ld nonoverlap %ld max_radius %.12e\n",checked,bad,maxrad);
  for(int q=0;q<10;q++){
    arb_mul_ui(x,CL2,bases[q],PREC);e1_eval(a,x,t);
    printf("E1_SAMPLE n %llu value %s\n",bases[q],arb_get_str(a,25,0));
  }
  arb_clear(x);arb_clear(a);arb_clear(b);arb_clear(t);return bad?4:0;
}
static int chi_pow(u64 n){int r=(int)(n%23);if(!r)return 0;int z=1;for(int k=0;k<11;k++)z=z*r%23;return z==1?1:-1;}
/* Independent trial-factor coefficient lookup for short validation blocks.
 * The prime table is reused, but partitioning and kernel are not. */
static i64 test_ap(u64 q,unsigned char*comp,int32_t*buf,long*cached){
  if(q<=ATOP)return A[q];long s=q/SEGQ;
  if(s!=*cached){unsigned char d[32];read_apseg(s,comp,buf,d);*cached=s;}
  u64 lo,hi;seg_bounds(s,&lo,&hi);u64 k=0;
  for(u64 p=lo;p<q;p++)k+=!comp[p-lo];
  if(comp[q-lo])fatal("test factor not prime");return buf[k];
}
static i64 test_coeff(u64 n,unsigned char*comp,int32_t*buf,long*cached){
  i64 out=1;u64 rem=n;
  for(long i=0;i<NSP&&SP[i]*SP[i]<=rem;i++){
    u64 p=SP[i];if(rem%p)continue;i64 ap=A[p],prev=1,cur=ap;int e=0;
    while(rem%p==0){rem/=p;e++;if(e>1){i64 next=is_bad(p)?cur*ap:ap*cur-(i64)p*prev;prev=cur;cur=next;}}
    out*=cur;
  }
  if(rem>1)out*=test_ap(rem,comp,buf,cached);return out;
}
static int block_test(void){
  u64 starts[]={1,1000000,100000000,295000000,1000000000,3450000000ULL,6999999000ULL};
  const u64 width=64;long bad=0,checked=0;
  u64*rem=malloc(width*8);i64*an=malloc(width*8);
  unsigned char*comp=malloc(SEGQ);int32_t*buf=malloc(SEGQ*4);long cached=-1;
  arb_t direct,model,v,x;arb_init(direct);arb_init(model);arb_init(v);arb_init(x);
  arb_init(EX);arb_init(ET);arb_init(EV);arb_init(EW);
  for(int q=0;q<7;q++){
    u64 lo=starts[q],hi=lo+width;if(hi>T+1)continue;
    gen_block(lo,hi,rem,an,0);arb_zero(direct);arb_zero(model);
    for(u64 n=lo;n<hi;n++){
      i64 a=an[n-lo];if(rem[n-lo]>1)a*=test_ap(rem[n-lo],comp,buf,&cached);
      i64 ref=test_coeff(n,comp,buf,&cached);if(a!=ref)bad++;
      int c=chi_pow(n);if(c!=chi[n%23])bad++;
      add_term(model,n,a);
      if(c&&ref){arb_mul_ui(x,CL2,n,NPREC);arb_hypgeom_expint(v,ONE,x,NPREC);
        arb_mul_si(v,v,ref*c,NPREC);arb_div_ui(v,v,n,NPREC);arb_add(direct,direct,v,NPREC);}
      checked++;
    }
    int ok=arb_overlaps(model,direct);bad+=!ok;
    printf("BLOCK_TEST lo %llu hi %llu overlaps %d model %s direct %s\n",lo,hi,ok,arb_get_str(model,24,0),arb_get_str(direct,24,0));
  }
  printf("BLOCK_TEST_TOTAL terms %ld failures %ld\n",checked,bad);return bad?4:0;
}
static void setup_stream(u64 cutoff,const char*apdir){
  T=cutoff;SEGQ=16777216;MODE=2;MM=1;APDIR=apdir;
  if((T+1)%SEGQ||T>39141244927ULL)fatal("cutoff must be complete retained segments");
  a1=0;a2=-22735;a3=0;a4=106272484;a6=0;
  b2=4*(i128)a2;b4=2*(i128)a4;b6=0;
  DISC=-(b2*b2*(-(i128)a4*a4))-8*b4*b4*b4;
  RT=1;while((RT+1)*(RT+1)<=T)RT++;
  small_primes();NSEG=T/SEGQ+1;APSH=calloc(NSEG,32);load_table(RT);
  u64*rem=malloc(8*(RT+1));i64*am=malloc(8*(RT+1));gen_block(1,RT+1,rem,am,0);
  AMT=_arb_vec_init(RT+1);
  for(u64 m=1;m<=RT;m++){
    if(rem[m-1]!=1)fatal("small coefficient not smooth");
    arb_set_si(AMT+m,am[m-1]);arb_div_ui(AMT+m,AMT+m,m,NPREC);
  }
  free(rem);free(am);NBLK=(T+BLK-1)/BLK;NUNIT=NSEG+NBLK;
}
static void combine(void){
  arb_t total,v,tail,result;arb_init(total);arb_init(v);arb_init(tail);arb_init(result);
  char hdr[65536];unsigned char(*leaves)[32]=malloc(32*NBLK);
  u64 smooth=0,pairs=0;
  for(long u=0;u<NUNIT;u++){
    read_unit(u,hdr,v,1);arb_add(total,total,v,PREC);
    if(u<NSEG){if(hdr_u64(hdr,"LSEG ")!=(u64)u)fatal("bad unit order");
      hdr_hex(hdr,"apsha ",APSH[u]);pairs+=hdr_u64(hdr,"pairs ");}
    else {long b=u-NSEG;if(hdr_u64(hdr,"BLK ")!=(u64)b)fatal("bad block order");
      hdr_hex(hdr,"leaf ",leaves[b]);smooth+=hdr_u64(hdr,"smooth ");}
  }
  if(smooth+pairs!=T)fatal("count identity failed");
  printf("COUNT smooth %llu pairs %llu sum %llu T %llu identity 1\n",smooth,pairs,smooth+pairs,T);
  unsigned char dg[32];char hx[65];CC_SHA256(APSH,32*NSEG,dg);hexs(dg,hx);printf("AP_SEGROOT_SHA256 %s segments %ld\n",hx,NSEG);
  CC_SHA256(leaves,32*NBLK,dg);hexs(dg,hx);printf("SMOOTH_MERKLE_SHA256 %s blocks %ld\n",hx,NBLK);
  arb_mul_2exp_si(total,total,1);tail_twist(tail,T);arb_set(result,total);
  arf_t up;arf_init(up);arb_get_ubound_arf(up,tail,NPREC);arb_add_error_arf(result,up);
  printf("C %s\nPARTIAL_2S %s\nPARTIAL_DUMP %s\nTAIL_BOUND %s\nTAIL_DUMP %s\nLPRIME_BALL %s\nLPRIME_DUMP %s\n",
    arb_get_str(CL2,30,0),arb_get_str(total,30,0),arb_dump_str(total),arb_get_str(tail,25,0),arb_dump_str(tail),arb_get_str(result,30,0),arb_dump_str(result));
  print_dec_bounds("LPRIME_INTERVAL",result,1000000);
  printf("ZERO_EXCLUDED %d\nPOSITIVE %d\n",!arb_contains_zero(result),arb_is_positive(result));
}
int main(int argc,char**argv){
  if(fegetround()!=FE_TONEAREST)fatal("rounding mode");
  if(argc<2)fatal("kernel-test | block-test APDIR | run T APDIR W OUT [START END] | combine T APDIR W OUT");
  init_twist();
  if(!strcmp(argv[1],"kernel-test"))return kernel_test();
  if(!strcmp(argv[1],"block-test")){
    if(argc!=3)fatal("block-test APDIR");
    setup_stream(418ULL*16777216-1,argv[2]);return block_test();
  }
  if(argc<6)fatal("run/combine T APDIR W OUT");
  setup_stream(strtoull(argv[2],0,10),argv[3]);W=atoi(argv[4]);OUT=argv[5];
  if(W<1||W>12)fatal("workers must be 1..12");
  mkdir(OUT,0755);
  /* Range arguments are operational, not certificate parameters. */
  char *locked[]={argv[0],"twist-D23-v1",argv[2],argv[3],argv[4],argv[5]};
  params_lock(6,locked,4);
  if(!strcmp(argv[1],"combine")){combine();return 0;}
  if(strcmp(argv[1],"run"))fatal("unknown command");
  USTART=argc>6?atol(argv[6]):0;UEND=argc>7?atol(argv[7]):NUNIT;
  if(USTART<0||UEND> NUNIT||USTART>UEND)fatal("bad unit range");
  NEXTU=USTART;pthread_t th[12];
  for(long i=0;i<W;i++)pthread_create(th+i,0,twist_worker,(void*)i);
  for(long i=0;i<W;i++)pthread_join(th[i],0);
  printf("WORK_UNITS_DONE %ld %ld TOTAL %ld\n",USTART,UEND,NUNIT);
  if(USTART==0&&UEND==NUNIT)combine();return 0;
}
