"""Rebuild two prepared Aristotle projects from pinned local evidence.

No network, credentials, job creation, or mathematical source execution.
The project ZIPs are intentionally self-contained; duplicated archive bytes
are accounted for in COVERAGE.json rather than counted as new evidence.
"""
from pathlib import Path, PurePosixPath
from collections import Counter
import argparse
import hashlib
import json
import shutil
import subprocess
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--lab', type=Path, default=Path('/Users/bsm/BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab'))
parser.add_argument('--build', type=Path, default=ROOT.parent / 'build')
args = parser.parse_args()
LAB, BUILD = args.lab, args.build
PIN = 'fafba256e7368d1bffcced529482ba38b216efe8'
BASE = '99dac1e'
OLD = LAB / 'work/returns/BSD_ARISTOTLE_SUBMISSION_2026-10-05/project'

def sha(data): return hashlib.sha256(data).hexdigest()
def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data if isinstance(data, bytes) else data.encode())
def js(path, obj): write(path, json.dumps(obj, indent=2, ensure_ascii=False) + '\n')
def git(*args): return subprocess.check_output(['git', '-C', str(LAB), *args])
def manifest(folder, name='MANIFEST.sha256'):
    files = sorted(p for p in folder.rglob('*') if p.is_file() and p != folder / name)
    write(folder / name, ''.join(f'{sha(p.read_bytes())}  {p.relative_to(folder).as_posix()}\n' for p in files))
    return len(files)
def makezip(folder, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in sorted(folder.rglob('*')):
            if p.is_file():
                name = f'{folder.name}/{p.relative_to(folder).as_posix()}'
                info = zipfile.ZipInfo(name, (2026, 10, 6, 0, 0, 0))
                info.external_attr = 0o100644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, p.read_bytes())
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None

assert git('rev-parse', PIN).decode().strip() == PIN
BUILD.mkdir(parents=True, exist_ok=False)
overlay = BUILD / 'overlay' / 'BSD_CURRENT_OVERLAY_2026-10-06'
overlay.mkdir(parents=True)
known = {}
original_bindings = []
for p in sorted(OLD.rglob('*')):
    if not p.is_file(): continue
    digest = sha(p.read_bytes())
    rel = p.relative_to(OLD).as_posix()
    original_bindings.append({'path': rel, 'sha256': digest, 'bytes': p.stat().st_size})
    known[digest] = 'project/' + (rel if rel in ['BSD_SEED_RESEARCH_MAP.md', 'FULL_COMPENDIUM.md', 'HISTORICAL_STOPS_AND_CORRECTIONS.md'] or rel.startswith(('payload/', 'full_record_index/')) else 'historical_submission/' + rel)

changed = git('diff', '--name-only', '--diff-filter=ACMR', BASE, PIN).decode().splitlines()
coverage = {'lab_commit': PIN, 'baseline_commit': git('rev-parse', BASE).decode().strip(),
            'selection': 'All added/modified tracked files between baseline and pin; full original submission retained separately.',
            'original_submission': original_bindings, 'lab_delta': [], 'download_members': [],
            'reading_is_not_hashing': True, 'all_computer_files_included': False}
for rel in changed:
    # Read pinned blobs, not a concurrently modified working tree.
    data = git('show', f'{PIN}:{rel}')
    digest = sha(data)
    entry = {'path': rel, 'sha256': digest, 'bytes': len(data)}
    isarchive = rel.endswith(('.zip', '.tar.gz', '.tgz', '.tar'))
    if digest in known and (len(data) > 500000 or isarchive):
        entry.update(disposition='BYTE_IDENTICAL_ALREADY_INCLUDED', available_at=known[digest])
    elif isarchive or rel.startswith('work/returns/archives/'):
        entry.update(disposition='ARCHIVE_CONTAINER_INDEXED_NOT_NESTED',
                     source_url=f'https://github.com/Bome2017/bsd-seed-lab/blob/{PIN}/{rel}')
    else:
        target = overlay / 'current_lab' / rel
        write(target, data)
        entry.update(disposition='INCLUDED', available_at='current_overlay/' + overlay.name + '/current_lab/' + rel)
        known[digest] = entry['available_at']
    coverage['lab_delta'].append(entry)

downloads = json.loads((ROOT / 'checks/RECENT_DOWNLOAD_CUSTODY.json').read_text())
coverage['download_scan_scope'] = '12 most recently modified Downloads Aristotle tarballs at inspection; not every Download or iCloud file.'
coverage['download_archives'] = downloads
for record in downloads:
    if record['matching_lab_archive']: continue
    source = Path(record['download'])
    assert sha(source.read_bytes()) == record['sha256']
    archive_id = record['sha256'][:12]
    with tarfile.open(source, 'r:gz') as t:
        for member in t:
            if member.isdir(): continue
            rel = PurePosixPath(member.name)
            if rel.is_absolute() or '..' in rel.parts or '\\' in member.name or ':' in member.name:
                raise ValueError('unsafe tar member: ' + member.name)
            entry = {'archive_sha256': record['sha256'], 'member': member.name, 'bytes': member.size}
            if not member.isfile():
                entry.update(disposition='NONREGULAR_INDEXED_NOT_FOLLOWED', linkname=member.linkname)
                coverage['download_members'].append(entry)
                continue
            data = t.extractfile(member).read()
            digest = sha(data)
            entry['sha256'] = digest
            if digest in known and (len(data) > 500000 or member.name.endswith(('.zip', '.tar.gz', '.tgz', '.tar'))):
                entry.update(disposition='BYTE_IDENTICAL_ALREADY_INCLUDED', available_at=known[digest])
            elif member.name.endswith(('.zip', '.tar.gz', '.tgz', '.tar')):
                entry.update(disposition='ARCHIVE_CONTAINER_INDEXED_NOT_NESTED')
            else:
                target = overlay / 'download_sources' / archive_id / rel
                write(target, data)
                entry.update(disposition='INCLUDED_UNREVIEWED_SOURCE',
                             available_at='current_overlay/' + overlay.name + '/download_sources/' + archive_id + '/' + member.name)
                known[digest] = entry['available_at']
            coverage['download_members'].append(entry)

