#!/usr/bin/env python3
"""Read the self-contained BSD evidence archive. Python standard library only.
No network, source execution, Aristotle submission, or credentials are used.
"""
import argparse,sqlite3,gzip,hashlib,json,tempfile,shutil,zipfile,sys,os
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(4*2**20),b''):h.update(b)
    return h.hexdigest()
def database():
    spec=json.loads((ROOT/'coverage/CATALOG_PARTS.json').read_text());key=spec['sha256']
    cache=Path(tempfile.gettempdir())/('bsd-record-'+key[:24]);cache.mkdir(exist_ok=True)
    target=cache/'catalog.sqlite'
    if not target.exists():
        compressed=cache/('catalog-'+str(os.getpid())+'.gz');h=hashlib.sha256()
        with compressed.open('wb') as out:
            for part in spec['parts']:
                data=(ROOT/part['path']).read_bytes()
                if hashlib.sha256(data).hexdigest()!=part['sha256']:raise ValueError('Catalog part mismatch')
                out.write(data);h.update(data)
        if h.hexdigest()!=key:raise ValueError('Catalog digest mismatch')
        tmp=cache/('catalog-'+str(os.getpid())+'.tmp')
        with gzip.open(compressed,'rb') as a,tmp.open('wb') as b:shutil.copyfileobj(a,b)
        tmp.replace(target);compressed.unlink()
    db=sqlite3.connect('file:'+str(target)+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;return db
def resolve(db,path):
    r=db.execute('select * from files where path=?',(path,)).fetchone()
    if r is None:raise ValueError('Original path not in catalog. Use find to locate the exact identity.')
    return r
def object_bytes(db,h):
    rows=db.execute('select * from chunks where sha256=? order by ordinal',(h,)).fetchall()
    if not rows:raise ValueError('No embedded byte object for this digest.')
    data=bytearray()
    for r in rows:
        with zipfile.ZipFile(ROOT/r['volume']) as z:data.extend(z.read(r['member']))
    if hashlib.sha256(data).hexdigest()!=h:raise ValueError('Evidence digest mismatch')
    return bytes(data)
def get(db,r,local=False):
    if r['object_path']:return object_bytes(db,r['sha256'])
    if local and r['sha256']:
        p=Path(r['path'])
        if not p.is_file():raise ValueError('External source is absent on this computer.')
        data=p.read_bytes()
        if hashlib.sha256(data).hexdigest()!=r['sha256']:raise ValueError('External source changed since capture.')
        return data
    raise ValueError('Bytes not embedded: '+r['disposition']+'; '+str(r['detail']))
def write_exact(dest,data):
    if dest.exists() and dest.read_bytes()!=data:raise ValueError('Refusing to overwrite a different file: '+str(dest))
    dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
def main():
    ap=argparse.ArgumentParser(description=__doc__);sp=ap.add_subparsers(dest='cmd',required=True)
    sp.add_parser('info')
    for cmd in ['find','search']:
        q=sp.add_parser(cmd);q.add_argument('query');q.add_argument('--limit',type=int,default=50)
    q=sp.add_parser('show');q.add_argument('path');q.add_argument('--start',type=int,default=1);q.add_argument('--end',type=int)
    q=sp.add_parser('extract');q.add_argument('path');q.add_argument('--output',type=Path,required=True);q.add_argument('--include-bulk-from-local',action='store_true')
    q=sp.add_parser('restore');q.add_argument('root');q.add_argument('--to',type=Path,required=True);q.add_argument('--include-bulk-from-local',action='store_true')
    q=sp.add_parser('unit');q.add_argument('id')
    q=sp.add_parser('history');q.add_argument('name',choices=['research','cloud-lab','current-lab']);q.add_argument('--output',type=Path,required=True)
    q=sp.add_parser('verify');q.add_argument('--deep',action='store_true')
    a=ap.parse_args()
    if a.cmd=='history':
        r=next(x for x in json.loads((ROOT/'history/INDEX.json').read_text()) if x['name']==a.name)
        if a.output.exists():raise ValueError('Refusing to overwrite '+str(a.output))
        a.output.parent.mkdir(parents=True,exist_ok=True);h=hashlib.sha256()
        with a.output.open('wb') as out:
            for part in r['parts']:
                data=(ROOT/part['path']).read_bytes()
                if hashlib.sha256(data).hexdigest()!=part['sha256']:raise ValueError('Git bundle part mismatch')
                h.update(data);out.write(data)
        if h.hexdigest()!=r['sha256']:raise ValueError('Assembled bundle mismatch')
        print(a.output);return
    if a.cmd=='unit':
        units=json.loads((ROOT/'sources/KNOWLEDGE_UNITS.json').read_text())
        matches=[u for u in units if u.get('id')==a.id]
        if not matches:raise ValueError('No such compendium unit')
        print(json.dumps(matches[0],indent=2,ensure_ascii=False));return
    if a.cmd=='verify':
        count=0
        for line in (ROOT/'MANIFEST.sha256').read_text().splitlines():
            h,path=line.split('  ',1);p=ROOT/path
            if not p.is_file() or digest(p)!=h:raise ValueError('Manifest mismatch: '+path)
            count+=1
        print('Manifest entries verified:',count)
        if a.deep:
            db=database();expected={r[0] for r in db.execute('select sha256 from objects')}
            verified=set();current=None;h=None
            for part in json.loads((ROOT/'evidence/VOLUMES.json').read_text()):
                with zipfile.ZipFile(ROOT/part['path']) as z:
                    for item in z.infolist():
                        key=item.filename.split('/')[0]
                        if key!=current:
                            if current is not None:
                                if h.hexdigest()!=current:raise ValueError('Evidence object mismatch: '+current)
                                verified.add(current)
                            current=key;h=hashlib.sha256()
                        with z.open(item) as f:
                            for b in iter(lambda:f.read(4*2**20),b''):h.update(b)
            if current is not None:
                if h.hexdigest()!=current:raise ValueError('Evidence object mismatch: '+current)
                verified.add(current)
            if verified!=expected:raise ValueError('Evidence catalog/object set mismatch')
            print('Reconstructed evidence objects verified:',len(verified))
        return
    db=database()
    if a.cmd=='info':
        print(json.dumps({'paths':db.execute('select count(*) from files').fetchone()[0],'unique_embedded_objects':db.execute('select count(*) from objects').fetchone()[0],'dispositions':{r[0]:r[1] for r in db.execute('select disposition,count(*) from files group by disposition')}},indent=2));return
    if a.cmd=='find':
        rows=db.execute('select path,disposition,sha256 from files where instr(lower(path),lower(?))>0 order by length(path),path limit ?',(a.query,a.limit))
        for r in rows:print(r['path']+'\t'+r['disposition']+'\t'+str(r['sha256']))
        return
    if a.cmd=='search':
        query='"'+a.query.replace('"','""')+'"'
        rows=db.execute('select l.path,l.sha256,l.indexed_bytes,l.full_bytes from text_search f join text_lookup l on l.id=f.rowid where text_search match ? limit ?',(query,a.limit))
        for r in rows:print(r['path']+'\t'+r['sha256']+(' [prefix indexed]' if r['indexed_bytes']<r['full_bytes'] else ''))
        return
    if a.cmd=='show':
        data=get(db,resolve(db,a.path))
        try:lines=data.decode('utf-8').splitlines()
        except UnicodeDecodeError:raise ValueError('Binary source; use extract.')
        for i in range(max(a.start-1,0),min(a.end or len(lines),len(lines))):print(f'{i+1}: {lines[i]}')
        return
    if a.cmd=='extract':
        write_exact(a.output,get(db,resolve(db,a.path),a.include_bulk_from_local));print(a.output);return
    if a.cmd=='restore':
        prefix=a.root.rstrip('/')+'/';rows=db.execute('select * from files where substr(path,1,?)=? order by path',(len(prefix),prefix)).fetchall()
        if not rows:raise ValueError('No catalog paths beneath this root.')
        skipped=[];n=0
        for r in rows:
            relative=Path(r['path'][len(prefix):])
            if '..' in relative.parts or relative.is_absolute():raise ValueError('Unsafe path in catalog')
            try:data=get(db,r,a.include_bulk_from_local)
            except ValueError as e:skipped.append({'path':r['path'],'reason':str(e)});continue
            write_exact(a.to/relative,data);n+=1
        a.to.mkdir(parents=True,exist_ok=True)
        (a.to/'RESTORE_RECEIPT.json').write_text(json.dumps({'source_root':a.root,'restored':n,'skipped':skipped},indent=2)+'\n')
        print(json.dumps({'restored':n,'skipped':len(skipped),'receipt':str(a.to/'RESTORE_RECEIPT.json')},indent=2))
if __name__=='__main__':
    try:main()
    except (ValueError,OSError,sqlite3.Error,zipfile.BadZipFile) as e:sys.exit(str(e))
