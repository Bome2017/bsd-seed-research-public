# Run013 successor active-manifest policy

`MANIFEST.sha256` is the sole active project manifest for this packaging-only
successor.

Its convention is:

- enumerate every shipped regular file recursively except `MANIFEST.sha256`
  itself;
- use paths relative to the successor project root, without a leading `./`;
- sort paths bytewise with `LC_ALL=C`;
- write one lowercase SHA-256 digest, two ASCII spaces, and one relative path per
  line;
- prohibit duplicate paths, absent paths, unmanifested regular files, symbolic
  links, hard-link archive aliases, and special files.

The active manifest intentionally does not ship the stale
`PROJECT_MANIFEST.sha256` from the original Aristotle artifact. Its exact digest
and replay failure are preserved in `RUN013_FORMALIZATION_PROVENANCE.md` and
`RUN013_SOURCE_PRESERVATION_BASELINE.md`.

The successor intentionally omits `.gitignore`; no historical bytes were
invented. It also excludes `.lake`, compiled `.olean` files, build caches,
`.DS_Store`, and `__MACOSX`.

Strict content replay is performed from the project root with:

```sh
shasum -a 256 -c MANIFEST.sha256
```

A separate file-set comparison verifies that the manifest paths equal the set
of shipped regular files other than `MANIFEST.sha256`.
