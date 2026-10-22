#!/usr/bin/env python3
"""Metadata-preserving evidence transition (v0.2.3). Read-only on every source; writes only evidence/ and one log.

Why this exists. `tools/build_evidence.py` regenerates PROVENANCE/EXCLUDED/REDACTIONS from scratch. Its generic output
does not reproduce metadata added by earlier reviews (the `review_restored` and `post-master source audit` rows, binding
descriptions, source roles, reviewed exclusion reasons). A plain rebuild therefore rewrites reviewed rows even when no
evidence changed. This tool keeps those rows and adds only declared evidence.

  1. Dry-run the UNMODIFIED builder, with the same private configuration, into a temporary directory. This re-derives,
     for every candidate, today's content hashes and privacy disposition (admitted / masked / excluded).
  2. For each baseline row (the pinned tables under --baseline), require: the same file; the same released bytes and
     hash; a consistent original hash (an empty baseline field may now be filled, but a different value is a source
     change); and the same disposition. Then emit the baseline row BYTE FOR BYTE, in baseline order.
  3. Append exactly the declared additions (--declared), as the builder generated them: same hashes, admitted
     unmasked.
  4. Reject anything else: a removal, an undeclared addition, a duplicate, a content change, a disposition change.
  5. Install only the declared new files into evidence/src/ (from the dry run, hash-checked), then verify the whole
     released tree against the final PROVENANCE.tsv.

Usage (never prints the private values):
  BSD_PRIVATE_REDACTION_FILE=<external JSON list> python3 tools/build_evidence_transition.py \
      --baseline review/history/v0.2.2/evidence --declared review/A4_EVIDENCE_ADDITIONS.json \
      --log review/A4_EVIDENCE_TRANSITION.json
  python3 tools/build_evidence_transition.py --self-test      # rejection rules on synthetic tables; no I/O
"""
import argparse, hashlib, json, shutil, sys, tempfile
from pathlib import Path

REL = Path(__file__).resolve().parent.parent
TABLES = {'PROVENANCE.tsv': 'release_path', 'EXCLUDED.tsv': 'original_path', 'REDACTIONS.tsv': 'release_path'}


class TransitionError(Exception):
    pass


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def parse(text, name):
    """Split a table into (header line, [row lines], {key: field dict}), keeping every line's exact text."""
    if not text.endswith('\n'):
        raise TransitionError(f'{name}: no trailing newline')
    lines = text[:-1].split('\n')
    header, rows = lines[0], lines[1:]
    cols = header.split('\t')
    key = TABLES[name]
    index = {}
    for line in rows:
        f = line.split('\t')
        if len(f) != len(cols):
            raise TransitionError(f'{name}: malformed row ({len(f)} fields)')
        d = dict(zip(cols, f))
        if d[key] in index:
            raise TransitionError(f'{name}: duplicate key {d[key]}')
        index[d[key]] = d
    return header, rows, index


