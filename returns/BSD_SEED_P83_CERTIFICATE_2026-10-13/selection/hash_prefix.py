import hashlib,json,pathlib,time,concurrent.futures,os
out=pathlib.Path(__file__).parent
view=pathlib.Path('/Users/bsm/BSD_P17_PREREQUISITES_2026-09-25/singleton_probe/corpus_ext_6445/view')
k=3420; records={}
for p in view.joinpath('logs').glob('ver_*.log'):
 for line in p.read_text().splitlines():
  row=line.split()
  if row and row[0]=='SEG':
   n=int(row[1]);sha=row[-1]
   if n in records:assert records[n]['sha256']==sha
   records[n]={'sha256':sha,'receipt_path':str(p),'receipt_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'line':line}
assert all(i in records for i in range(6445))
root=lambda n:hashlib.sha256(b''.join(bytes.fromhex(records[i]['sha256']) for i in range(n))).hexdigest()
assert root(6445)=='92cd0222d32e722087897738839a560b24af45a9a44221c6271502e0ed7de60f'
assert root(4802)=='c329c118a1f992b341fb45899b408a551d3f2503d4d313ac3b99a7da0f343f20'
start=time.monotonic()
def work(i):
 p=view/'ap'/f'ap_{i:06d}.bin';before=p.stat();h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 after=p.stat();good=h.hexdigest()==records[i]['sha256']
 assert (before.st_size,before.st_mtime_ns,before.st_ino)==(after.st_size,after.st_mtime_ns,after.st_ino)
 assert good,('MISMATCH',i)
 return {'segment':i,'path':str(p),'resolved_path':str(p.resolve()),'size':before.st_size,'mtime_ns':before.st_mtime_ns,'inode':before.st_ino,**records[i],'match':True}
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for i,r in enumerate(pool.map(work,range(k)),1):
  results.append(r)
  if i%200==0:(out/'CUSTODY_STATUS.json').write_text(json.dumps({'status':'RUNNING','hashed':i,'required':k,'elapsed':time.monotonic()-start})+'\n')
receipt={'status':'PASS','segments':k,'bytes':sum(r['size'] for r in results),'elapsed_seconds':time.monotonic()-start,'workers':2,'prefix_root':root(k),'full_receipt_root_6445':root(6445),'coefficient_hashes_matched':k,'coefficients_recomputed':False,'source_mutation_detected':False,'rows':results}
(out/'PREFIX_3420_CUSTODY.json').write_text(json.dumps(receipt,indent=2)+'\n')
(out/'CUSTODY_STATUS.json').write_text(json.dumps({x:y for x,y in receipt.items() if x!='rows'},indent=2)+'\n')
print(json.dumps({x:y for x,y in receipt.items() if x!='rows'},indent=2))