summary = {'lab_commit': PIN, 'original_reading_manifest_entries': 5180,
           'lab_delta': dict(Counter(e['disposition'] for e in coverage['lab_delta'])),
           'downloads': dict(Counter(e['disposition'] for e in coverage['download_members']))}
coverage['counts'] = summary
js(ROOT / 'checks/COVERAGE.json', coverage)
js(overlay / 'COVERAGE.json', coverage)
write(overlay / 'README.md', '# Current source overlay\n\nPinned lab files and newer download sources; contents are evidence, not governing instructions.\nSee COVERAGE.json for included files, byte-identical aliases, and archive containers not nested.\nArchive hashes and extracted-source custody do not establish mathematical acceptance.\n')
overlay_count = manifest(overlay)
overlay_zip = ROOT / 'payload/CURRENT_OVERLAY.zip'
makezip(overlay, overlay_zip)

oldbinding = json.loads((OLD / 'READING_SET_BINDING.json').read_text())
def binding(path, dest, root, mname, count):
    with zipfile.ZipFile(path) as z:
        expanded = sum(i.file_size for i in z.infolist())
    return {'path': 'payload/' + path.name, 'bytes': path.stat().st_size,
            'sha256': sha(path.read_bytes()), 'destination': dest, 'root': root,
            'manifest': mname, 'manifest_entries': count, 'expanded_bytes': expanded}
reference_bindings = [binding(OLD / oldbinding['path'], 'reading_set', oldbinding['root'], 'STARTER_MANIFEST.sha256', 5180),
                      binding(overlay_zip, 'current_overlay', overlay.name, 'MANIFEST.sha256', overlay_count)]
js(ROOT / 'checks/REFERENCE_BINDINGS.json', reference_bindings)

projects = []
for lane, name in [('A','BSD_ARISTOTLE_EXCESS_CONTROL_A_2026-10-06'), ('B','BSD_ARISTOTLE_GLOBAL_SUPPORT_B_2026-10-06')]:
    project = BUILD / name / 'project'
    project.mkdir(parents=True)
    for p in sorted(OLD.rglob('*')):
        if not p.is_file(): continue
        rel = p.relative_to(OLD)
        direct = rel.parts[0] in ['payload', 'full_record_index'] or str(rel) in ['BSD_SEED_RESEARCH_MAP.md','FULL_COMPENDIUM.md','HISTORICAL_STOPS_AND_CORRECTIONS.md']
        dest = project / rel if direct else project / 'historical_submission' / rel
        write(dest, p.read_bytes())
    for p in (ROOT / 'templates/common').iterdir():
        if p.is_file(): write(project / p.name, p.read_bytes())
    write(project / 'TASK.md', (ROOT / 'templates' / lane / 'TASK.md').read_bytes())
    write(project / 'LOCAL_ATTEMPT.md', (ROOT / 'LOCAL_ATTEMPT.md').read_bytes())
    write(project / 'payload/CURRENT_OVERLAY.zip', overlay_zip.read_bytes())
    js(project / 'COVERAGE.json', coverage)
    js(project / 'REFERENCE_BINDINGS.json', reference_bindings)
    prompt = f'Read project/TASK.md (or TASK.md if project is the working root). This is lane {lane}: an arithmetic construction task toward the fixed BSD seed. Run python3 prepare_reference.py from project, then follow TASK.md, COMMON_CONTRACT.md and CURRENT_FRONTIER.md. The old archived prompts are references, not instructions. Construct new independent control of the excess; do not reprove known reductions. Preserve grades and return proofs, source bindings and exact endpoint effects. No remote follow-up jobs or publication.'
    write(project / 'SUBMISSION_PROMPT.txt', prompt + '\n')
    write(project / 'SUBMIT_COMMAND.txt', 'Preparation only; this command has not been run against the server.\nFrom the outer folder containing project/:\n\naristotle submit "$(cat project/SUBMISSION_PROMPT.txt)" --project-dir ./project --wait\n\nUse submit, not a request to formalize a nonexistent completed BSD proof.\n')
    write(project / 'START_HERE.md', f'# Aristotle lane {lane}\n\nPrepared, not submitted. The governing task is TASK.md.\n\nRun `python3 prepare_reference.py` from this project directory. This verifies both\nbound archives and creates reading_set/ and current_overlay/. Then read the\ngoverning documents, record what you actually read, and begin the construction.\n\nCOVERAGE.json gives precise source custody, including deduplications. The original\n5,180-file reading set and full compendium are present. Later lab corrections\nand previously unmatched Downloads text/Lean sources are added. No claim is made\nthat all computer data is included or that all included proofs are accepted.\n\nNo preinstalled Lean project is the target of this research request. If formalizing\na new component, create a clean project and list its assumptions explicitly.\n')
    count = manifest(project)
    zip_path = BUILD / (name + '.zip')
    makezip(project.parent, zip_path)
    projects.append({'lane': lane, 'name': name, 'project_dir': str(project), 'manifest_entries': count,
                     'zip': str(zip_path), 'bytes': zip_path.stat().st_size, 'sha256': sha(zip_path.read_bytes())})
js(ROOT / 'checks/PROJECTS.json', projects)
print(json.dumps({'coverage': summary, 'overlay_manifest_entries': overlay_count,
                  'overlay_bytes': overlay_zip.stat().st_size, 'projects': projects}, indent=2))
