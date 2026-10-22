#!/usr/bin/env python3
import urllib.request,hashlib,json,concurrent.futures
from pathlib import Path
B=Path(__file__).resolve().parent
SHA='25cec5ecfec8b9f016eb1631ac633194c2bed39f'
labels={'1913b1','1913b2','2429b1','28042a1','28042a2','35882a1'}
paths=['allbsd/allbsd.00000-09999','allbsd/allbsd.20000-29999','allbsd/allbsd.30000-39999','allgens/allgens.20000-29999','allgens/allgens.30000-39999']
def fetch(path):
 u=f'https://raw.githubusercontent.com/JohnCremona/ecdata/{SHA}/{path}'
 raw=urllib.request.urlopen(u,timeout=45).read()
 lines=[]
 for i,line in enumerate(raw.decode().splitlines(),1):
  t=line.split()
  if ''.join(t[:3]) in labels:lines.append(dict(line_number=i,raw=line,label=''.join(t[:3])))
 return dict(path=path,url=u,downloaded_bytes=len(raw),downloaded_sha256=hashlib.sha256(raw).hexdigest(),selected_rows=lines)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(fetch,paths))
(B/'SELECTED_PRIMARY_ROWS.json').write_text(json.dumps(dict(commit=SHA,files=r),indent=2)+'\n')
for x in r:
 print(x['path'])
 for s in x['selected_rows']:print(s['raw'])
