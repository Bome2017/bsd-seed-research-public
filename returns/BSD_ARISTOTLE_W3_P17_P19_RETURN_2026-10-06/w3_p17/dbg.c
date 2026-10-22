#include "ap.h"
int main(int c,char**v){ bsgs_ws W; ws_init(&W); u64 p=strtoull(v[1],0,10); int ok; i64 a=ap_bsgs(p,&W,&ok); printf("ap=%ld ok=%d\n",a,ok);
 if(p<2000000000ULL){ printf("naive=%ld\n",ap_naive(p)); } }
