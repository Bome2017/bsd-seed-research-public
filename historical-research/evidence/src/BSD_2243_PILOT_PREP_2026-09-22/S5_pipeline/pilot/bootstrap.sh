#!/bin/bash
# bootstrap.sh -- build the 2243 pilot toolchain on a fresh Ubuntu 24.04 machine (x86_64; aarch64 untested). Idempotent.
# Same library versions as the local reference build: FLINT 3.3.1 (downloaded from the upstream GitHub release; its
# sha256 is recorded), PARI 2.17.4 (bundled tarball, identical to the local source), GMP/MPFR from the distribution.
# Sources compile UNCHANGED: SHA-256 comes from the bundled compat/CommonCrypto shim (validated against Apple CommonCrypto).
set -euo pipefail
B=$(cd "$(dirname "$0")/.." && pwd); PFX=$B/local; mkdir -p $PFX $B/build $B/bin $B/logs
exec > >(tee -a $B/logs/bootstrap.log) 2>&1
echo "BOOTSTRAP start $(date -u +%FT%TZ)"; uname -a; lscpu | sed -n 1,25p; free -g; echo "nproc $(nproc)"
export DEBIAN_FRONTEND=noninteractive
sudo apt-get update -y -q && sudo apt-get install -y -q build-essential m4 libgmp-dev libmpfr-dev python3 time curl ca-certificates
NJ=$(nproc)
if [ ! -f $PFX/lib/libflint.so ]; then
  cd $B/build; curl -fsSL -o flint-3.3.1.tar.gz https://github.com/flintlib/flint/releases/download/v3.3.1/flint-3.3.1.tar.gz
  sha256sum flint-3.3.1.tar.gz | tee $B/logs/flint_tarball.sha256
  tar xzf flint-3.3.1.tar.gz; cd flint-3.3.1
  ./configure --prefix=$PFX --with-gmp=/usr --with-mpfr=/usr --disable-static > $B/logs/flint_configure.log 2>&1
  make -j$NJ > $B/logs/flint_make.log 2>&1; make install > $B/logs/flint_install.log 2>&1
fi
if [ ! -f $PFX/lib/libpari.so ]; then
  cd $B/build; sha256sum $B/third_party/pari-2.17.4.tar.gz | tee $B/logs/pari_tarball.sha256; tar xzf $B/third_party/pari-2.17.4.tar.gz; cd pari-2.17.4
  ./Configure --prefix=$PFX > $B/logs/pari_configure.log 2>&1; make -j$NJ gp > $B/logs/pari_make.log 2>&1; make install > $B/logs/pari_install.log 2>&1
fi
cd $B/src
cc -O2 -Wall -Wextra -Wno-deprecated-declarations -Icompat -o $B/bin/wverify wverify.c
cc -O3 -march=native -Wall -I$PFX/include apwit.c fastap.c -L$PFX/lib -Wl,-rpath,$PFX/lib -lpari -lm -o $B/bin/apwit_v
cc -O2 -march=native -Wall -Wextra -Wno-deprecated-declarations -Icompat -I$PFX/include acc2243v2.c -L$PFX/lib -Wl,-rpath,$PFX/lib -lflint -lmpfr -lgmp -lpthread -lm -o $B/bin/acc2243v2
( cd $B && sha256sum src/*.c src/compat/CommonCrypto/CommonDigest.h scripts/*.sh bin/* ) | tee $B/logs/build_hashes.txt
grep -E "__FLINT_VERSION|FLINT_VERSION \"" $PFX/include/flint/flint.h | tee -a $B/logs/build_hashes.txt; cc --version | head -1 | tee -a $B/logs/build_hashes.txt
echo "BOOTSTRAP_DONE $(date -u +%FT%TZ)"
