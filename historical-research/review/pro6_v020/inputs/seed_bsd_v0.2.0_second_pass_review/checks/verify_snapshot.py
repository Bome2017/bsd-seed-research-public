"""Verify the supplied release ZIP against its manifest and pinned Git tree.
This checks byte identity, not truth of mathematical claims. No extraction/write.
Usage: python verify_snapshot.py path/to/release.zip
"""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, stat, zipfile
P=argparse.ArgumentParser(description=__doc__)
P.add_argument('zipfile',type=Path)
a=P.parse_args()
EXPECTED='f008308751e76c052b248ff9672aa7bb976e4a94'
def obj(kind,data):
    return hashlib.sha1(kind.encode()+b' '+str(len(data)).encode()+b'\0'+data).digest()
with zipfile.ZipFile(a.zipfile) as z:
    files={}
    modes={}
    for x in z.infolist():
        p=PurePosixPath(x.filename)
        if p.is_absolute() or '..' in p.parts:raise ValueError('Unsafe member')
        if x.is_dir():continue
        if stat.S_ISLNK(x.external_attr>>16):raise ValueError('Unexpected symlink')
        rel=PurePosixPath(*p.parts[1:]).as_posix()
        if rel in files:raise ValueError('Duplicate file')
        files[rel]=z.read(x)
        modes[rel]=b'100755' if (x.external_attr>>16)&0o111 else b'100644'
    manifests=[n for n in files if '/' not in n and 'MANIFEST' in n.upper()]
    checked=0
    for n in manifests:
        for ln in files[n].decode().splitlines():
            if not ln.strip() or ln.startswith('#'):continue
            h,rel=ln.split(maxsplit=1);rel=rel.lstrip('*').removeprefix('./')
            if len(h)!=64:raise ValueError('Unexpected manifest format')
            assert hashlib.sha256(files[rel]).hexdigest()==h,rel
            checked+=1
    root={}
    for rel,data in files.items():
        node=root;parts=rel.split('/')
        for d in parts[:-1]:node=node.setdefault(d,{})
        node[parts[-1]]=(modes[rel],obj('blob',data))
    def tree(node):
        body=b''
        for name,val in sorted(node.items(),key=lambda kv:(kv[0]+('/' if isinstance(kv[1],dict) else '')).encode()):
            mode,digest=(b'40000',tree(val)) if isinstance(val,dict) else val
            body+=mode+b' '+name.encode()+b'\0'+digest
        return obj('tree',body)
    th=tree(root).hex()
    assert th==EXPECTED,(th,EXPECTED)
    print(json.dumps({'zip_sha256':hashlib.sha256(a.zipfile.read_bytes()).hexdigest(),'files':len(files),'manifest_entries_verified':checked,'git_tree':th,'matches_pinned_commit_tree':True},indent=2))
