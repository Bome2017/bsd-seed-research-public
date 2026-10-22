# Evidence policy

`SOURCE_BINDINGS.tsv` binds inherited inputs by absolute path and SHA-256.
The old scout directory remains immutable input; this project does not
rewrite it.

New computations must record program bytes, input bytes, tool version, seed
where applicable, stdout/stderr, exit status, and a statement of what the
computation establishes.  Sample-prime output is corroboration only unless a
separate symbolic lemma proves uniformity.

