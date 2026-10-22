"""Verify all bound archives, extract safely, then verify all listed files.

This program reads no credentials, uses no network, and executes no archive
member. Re-running verifies existing trees without overwriting their files.
"""
from pathlib import Path, PurePosixPath
import hashlib
import json
import os
import shutil
import stat
import zipfile

ROOT = Path(__file__).resolve().parent

def sha_file(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def safe_name(name):
    p = PurePosixPath(name)
    if not name or p.is_absolute() or '..' in p.parts or '\\' in name or ':' in name:
        raise ValueError('unsafe member name: ' + name)
    return p

def verify_tree(root, manifest_name, expected_count):
    manifest = root.joinpath(*safe_name(manifest_name).parts)
    listed = set()
    for line in manifest.read_text().splitlines():
        expected, name = line.split('  ', 1)
        rel = safe_name(name)
        if name in listed:
            raise ValueError('duplicate manifest path: ' + name)
        listed.add(name)
        path = root.joinpath(*rel.parts)
        if any(p.is_symlink() for p in [path, *path.parents] if p != root.parent):
            raise ValueError('symlink in extracted tree: ' + name)
        if sha_file(path) != expected:
            raise ValueError('member digest mismatch: ' + name)
    if len(listed) != expected_count:
        raise ValueError('manifest entry count mismatch')
    return len(listed)

def extract(binding):
    archive = ROOT.joinpath(*safe_name(binding['path']).parts)
    if archive.stat().st_size != binding['bytes'] or sha_file(archive) != binding['sha256']:
        raise ValueError('archive binding mismatch: ' + binding['path'])
    dest = ROOT.joinpath(*safe_name(binding['destination']).parts)
    if dest.is_symlink():
        raise ValueError('destination is a symlink')
    if not dest.exists():
        # A private empty directory prevents collision with user files.
        staging = dest.with_name(dest.name + '.extracting')
        staging.mkdir(exist_ok=False)
        with zipfile.ZipFile(archive) as z:
            seen = set()
            total = 0
            for info in z.infolist():
                rel = safe_name(info.filename)
                name = str(rel)
                if name in seen:
                    raise ValueError('duplicate ZIP path: ' + name)
                seen.add(name)
                mode = (info.external_attr >> 16) & 0xffff
                if stat.S_ISLNK(mode) or stat.S_IFMT(mode) not in (0, stat.S_IFREG, stat.S_IFDIR):
                    raise ValueError('non-regular ZIP member: ' + name)
                if rel.parts[0] != binding['root']:
                    raise ValueError('unexpected archive root')
                total += info.file_size
            if total != binding['expanded_bytes']:
                raise ValueError('expanded byte count mismatch')
            for info in z.infolist():
                out = staging.joinpath(*safe_name(info.filename).parts)
                if info.is_dir():
                    out.mkdir(parents=True, exist_ok=True)
                else:
                    out.parent.mkdir(parents=True, exist_ok=True)
                    with z.open(info) as source, out.open('xb') as target:
                        shutil.copyfileobj(source, target)
        base = staging / binding['root']
        verify_tree(base, binding['manifest'], binding['manifest_entries'])
        os.rename(staging, dest)
    base = dest / binding['root']
    count = verify_tree(base, binding['manifest'], binding['manifest_entries'])
    return {'root': str(base), 'members_checked': count, 'archive_sha256': binding['sha256']}

if __name__ == '__main__':
    bindings = json.loads((ROOT / 'REFERENCE_BINDINGS.json').read_text())
    results = [extract(binding) for binding in bindings]
    print(json.dumps({'status': 'READING_SETS_VERIFIED', 'archives': results,
                      'members_checked': sum(r['members_checked'] for r in results),
                      'research_files_read_by_this_program': 0,
                      'mathematical_claims_verified': False}, indent=2))
