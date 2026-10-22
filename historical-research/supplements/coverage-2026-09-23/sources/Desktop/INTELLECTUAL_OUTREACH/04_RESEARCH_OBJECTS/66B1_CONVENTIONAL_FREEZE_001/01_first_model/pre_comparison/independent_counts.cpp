// Independent exact point-count reconstruction, written after prediction freeze.
// No code is imported from the packet. Compile: g++ -O3 -std=c++17 ...
#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <stdexcept>
using i64=std::int64_t;
int norm(i64 a,int p){ a%=p; return int(a<0?a+p:a); }
int leg(i64 a,int p){ i64 x=norm(a,p),r=1; if(!x)return 0; for(int e=(p-1)/2;e;e>>=1,x=x*x%p)if(e&1)r=r*x%p; return r==1?1:-1; }
int v2(int n){if(n<=0)throw std::runtime_error("nonpositive count");int r=0;while(!(n&1)){++r;n>>=1;}return r;}
int count(const std::vector<unsigned char>& roots,int p,int f0,int d1,int d2,int d3){
 int f=norm(f0,p),a=norm(d1,p),b=norm(d2,p),c=norm(d3,p),n=1;
 for(int x=0;x<p;++x){n+=roots[f];f+=a;if(f>=p)f-=p;a+=b;if(a>=p)a-=p;b+=c;if(b>=p)b-=p;}
 return n;
}
int main(int argc,char**argv){
 try{
 int bound=argc>1?std::stoi(argv[1]):100000;
 if(bound<20||bound>10000000)throw std::runtime_error("unsupported bound");
 std::vector<bool> sieve(bound,true);sieve[0]=sieve[1]=false;
 for(int i=2;i64(i)*i<bound;++i)if(sieve[i])for(int j=i*i;j<bound;j+=i)sieve[j]=false;
 std::cout<<"p,N_min,N_descent,trace,v2,chi2,chi_neg2,chi33,p_mod8,q_over3,q_over11,family\n";
 for(int p=3;p<bound;++p)if(sieve[p]&&p!=3&&p!=11){
  std::vector<unsigned char> roots(p,0);roots[0]=1;
  for(i64 y=1;y<=(p-1)/2;++y)roots[y*y%p]=2;
  int n=count(roots,p,-3,3,34,24),m=count(roots,p,0,82,40,6);
  int c3=leg(p,3),c11=leg(p,11),fam=p%8==5&&c3==-1&&c11==1;
  std::cout<<p<<','<<n<<','<<m<<','<<p+1-n<<','<<v2(n)<<','<<leg(2,p)<<','<<leg(-2,p)<<','<<leg(33,p)<<','<<p%8<<','<<c3<<','<<c11<<','<<fam<<'\n';
 }
 }catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}
}
