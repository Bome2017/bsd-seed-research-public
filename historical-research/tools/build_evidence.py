#!/usr/bin/env python3
"""Assemble evidence/src/ from the research tree, read-only on every source.

Inputs (all read-only):
  * every source bound by the canonical master record (SOURCE_BINDINGS.json);
  * the master folder's own top-level record files;
  * the post-master folders listed in POST_MASTER (records created or changed after the master's last integration);
  * extra files named in tools/extra_evidence.txt (one absolute path per line; '#' comments).

Each included file is copied byte-for-byte to evidence/src/<path relative to RESEARCH_HOME>, re-hashed after the copy, and listed
in evidence/PROVENANCE.tsv. Every excluded file is listed in evidence/EXCLUDED.tsv with its reason. Nothing outside the
release folder is written.
"""
import hashlib, json, os, re, shutil, sys, tarfile
from pathlib import Path
from archive_privacy import contains_private_metadata, ArchiveInspectionError

RESEARCH_HOME = Path('/Users/bsm')
REL = Path(__file__).resolve().parent.parent
MASTER = RESEARCH_HOME / 'BSD_CODEX6_MASTER_HANDOFF_2026-09-19'
OUT = REL / 'evidence' / 'src'
POST_MASTER = [
    'BSD_SEED_P13_RUN_2026-09-21', 'BSD_DEFINITE_FIELD_GATE_2026-09-22', 'BSD_TWIST_D7_CERTIFICATE_2026-09-22',
    'BSD_TWIST_SHA_SUPPORT_2026-09-22', 'BSD_TWIST_SHA_SUPPORT_BLIND_2026-09-22', 'BSD_C2_WITNESS_2026-09-22',
    'BSD_FRONTIER_FREEZE_2026-09-22', 'BSD_SUPERSINGULAR_SIGNED_BRIDGE_2026-09-22',
    'BSD_SUPERSINGULAR_SIGNED_BRIDGE_REVIEW_2026-09-22', 'BSD_A3_LEAN_CORE_2026-09-22',
    'BSD_ARISTOTLE_ORDINARY_BRIDGE_2026-09-22', 'BSD_ARISTOTLE_TAIL_COMPRESSION_2026-09-22',
    'BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22', 'BSD_2243_PILOT_PREP_2026-09-22', 'BSD_2243_ACC_CODEX_CHECK_2026-09-23',
    'BSD_2243_EVALUATOR_REVIEW_2026-09-23', 'BSD_2243_COMPRESSION_ATTEMPT_2026-09-23', 'BSD_2243_D5_INDEPENDENT_2026-09-23',
]
PRIVATE = ['BSD_OUTREACH_ASSESSMENT_2026-09-22']            # correspondence with named third parties: never copied
MAX_BYTES = 10 * 1024 * 1024
# Private e-mail thread identifiers (correspondence metadata with no evidentiary value) are masked in released copies.
# Rebuilding the evidence is a local archival operation, not needed for verification.
# Supply a private JSON list of literal identifiers outside this repository.
_private_file = os.environ.get('BSD_PRIVATE_REDACTION_FILE')
if not _private_file:
    raise SystemExit('Evidence rebuild requires BSD_PRIVATE_REDACTION_FILE (external JSON list). Use verify_release.py to verify the existing snapshot.')
_private_ids = json.loads(Path(_private_file).read_text())
if not isinstance(_private_ids, list) or not _private_ids or not all(isinstance(x, str) and x for x in _private_ids):
    raise SystemExit('Private redaction configuration must be a nonempty JSON list of nonempty strings.')
REDACT = [(re.compile(re.escape(x.encode())), b'[private-thread-id-redacted]') for x in _private_ids]

MACHO = {b'\xcf\xfa\xed\xfe', b'\xce\xfa\xed\xfe', b'\xca\xfe\xba\xbe', b'\x7fELF'}
JUNK = {'.DS_Store'}


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


_PDF_DIRS = {}


def dir_has_pdf(d: Path):
    if d not in _PDF_DIRS:
        _PDF_DIRS[d] = any(q.suffix.lower() == '.pdf' for q in d.iterdir())
    return _PDF_DIRS[d]


