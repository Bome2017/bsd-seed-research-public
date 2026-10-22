// Independent recount: direct polynomial evaluation, not the retained finite-difference algorithm.
// Usage: referee_counts [exclusive_bound]; writes CSV to stdout.
#include <iostream>
#include <vector>
#include <cstdint>
#include <stdexcept>
int main(int argc,char**argv) {
  try {
    int B=argc>1?std::stoi(argv[1]):100000;
    if(B<6 || B>1000000) throw std::runtime_error("bound must be in [6,1000000]");
    std::vector<bool> prime(B,true); prime[0]=prime[1]=false;
    for(int i=2;i<= (B-1)/i;++i) if(prime[i])
      for(int j=i*i;j<B;j+=i) prime[j]=false;
    std::cout<<"p,N_min,N_descent\n";
    for(int p=5;p<B;++p) if(prime[p] && p!=11) {
      std::vector<unsigned char> multiplicity(p,0);
      for(int64_t y=0;y<p;++y) ++multiplicity[(y*y)%p];
      int nmin=1,nd=1;
      for(int64_t x=0;x<p;++x) {
        // (2y+x+1)^2 = 4x^3+5x^2-6x-3 on the original minimal equation.
        int64_t a=(((4*x+5)*x-6)*x-3)%p;
        if(a<0) a+=p;
        int64_t b=x*(x*x+17*x+64)%p;
        nmin+=multiplicity[a]; nd+=multiplicity[b];
      }
      std::cout<<p<<','<<nmin<<','<<nd<<'\n';
    }
  } catch(const std::exception&e) { std::cerr<<e.what()<<'\n'; return 1; }
}
