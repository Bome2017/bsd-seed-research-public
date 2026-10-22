# Replay

Use the parent INPUT_BINDINGS.json to verify frozen inputs. Run gate.gp with the pinned original GP binary in an isolated copy of this directory, keeping sibling inputs/ paths intact. GP write appends, so remove generated outputs only in the isolated replay copy before running. The maximum budget is60 seconds and1GB.

Expected completion is [331,20,120,60,60,[3,5,6],[20,20,20],[0,0,0]]. A missing marker, timeout, or partial output is not a full-rank certificate. The original run used no new factorization or BNF. Matrix-only checks can read GATE_CORE.json according to CORE_SCHEMA.json without repeating number-field transport.
