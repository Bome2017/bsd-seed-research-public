#!/bin/bash
# Rebuild all binaries of the rigorous stream core (exact commands used on 2026-09-19; toolchain in TOOLCHAIN.txt).
set -euo pipefail
R=$(cd "$(dirname "$0")" && pwd)
P=${P:-$HOME/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4}          # PARI 2.17.4 (producer only)
SE=${SE:-$HOME/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env}              # FLINT 3.3.1 (Arb), GMP, MPFR
# 1. independent verifier: integer arithmetic only, no external library beyond CommonCrypto (SHA-256)
cc -O2 -Wall -Wextra -Wno-deprecated-declarations -o $R/verifier/wverify $R/verifier/wverify.c
# 2. witness producer (untrusted): PARI + fastap.c (byte-identical copy of the LP5 fastap.c)
(cd $R/src && cc -O3 -march=native -Wall -Iinc -I$P/src/headers -I$P/Odarwin-x86_64 apwit.c fastap.c -L$P/Odarwin-x86_64 -lpari -lm -o apwit)
# 3. rigorous engine: FLINT/Arb ball arithmetic
cc -O2 -march=native -Wall -Wextra -Wno-deprecated-declarations -I$SE/include $R/src/arbcore.c -L$SE/lib -Wl,-rpath,$SE/lib -lflint -lmpfr -lgmp -lpthread -o $R/src/arbcore
shasum -a 256 $R/verifier/wverify.c $R/src/apwit.c $R/src/fastap.c $R/src/arbcore.c $R/verifier/wverify $R/src/apwit $R/src/arbcore
echo "run apwit with DYLD_LIBRARY_PATH=$P/Odarwin-x86_64"
