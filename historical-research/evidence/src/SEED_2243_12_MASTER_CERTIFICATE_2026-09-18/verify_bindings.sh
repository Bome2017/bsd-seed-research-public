#!/bin/sh
# Recompute the sha256 of every upstream record bound at freeze time (paths relative to $HOME).
cd "$HOME" || exit 2
shasum -a 256 -c "$HOME/SEED_2243_12_MASTER_CERTIFICATE_2026-09-18/BINDINGS.sha256"
