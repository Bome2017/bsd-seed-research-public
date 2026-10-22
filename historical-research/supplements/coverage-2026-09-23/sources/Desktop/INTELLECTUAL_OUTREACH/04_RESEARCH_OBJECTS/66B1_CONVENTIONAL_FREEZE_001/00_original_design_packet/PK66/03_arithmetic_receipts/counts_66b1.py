def isp(n):
    if n<2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%p==0: return n==p
    d,s=n-1,0
    while d%2==0: d//=2; s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x=pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return True
def leg(a,p):
    a%=p
    return 0 if a==0 else (1 if pow(a,(p-1)//2,p)==1 else -1)
def cnt_min(q):   # 66b1: y^2 + xy + y = x^3 + x^2 - 2x - 1
    qr=bytearray(q)
    for t in range(1,(q+1)//2): qr[(t*t)%q]=1
    n=1
    for u in range(q):
        rhs=(u*u*u+u*u-2*u-1)%q; b=(u+1)%q; d=(b*b+4*rhs)%q
        n+=1 if d==0 else (2 if qr[d] else 0)
    return n
def cnt_E1(q):    # descent model: Y^2 = X^3 + 17X^2 + 64X
    qr=bytearray(q)
    for t in range(1,(q+1)//2): qr[(t*t)%q]=1
    n=1
    for x in range(q):
        r=(x*x*x+17*x*x+64*x)%q
        n+=1 if r==0 else (2 if qr[r] else 0)
    return n
def v2(n):
    k=0
    while n%2==0: n//=2;k+=1
    return k
print("66b1 = LMFDB 66.b4, minimal model  y^2 + xy + y = x^3 + x^2 - 2x - 1")
print("descent model candidate            Y^2 = X^3 + 17X^2 + 64X   (A=17, B=64, A^2-4B=33)")
print("Delta(minimal) = 528 = 2^4*3*11    Delta(Y^2=X^3+17X^2+64X) = 16*64^2*33 =", 16*64*64*33, "= 2^16*3*11")
print()
print("q      q%8 (q/3) (q/11)  #E_min  #E_desc  v2  a_q   in_family")
rows=[]
for q in range(3,4000):
    if not isp(q) or q in (2,3,11): continue
    if q%8!=5: continue
    if leg(q,3)!=-1 or leg(q,11)!=1: continue
    nm=cnt_min(q); nd=cnt_E1(q); a=q+1-nm
    fam = (v2(nm)==2 and a!=0)
    rows.append((q,nm,nd,v2(nm),a,fam))
    if len(rows)<=14:
        print(f"{q:6d}  {q%8:3d} {leg(q,3):+4d} {leg(q,11):+5d} {nm:8d} {nd:8d} {v2(nm):3d} {a:5d}   {fam}")
print(f"... {len(rows)} primes below 4000 satisfying q=5(8), (q/3)=-1, (q/11)=+1")
print(f"model counts agree on all of them : {all(r[1]==r[2] for r in rows)}")
from collections import Counter
print(f"v2 distribution                   : {dict(sorted(Counter(r[3] for r in rows).items()))}")
print(f"a_q = 0 anywhere                  : {[r[0] for r in rows if r[4]==0]}")
print()
print("CONTROL - the two quadratic characters that governed 62a1, computed for 66b1's discriminant 33:")
b2=Counter(); 
for q in range(3,4000):
    if not isp(q) or q in (2,3,11): continue
    b2[(leg(2,q),leg(33,q))].setdefault if False else None
    b2[(leg(2,q),leg(33,q),v2(cnt_min(q)))]+=1
agg={}
for (c2,c33,k),n in b2.items(): agg.setdefault((c2,c33),Counter())[k]+=n
for k in sorted(agg): print(f"  (2/q)={k[0]:+d}  (33/q)={k[1]:+d} :  v2 histogram {dict(sorted(agg[k].items()))}")
