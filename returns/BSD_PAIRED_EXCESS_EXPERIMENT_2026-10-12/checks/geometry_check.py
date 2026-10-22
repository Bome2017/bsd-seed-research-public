"""Small exact check of the actual new residual geometry; not seed arithmetic."""
import json
from pathlib import Path
p=5;M=[[-2,1],[-1,-2]];H=[[4,2],[2,1]];ell=[1,3];v=[1,3]
def dot(a,b):return sum(x*y for x,y in zip(a,b))%p
def mv(a,v):return [dot(r,v) for r in a]
def mm(a,b):return [[dot(r,c) for c in zip(*b)] for r in a]
assert (M[0][0]*M[1][1]-M[0][1]*M[1][0])==5
assert (H[0][0]*H[1][1]-H[0][1]*H[1][0])%p==0 and H[0][0]%p
assert mv(H,v)==[0,0] and dot(ell,v)==0
assert mm(list(map(list,zip(*M))),mm(H,M))==[[0,0],[0,0]]
assert [dot(ell,c) for c in zip(*M)]==[0,0]
assert all(mv(H,list(c))==[0,0] for c in zip(*M))
r={'height_rank_mod5':1,'height_radical_generator':v,'logarithm_kernel_generator':v,'lines':'COINCIDENT','F_local_point_index':0,'A_local_point_index':1,'A_index_reason':'ell_A=ell_F M; det M=5; ell_A=0 mod5 and ell_F nonzero mod5','not_seed17_distinct_line_geometry':True}
Path('outputs/GEOMETRY_CHECK.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