def exclusion(p: Path):
    """Return a reason string if the file must not be copied, else None."""
    s = str(p)
    if '/BSD_SEED_P13_RUN_2026-09-21/run/' in s and not (p.parent.name == 'run' and p.suffix == '.txt'):
        return 'bulk computation work units and logs of the C13 run (see data/LARGE_DATA.md; audited by the master completion review)'
    if p.name in JUNK or '__pycache__' in p.parts or '.lake' in p.parts or '.git' in p.parts:
        return 'build/OS artifact'
    if p.name.startswith('system_snapshot'):
        return 'host telemetry (process/app listing; private and irrelevant to the mathematics)'
    if any(f'/{d}/' in s for d in PRIVATE):
        return 'private correspondence with named third parties (not redistributed)'
    if p.suffix.lower() == '.pdf':
        return 'third-party publication (copyright; cited, local sha256 recorded)'
    if p.suffix.lower() == '.txt' and (re.search(r'/(sources|[a-z]+_sources)/', s)
                                       or re.match(r'(SteinWuthrich|source_macias_castillo)', p.name)
                                       or dir_has_pdf(p.parent)):
        return 'third-party publication text extraction (copyright; cited, local sha256 recorded)'
    if re.fullmatch(r'ap_\d+\.(bin|tmp)', p.name) or p.name.endswith('.bin') and p.stat().st_size > 1024 * 1024:
        return 'bulk coefficient/binary data (see data/LARGE_DATA.md)'
    try:
        with open(p, 'rb') as f:
            if f.read(4) in MACHO:
                return 'compiled executable (sources included instead)'
    except OSError:
        return 'unreadable'
    if p.stat().st_size > MAX_BYTES:
        return f'larger than {MAX_BYTES} bytes (see data/LARGE_DATA.md)'
    if p.name.endswith(('.tar.gz', '.tgz', '.tar', '.zip')):
        try:
            if contains_private_metadata(p.name, p.read_bytes(), [rx for rx, _ in REDACT]):
                return 'archive embeds private correspondence metadata, including nested archives (retain needed unpacked records with redaction)'
        except (ArchiveInspectionError, OSError):
            return 'archive not safely inspectable within privacy bounds; excluded pending explicit review'
    return None


def main():
    bindings = json.loads((MASTER / 'SOURCE_BINDINGS.json').read_text())
    bound = {s['path']: s for s in bindings['sources']}
    cands = {}                                             # path -> category
    for p in bound:
        cands[p] = 'master_bound'
    for p in sorted(MASTER.iterdir()):
        if p.is_file():
            cands.setdefault(str(p), 'master_record')
    for d in POST_MASTER:
        for root, dirs, files in os.walk(RESEARCH_HOME / d):
            dirs[:] = [x for x in dirs if x not in ('.lake', '.git', '__pycache__')]
            for f in files:
                cands.setdefault(str(Path(root) / f), 'post_master')
    extra = REL / 'tools' / 'extra_evidence.txt'
    if extra.exists():
        for line in extra.read_text().splitlines():
            line = line.split('#', 1)[0].strip()
            if line:
                pp = Path(line)
                if pp.is_dir():
                    for root, dirs, files in os.walk(pp):
                        dirs[:] = [x for x in dirs if x not in ('.lake', '.git', '__pycache__')]
                        for f in files:
                            cands.setdefault(str(Path(root) / f), 'extra')
                else:
                    cands.setdefault(line, 'extra')
    prov, excl, redactions = [], [], []
    for s, cat in sorted(cands.items()):
        p = Path(s)
        if not p.is_file():
            excl.append((s, '', 'missing on disk', cat))
            continue
        why = exclusion(p)
        if why:
            excl.append((s, str(p.stat().st_size), why, cat))
            continue
        rel = p.relative_to(RESEARCH_HOME)
        dst = OUT / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        before = sha(p)
        raw = p.read_bytes()
        red = raw
        for rx, rep in REDACT:
            red = rx.sub(rep, red)
        if red != raw:
            dst.write_bytes(red)
            shutil.copystat(p, dst)
            redactions.append((str(rel), before, sha(dst)))
        elif not dst.exists() or sha(dst) != before:
            shutil.copy2(p, dst)
        after = sha(dst)
        if after != before and red == raw:
            sys.exit(f'copy mismatch: {p}')
        b = bound.get(s)
        prov.append((str(rel), s, after, str(p.stat().st_size), cat, b['sha256'] if b else '',
                     ('match' if b and b['sha256'] == before else ('CHANGED_SINCE_MASTER_BINDING' if b else '')),
                     (b.get('role', '') if b else '').replace('\t', ' ')[:160], before))
    with open(REL / 'evidence' / 'PROVENANCE.tsv', 'w') as f:
        f.write('release_path\toriginal_path\tsha256\tbytes\tcategory\tmaster_bound_sha256\tbinding_check\tmaster_role\toriginal_sha256\n')
        for r in prov:
            f.write('evidence/src/' + '\t'.join(r) + '\n')
    with open(REL / 'evidence' / 'EXCLUDED.tsv', 'w') as f:
        f.write('original_path\tbytes\treason\tcategory\tsha256_of_original\n')
        for s, sz, why, cat in excl:
            h = sha(s) if Path(s).is_file() and why != 'build/OS artifact' else ''
            f.write(f'{s}\t{sz}\t{why}\t{cat}\t{h}\n')
    with open(REL / 'evidence' / 'REDACTIONS.tsv', 'w') as f:
        f.write('release_path\toriginal_sha256\treleased_sha256\tredaction\n')
        for rel_, a, b_ in redactions:
            f.write(f'evidence/src/{rel_}\t{a}\t{b_}\tprivate e-mail thread identifier masked\n')
    tot = sum(int(r[3]) for r in prov)
    print(f'included {len(prov)} files, {tot} bytes; excluded {len(excl)}; '
          f'changed-since-binding {sum(1 for r in prov if r[6] == "CHANGED_SINCE_MASTER_BINDING")}; redacted {len(redactions)}')


if __name__ == '__main__':
    main()
