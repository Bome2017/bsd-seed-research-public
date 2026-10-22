from pathlib import Path
from fractions import Fraction as F
import re,json,hashlib,subprocess,os,shutil,resource
r=Path(__file__).parent;ref=Path('/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run')
pat=re.compile(r'^XB (\d+) plus (.*?) cand (-?\d+)/(\d+) contains ([01]) unique ([01]) minus (.*?) cand (-?\d+)/(\d+) contains ([01]) unique ([01])$')
def interval(s):
 s=s.strip('[] ')
 if '+/-' in s:
  a,b=s.split('+/-'); mid=F(a.strip()) if a.strip() else F(0);rad=F(b.strip());return mid-rad,mid+rad
 v=F(s);return v,v
def read(p):
 result={}
 for line in p.read_text().splitlines():
  m=pat.match(line)
  if not m:continue
  g=m.groups();result[int(g[0])]=[(interval(g[1]),F(int(g[2]),int(g[3])),int(g[4]),int(g[5])),(interval(g[6]),F(int(g[7]),int(g[8])),int(g[9]),int(g[10]))]
 return result
res={};checks=0
for n in [27,81]:
 expected={int(x[0]):(F(x[1]),F(x[2])) for line in (ref/f'SYMBOLS_m{n}.txt').read_text().splitlines() if line and not line.startswith('#') for x in [line.split()]}
 ds=[read(r/f'm{n}_{path}.txt') for path in ['direct','dft']]
 for data in ds:
  assert set(data)==set(expected)
  for b,rec in data.items():
   for sign,((lo,hi),cand,has,unique) in enumerate(rec):
    value=expected[b][sign];assert cand==value and has==unique==1 and lo<=value<=hi and hi-lo<F(1,1024),(n,b,sign,rec)
    checks+=1
 for b in expected:
  for sign in [0,1]:
   (l,h)=ds[0][b][sign][0];(l2,h2)=ds[1][b][sign][0];assert max(l,l2)<=min(h,h2)
 res[str(n)]={'symbols':len(expected),'plus_and_minus_match_exact_retained_values':True,'both_paths':True,'printed_intervals_contain_reference_and_unique_lattice_point':True}
s=(r/'m27_direct.txt').read_text();assert 'CHUNK_DIGEST e24f3f4d4e705b42e6002bf8059430aa73ae3315bc437d2665bd99d151330681' in s
assert 'ca234d65fa40332695f5f08675ade782c9a8439bee068b69ac9b64a470002084 segments 288' in s
s=(r/'m81_dft.txt').read_text();assert 'A_EXACT LATDEN*a_{n,r} = 15851520' in s;assert 'mod p = 0   UNIT_TEST FAIL' in s
res.update(containment_checks=checks,m27_digest_matches_predeclared=True,m27_segment_root_matches_retained=True,m81_exact_anchor=15851520,m81_unit_test=False,m81_imported_checkpoints_not_full_replay=True)
(r/'REPLAY_COMPARISON.json').write_text(json.dumps(res,indent=2)+'\n')
neg={};nr=r/'negative_tests';nr.mkdir(exist_ok=True);fs=list((r/'m27').glob('ckpt_g*.bin'))
base=[str(r/'acc2243v2_codex'),'merge','0','-22735','0','106272484','0','27','2167729337579528','1','4831838207','16777216',str(ref/'ap')]
env={k:v for k,v in os.environ.items() if not k.startswith('ACC_')}
for typ in ['bitflip','missing_checkpoint','duplicate_checkpoint','delete_record_rehash','wrong_T']:
 d=nr/typ;d.mkdir(exist_ok=True)
 for f in fs:shutil.copyfile(f,d/f.name)
 f=d/fs[0].name
 if typ=='bitflip':
  b=bytearray(f.read_bytes());b[-90]^=1;f.write_bytes(b)
 elif typ=='missing_checkpoint':f.unlink()
 elif typ=='duplicate_checkpoint':shutil.copyfile(f,d/'ckpt_g002_w00.bin')
 elif typ=='delete_record_rehash':
  blob=f.read_bytes();body=blob[:-70];lines=body.split(b'\n');n=int(lines[3].split()[1]);assert lines[4].startswith(b'U ')
  lines[3]=b'NREC '+str(n-1).encode();del lines[4];body=b'\n'.join(lines);f.write_bytes(body+b'\nEND '+hashlib.sha256(body).hexdigest().encode()+b'\n')
 cmd=base.copy()
 if typ=='wrong_T':cmd[10]='4831838206'
 q=subprocess.run(cmd+[str(d),'1024'],capture_output=True,text=True,env=env,timeout=30)
 (nr/f'{typ}.log').write_text(q.stdout+q.stderr)
 neg[typ]={'exit_code':q.returncode,'stderr':q.stderr.strip()};assert q.returncode!=0,(typ,q.stdout)
(r/'NEGATIVE_TESTS.json').write_text(json.dumps(neg,indent=2)+'\n')
u=resource.getrusage(resource.RUSAGE_CHILDREN);(r/'NEGATIVE_TEST_RUNTIME.json').write_text(json.dumps({'user_seconds':u.ru_utime,'system_seconds':u.ru_stime})+'\n')
print(json.dumps({'comparison':res,'negative_tests':neg},indent=2))