def merge(base, gen, declared):
    """Pure merge. base/gen map table name -> text. declared = the additions document. Returns (tables, report)."""
    B = {n: parse(base[n], n) for n in TABLES}
    G = {n: parse(gen[n], n) for n in TABLES}
    for n in TABLES:
        if B[n][0] != G[n][0]:
            raise TransitionError(f'{n}: header changed')
    adds = {a['release_path']: a for a in declared['additions']}
    if len(adds) != len(declared['additions']):
        raise TransitionError('declared additions contain a duplicate')
    if declared.get('declared_exclusions') or declared.get('declared_redactions'):
        raise TransitionError('this transition declares no exclusions or redactions')
    bprov, gprov = B['PROVENANCE.tsv'][2], G['PROVENANCE.tsv'][2]
    bred, gred = B['REDACTIONS.tsv'][2], G['REDACTIONS.tsv'][2]
    bexc, gexc = B['EXCLUDED.tsv'][2], G['EXCLUDED.tsv'][2]
    report = {'retained_metadata_differences': {n: [] for n in TABLES}}

    def note(name, key, b, g):
        diff = {c: {'retained': b[c], 'generic_builder': g[c]} for c in b if b[c] != g[c]}
        if diff:
            report['retained_metadata_differences'][name].append({'key': key, 'fields': diff})

    # PROVENANCE: every baseline row must be the same evidence, with the same disposition
    for k, b in bprov.items():
        g = gprov.get(k)
        if g is None:
            raise TransitionError(f'PROVENANCE: baseline row no longer produced (removal or disposition change): {k}')
        if g['original_path'] != b['original_path']:
            raise TransitionError(f'PROVENANCE: original path changed: {k}')
        if (g['sha256'], g['bytes']) != (b['sha256'], b['bytes']):
            raise TransitionError(f'PROVENANCE: released content changed: {k}')
        if b['original_sha256'] and g['original_sha256'] != b['original_sha256']:
            raise TransitionError(f'PROVENANCE: source content changed: {k}')
        if (k in bred) != (k in gred):
            raise TransitionError(f'PROVENANCE: masking disposition changed: {k}')
        note('PROVENANCE.tsv', k, b, g)
    new = [k for k in gprov if k not in bprov]
    undeclared = sorted(set(new) - set(adds))
    if undeclared:
        raise TransitionError(f'PROVENANCE: undeclared addition(s): {undeclared[:3]}')
    missing = sorted(set(adds) - set(new))
    if missing:
        raise TransitionError(f'PROVENANCE: declared addition(s) not produced: {missing[:3]}')
    for k in new:
        g, a = gprov[k], adds[k]
        if k in gred:
            raise TransitionError(f'PROVENANCE: declared addition was masked: {k}')
        if (g['sha256'], g['original_sha256'], g['bytes'], g['original_path']) != (a['sha256'], a['sha256'], str(a['bytes']), a['original_path']):
            raise TransitionError(f'PROVENANCE: declared addition differs from its declaration: {k}')
    # EXCLUDED: every baseline exclusion must still be excluded, same file; no new exclusions
    for k, b in bexc.items():
        g = gexc.get(k)
        if g is None:
            raise TransitionError(f'EXCLUDED: baseline exclusion no longer excluded (disposition change or removal): {k}')
        if g['bytes'] != b['bytes'] or (b['sha256_of_original'] and g['sha256_of_original'] != b['sha256_of_original']):
            raise TransitionError(f'EXCLUDED: excluded source changed: {k}')
        note('EXCLUDED.tsv', k, b, g)
    extra_exc = sorted(set(gexc) - set(bexc))
    if extra_exc:
        raise TransitionError(f'EXCLUDED: undeclared new exclusion(s): {extra_exc[:3]}')
    # REDACTIONS: identical masked outputs; no new masking
    for k, b in bred.items():
        g = gred.get(k)
        if g is None or (g['original_sha256'], g['released_sha256']) != (b['original_sha256'], b['released_sha256']):
            raise TransitionError(f'REDACTIONS: masking outcome changed: {k}')
        note('REDACTIONS.tsv', k, b, g)
    if set(gred) - set(bred):
        raise TransitionError('REDACTIONS: undeclared new masking')
    # emit: baseline lines verbatim, in baseline order; declared additions appended in builder order
    gen_lines = {parse_key(line, 'PROVENANCE.tsv', G): line for line in G['PROVENANCE.tsv'][1]}
    out = {}
    out['PROVENANCE.tsv'] = '\n'.join([B['PROVENANCE.tsv'][0]] + B['PROVENANCE.tsv'][1] + [gen_lines[k] for k in new]) + '\n'
    out['EXCLUDED.tsv'] = base['EXCLUDED.tsv']
    out['REDACTIONS.tsv'] = base['REDACTIONS.tsv']
    report['counts'] = {
        'PROVENANCE.tsv': {'baseline_rows': len(bprov), 'preserved_verbatim': len(bprov), 'appended': len(new)},
        'EXCLUDED.tsv': {'baseline_rows': len(bexc), 'preserved_verbatim': len(bexc), 'appended': 0},
        'REDACTIONS.tsv': {'baseline_rows': len(bred), 'preserved_verbatim': len(bred), 'appended': 0}}
    report['appended'] = new
    return out, report


def parse_key(line, name, parsed):
    cols = parsed[name][0].split('\t')
    return dict(zip(cols, line.split('\t')))[TABLES[name]]


def dry_run_builder(extra_evidence_text):
    """Run the unmodified builder with its outputs redirected to a temporary directory."""
    sys.path.insert(0, str(REL / 'tools'))
    import build_evidence as be                      # reads BSD_PRIVATE_REDACTION_FILE; never printed here
    tmp = Path(tempfile.mkdtemp(prefix='evidence_dry_run_'))
    (tmp / 'tools').mkdir(); (tmp / 'evidence' / 'src').mkdir(parents=True)
    (tmp / 'tools' / 'extra_evidence.txt').write_text(extra_evidence_text)
    be.REL, be.OUT = tmp, tmp / 'evidence' / 'src'
    be.main()
    gen = {n: (tmp / 'evidence' / n).read_text() for n in TABLES}
    return tmp, gen, sha_file(REL / 'tools' / 'build_evidence.py')


