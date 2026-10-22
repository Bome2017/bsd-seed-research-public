/-
Verification harness for the single authorised output of this job.
Not part of the `RequestProject` library (the library glob is `RequestProject.+`);
run it with `lake env lean verify/Verify.lean`.
-/
import RequestProject.GateRFinite.Finiteness

set_option pp.explicit true
set_option pp.universes true
set_option pp.fullNames true

#check @GateRFinite.h41_finite

#print axioms GateRFinite.h41_finite

open Lean in
/-- Project-declared constants occurring in the transitive proof-term closure of
`GateRFinite.h41_finite`; compiler-generated auxiliaries are filtered out. -/
def projectDeps : Lean.Elab.Command.CommandElabM Unit := do
  let env ← Lean.getEnv
  let pref := ["GateR", "GateRFinite", "R0", "R1", "P01", "P03a", "P03b", "P03c", "P03d",
    "P03e", "P04a", "P04b", "P04c", "SDyadic", "Run013", "Descent"]
  let isAux (s : String) : Bool :=
    ["_proof_", "_simp_", "_aux", "match_", "_eq_", "_unsafe", "_cstage",
      "proof_", "_sunfold", "_mutual", "_closed"].any (fun t => (s.splitOn t).length != 1)
  let mut seen : Lean.NameSet := {}
  let mut todo : List Lean.Name := [`GateRFinite.h41_finite]
  let mut hits : Array String := #[]
  let mut direct : Array String := #[]
  while !todo.isEmpty do
    let n :: rest := todo | break
    todo := rest
    if seen.contains n then continue
    seen := seen.insert n
    let s := n.toString
    if pref.any (fun p => s.startsWith (p ++ ".")) && !isAux s then
      hits := hits.push s
    match env.find? n with
    | some ci =>
      let mut cs : Lean.NameSet := {}
      cs := ci.type.getUsedConstants.foldl (·.insert ·) cs
      if let some v := ci.value? then
        cs := v.getUsedConstants.foldl (·.insert ·) cs
      if n == `GateRFinite.h41_finite then
        direct := cs.toList.map (·.toString) |>.toArray
      todo := cs.toList ++ todo
    | none => pure ()
  Lean.logInfo m!"IMMEDIATE constants of the proof term of h41_finite:\n{direct.qsort (· < ·)}"
  Lean.logInfo m!"PROJECT declarations in the transitive closure ({hits.size}):\n{hits.qsort (· < ·)}"

run_cmd projectDeps
