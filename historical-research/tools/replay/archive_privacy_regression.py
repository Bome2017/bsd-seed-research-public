#!/usr/bin/env python3
"""Regression for the actual nested-archive omission; uses dummy identifiers."""
import io
from pathlib import Path
import re
import sys
import tarfile
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from archive_privacy import contains_private_metadata, ArchiveInspectionError


def tar(name, data):
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode='w:gz') as t:
        m = tarfile.TarInfo(name)
        m.size = len(data)
        t.addfile(m, io.BytesIO(data))
    return buf.getvalue()


patterns = [re.compile(b'dummy-private-marker')]
bad = tar('inner.tar.gz', tar('record.md', b'dummy-private-marker'))
clean = tar('inner.tar.gz', tar('record.md', b'public arithmetic'))
if not contains_private_metadata('outer.tar.gz', bad, patterns):
    raise AssertionError('nested private value escaped inspection')
if contains_private_metadata('outer.tar.gz', clean, patterns):
    raise AssertionError('clean archive falsely rejected')
buf = io.BytesIO()
with zipfile.ZipFile(buf, 'w') as z:
    z.writestr('inner.tar.gz', bad)
if not contains_private_metadata('outer.zip', buf.getvalue(), patterns):
    raise AssertionError('mixed ZIP/TAR nesting escaped inspection')
for name, data, options in [
    ('broken.tar.gz', b'not an archive', {}),
    ('deep.tar.gz', clean, {'max_depth': 1}),
    ('large.tar.gz', clean, {'max_total_bytes': 1}),
]:
    try:
        contains_private_metadata(name, data, patterns, **options)
    except ArchiveInspectionError:
        pass
    else:
        raise AssertionError('inspection failure must not count as clean')
print('ALL PASS: nested TAR and ZIP detection; clean control; malformed/depth/size rejection')