def run(args):
    baseline = REL / args.baseline
    declared_path = REL / args.declared
    declared = json.loads(declared_path.read_text())
    base = {n: (baseline / n).read_text() for n in TABLES}
    tmp, gen, builder_sha = dry_run_builder((REL / 'tools' / 'extra_evidence.txt').read_text())
    try:
        out, report = merge(base, gen, declared)
        # install exactly the declared new files, from the dry run, hash-checked
        for a in declared['additions']:
            rel = a['release_path'][len('evidence/src/'):]
            src, dst = tmp / 'evidence' / 'src' / rel, REL / a['release_path']
            if sha_file(src) != a['sha256']:
                raise TransitionError(f'dry-run copy differs from declaration: {rel}')
            if dst.exists() and sha_file(dst) != a['sha256']:
                raise TransitionError(f'existing release file differs from declaration: {rel}')
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        # the whole released tree must equal the final PROVENANCE.tsv, file for file
        hdr, rows, prov = parse(out['PROVENANCE.tsv'], 'PROVENANCE.tsv')
        tree = {str(p.relative_to(REL)) for p in (REL / 'evidence' / 'src').rglob('*') if p.is_file()}
        if tree != set(prov):
            raise TransitionError(f'released tree differs from PROVENANCE: +{sorted(tree - set(prov))[:3]} -{sorted(set(prov) - tree)[:3]}')
        bad = [k for k, r in prov.items() if sha_file(REL / k) != r['sha256']]
        if bad:
            raise TransitionError(f'released file hash differs from PROVENANCE: {bad[:3]}')
        for n, text in out.items():
            (REL / 'evidence' / n).write_text(text)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    log = {'tool': {'path': 'tools/build_evidence_transition.py', 'sha256': sha_file(Path(__file__))},
           'builder_unmodified': {'path': 'tools/build_evidence.py', 'sha256': builder_sha},
           'baseline_tables': {n: {'path': f'{args.baseline}/{n}', 'sha256': sha_bytes(base[n].encode())} for n in TABLES},
           'generic_dry_run_tables_sha256': {n: sha_bytes(gen[n].encode()) for n in TABLES},
           'declared': {'path': args.declared, 'sha256': sha_file(declared_path)},
           'result_tables': {n: sha_bytes(out[n].encode()) for n in TABLES},
           'counts': report['counts'], 'appended': report['appended'],
           'retained_metadata_differences_count': {n: len(v) for n, v in report['retained_metadata_differences'].items()},
           'retained_metadata_differences': report['retained_metadata_differences'],
           'note': 'Each difference is a baseline (reviewed) value retained where the current generic builder would write another; '
                   'content hashes and dispositions were proved equal before retention.'}
    (REL / args.log).write_text(json.dumps(log, indent=1) + '\n')
    c = report['counts']
    print(f"TRANSITION_PASS: provenance {c['PROVENANCE.tsv']['preserved_verbatim']} preserved + {c['PROVENANCE.tsv']['appended']} appended; "
          f"exclusions {c['EXCLUDED.tsv']['preserved_verbatim']} preserved; redactions {c['REDACTIONS.tsv']['preserved_verbatim']} preserved; "
          f"retained reviewed differences {log['retained_metadata_differences_count']}")


