# Changed relation producer

The unmodified smaller-factor-base run completed factor-base construction using
732,577,792 peak resident bytes, but did not progress beyond its initial eleven
relation columns during the 117-second alarm window. It retained a deficit of
721 relations while repeatedly executing `small_norm`.

This gate changes the documented relation producer, not the memory ceiling:
`bnfinit(NF,1,[0.02,0,-1])`. The retained official PARI documentation explicitly
says that `nrpid=-1` disables small-norm searching. In pinned PARI 2.17.3
`buch2.original.c`, the small-norm branch at line 3903 requires `Nrelid > 0`,
and the subsequent positive-need branch invokes `rnd_rel`.

Version detail: the installed 2.17.3 general number-field documentation
describes zero as disabling this search, whereas the older retained HTML
describes minus one. The pinned 2.17.3 GP entry point `bnfinit0` passes the
third integer unchanged to `Buchall_param`, whose branch requires it to
be strictly positive. Thus minus one has the stated effect in the actual
runtime; the direct log confirms entry into `rnd_rel`. No undocumented
interpretation of a negative parameter is needed.

The full completeness factor base is unchanged. The calculation remains
conditional on GRH until separately certified by `bnfcertify`; an unfinished
run does not even establish a conditional class group.

The wall gate is 180 seconds, with an internal alarm at 177 seconds and a
2GB PARI stack. Output is written directly to files throughout execution.
The external timeout kills the full new process group. A completed BNF is
saved before any further arithmetic. No class or unit result is accepted
without the explicit completion marker.
