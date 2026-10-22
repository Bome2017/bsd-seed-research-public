"""Independent checks of PROOF.md sections 2,4,5 and 7 that are finite group theory or congruences."""
import json, itertools
out={}
# (1) 24 | n^2  =>  12 | n
out["n_mod12_when_24_divides_n_squared"]=sorted({n%12 for n in range(1,10000) if (n*n)%24==0})
# (2) C1 congruences imply C60 congruences
out["C1_implies_C60"]=all((m%120==11) for m in range(1,200000) if m%840==491) and all(n%60==0 for n in range(420,200000,420))
# (3) C60 implies Zywina's 11 mod 24 for m, A, B
bad=[]
for m in [11,131,251,371,491,611,731,851,971,1091,3491,3011]:
    if m%120!=11: continue
    for n in [60,120,180,420,600]:
        for v in (m, m+16*n*n, m+25*n*n):
            if v%24!=11: bad.append((m,n,v))
out["C60_gives_11_mod_24_for_m_A_B"]=(bad==[])
# (4) the local matrix picture at A: T^2=-I, det T=1, F T F^-1 = T^-1  =>  no common invariant line
def mats(l): return [(a,b,c,d) for a in range(l) for b in range(l) for c in range(l) for d in range(l) if (a*d-b*c)%l]
def mm(x,y,l): return ((x[0]*y[0]+x[1]*y[2])%l,(x[0]*y[1]+x[1]*y[3])%l,(x[2]*y[0]+x[3]*y[2])%l,(x[2]*y[1]+x[3]*y[3])%l)
def inv(x,l):
    d=pow((x[0]*x[3]-x[1]*x[2])%l,l-2,l); return ((x[3]*d)%l,(-x[1]*d)%l,(-x[2]*d)%l,(x[0]*d)%l)
def lines(l): return [(1,t) for t in range(l)]+[(0,1)]
def act(x,v,l): return ((x[0]*v[0]+x[1]*v[1])%l,(x[2]*v[0]+x[3]*v[1])%l)
def same_line(u,v,l):
    return (u[0]*v[1]-u[1]*v[0])%l==0 and (u!=(0,0) and v!=(0,0))
res={}
for l in [3,5,7,11,13]:
    G=mats(l); mI=((-1)%l,0,0,(-1)%l)
    T=next(t for t in G if mm(t,t,l)==mI and (t[0]*t[3]-t[1]*t[2])%l==1)   # all such T are conjugate (min poly x^2+1)
    Ts=[t for t in G if mm(t,t,l)==mI and (t[0]*t[3]-t[1]*t[2])%l==1]
    Tinv=inv(T,l)
    Fs=[f for f in G if mm(mm(f,T,l),inv(f,l),l)==Tinv]
    stable=[]
    for f in Fs:
        for v in lines(l):
            if same_line(act(T,v,l),v,l) and same_line(act(f,v,l),v,l): stable.append((f,v))
    # transvection + its lower conjugate generate SL_2(F_l)?
    up=(1,1,0,1); lo=(1,0,1,1)
    S={(1,0,0,1)}; fr=[(1,0,0,1)]
    while fr:
        x=fr.pop()
        for g in (up,lo):
            y=mm(x,g,l)
            if y not in S: S.add(y); fr.append(y)
    res[l]={"count_T_with_Tsq_minusI_det1":len(Ts),"T_is_nonscalar":T[1]%l!=0 or T[2]%l!=0,
            "num_F_with_conjugation_to_inverse":len(Fs),"common_invariant_lines":len(stable),
            "order_generated_by_upper_and_lower_transvections":len(S),"SL2_order":l*(l*l-1)}
out["local_matrix_and_group_lemma"]=res
out["all_no_common_line"]=all(v["common_invariant_lines"]==0 for v in res.values())
out["all_generate_SL2"]=all(v["order_generated_by_upper_and_lower_transvections"]==v["SL2_order"] for v in res.values())
print(json.dumps(out,indent=1))