def self_test():
    H = {'PROVENANCE.tsv': 'release_path\toriginal_path\tsha256\tbytes\tcategory\tmaster_bound_sha256\tbinding_check\tmaster_role\toriginal_sha256',
         'EXCLUDED.tsv': 'original_path\tbytes\treason\tcategory\tsha256_of_original',
         'REDACTIONS.tsv': 'release_path\toriginal_sha256\treleased_sha256\tredaction'}
    t = lambda n, rows: '\n'.join([H[n]] + rows) + '\n'
    base = {'PROVENANCE.tsv': t('PROVENANCE.tsv', ['evidence/src/a\t/h/a\tAA\t1\treview_restored\tAA\tMATCH\trole\t',
                                                    'evidence/src/m\t/h/m\tMM\t2\tpost_master\t\t\t\tOM']),
            'EXCLUDED.tsv': t('EXCLUDED.tsv', ['/h/x\t5\treviewed reason\tprivate archive\tXX']),
            'REDACTIONS.tsv': t('REDACTIONS.tsv', ['evidence/src/m\tOM\tMM\tprivate e-mail thread identifier masked'])}
    good = {'PROVENANCE.tsv': t('PROVENANCE.tsv', ['evidence/src/a\t/h/a\tAA\t1\textra\t\t\t\tAA',
                                                    'evidence/src/m\t/h/m\tMM\t2\tpost_master\t\t\t\tOM',
                                                    'evidence/src/n\t/h/n\tNN\t3\textra\t\t\t\tNN']),
            'EXCLUDED.tsv': t('EXCLUDED.tsv', ['/h/x\t5\tgeneric reason\tpost_master\tXX']),
            'REDACTIONS.tsv': base['REDACTIONS.tsv']}
    decl = {'additions': [{'release_path': 'evidence/src/n', 'original_path': '/h/n', 'sha256': 'NN', 'bytes': 3}]}
    out, rep = merge(base, good, decl)
    assert out['PROVENANCE.tsv'] == base['PROVENANCE.tsv'] + 'evidence/src/n\t/h/n\tNN\t3\textra\t\t\t\tNN\n'
    assert out['EXCLUDED.tsv'] == base['EXCLUDED.tsv'] and len(rep['retained_metadata_differences']['EXCLUDED.tsv']) == 1
    def mut(name, old, new):
        g = dict(good); assert old in g[name]; g[name] = g[name].replace(old, new); return g
    cases = {
        'removal': (mut('PROVENANCE.tsv', 'evidence/src/a\t/h/a\tAA\t1\textra\t\t\t\tAA\n', ''), decl),
        'released_content_change': (mut('PROVENANCE.tsv', 'evidence/src/a\t/h/a\tAA', 'evidence/src/a\t/h/a\tAB'), decl),
        'source_content_change': (mut('PROVENANCE.tsv', '\t2\tpost_master\t\t\t\tOM', '\t2\tpost_master\t\t\t\tOX'), decl),
        'masking_disposition_change': (mut('REDACTIONS.tsv', 'evidence/src/m\tOM\tMM\tprivate e-mail thread identifier masked\n', ''), decl),
        'undeclared_addition': (mut('PROVENANCE.tsv', 'evidence/src/n\t/h/n\tNN\t3\textra\t\t\t\tNN\n',
                                    'evidence/src/n\t/h/n\tNN\t3\textra\t\t\t\tNN\nevidence/src/z\t/h/z\tZZ\t9\textra\t\t\t\tZZ\n'), decl),
        'declared_hash_mismatch': (good, {'additions': [{'release_path': 'evidence/src/n', 'original_path': '/h/n', 'sha256': 'NX', 'bytes': 3}]}),
        'declared_not_produced': (mut('PROVENANCE.tsv', 'evidence/src/n\t/h/n\tNN\t3\textra\t\t\t\tNN\n', ''), decl),
        'duplicate_row': (mut('PROVENANCE.tsv', 'evidence/src/n\t/h/n\tNN\t3\textra\t\t\t\tNN\n',
                              'evidence/src/n\t/h/n\tNN\t3\textra\t\t\t\tNN\nevidence/src/n\t/h/n\tNN\t3\textra\t\t\t\tNN\n'), decl),
        'exclusion_now_admitted': (mut('EXCLUDED.tsv', '/h/x\t5\tgeneric reason\tpost_master\tXX\n', ''), decl),
        'excluded_source_change': (mut('EXCLUDED.tsv', '\tpost_master\tXX', '\tpost_master\tXY'), decl),
        'new_exclusion': (mut('EXCLUDED.tsv', '/h/x\t5\tgeneric reason\tpost_master\tXX\n', '/h/x\t5\tgeneric reason\tpost_master\tXX\n/h/y\t1\tr\tc\tYY\n'), decl),
        'header_change': (mut('PROVENANCE.tsv', 'master_role', 'role'), decl),
    }
    results = {}
    for name, (g, d) in cases.items():
        try:
            merge(base, g, d); results[name] = 'ACCEPTED (defect)'
        except TransitionError:
            results[name] = 'rejected'
    for k, v in results.items():
        print(f'{k:28s} {v}')
    ok = all(v == 'rejected' for v in results.values())
    print('SELF_TEST_PASS: positive case accepted; every negative case rejected' if ok else 'SELF_TEST_FAIL')
    return ok


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--self-test', action='store_true')
    ap.add_argument('--baseline'); ap.add_argument('--declared'); ap.add_argument('--log')
    a = ap.parse_args()
    if a.self_test:
        raise SystemExit(0 if self_test() else 1)
    if not (a.baseline and a.declared and a.log):
        raise SystemExit('need --baseline, --declared and --log (or --self-test)')
    try:
        run(a)
    except TransitionError as e:
        raise SystemExit(f'TRANSITION_FAIL: {e}')
