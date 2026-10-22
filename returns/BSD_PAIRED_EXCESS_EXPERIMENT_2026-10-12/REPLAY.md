# Replay

Run from this folder.

- `python3 checks/combined_exact.py`: exact point-map, local factors and5-saturation for d329233; rank upper bound retained from saved descent.
- `python3 checks/compare_digits.py`: independently recomputes corrected quotients from raw saved digits; distinguishes zero residues from exact valuations.
- `python input/BSD_ODD_EXCESS_RECHECK_2026-10-12/verify_exact.py`: replay Pro's supplied checker (requires SymPy1.14.0).
- PARI2.17.3: `gp -fq -s 4000M checks/partner_A.gp` recomputes the new partner coefficient and regulator, roughly10seconds observed.
- `gp -fq -s 128M checks/paired_heights.gp` checks the matrix and logarithm identities.
- `python3 checks/build_chunked.py` builds the partial-sum function from the separately bound official PARI source. Its source/runtime paths are recorded in the script; adjust paths on another machine. No system library is overwritten.
- `gp -fq -s 512M checks/chunk_control.gp` compares full moments with stock/saved cases. The install path points at this packet's local build directory; adjust on another machine.
- `gp -fq -s 512M checks/combined329233_n8.gp` recomputes the higher-precision combined control, with progress and recoverable partial moments. Runtime/cap recorded separately.

Saved discovery screens are optional and not proof inputs. All errors from the rejected whole-sum run are retained. A DONE marker, empty stderr and adequate precision are required, not just exit status0. No seed value is evaluated.
