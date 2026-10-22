import RequestProject.GateR.Assembly
open Lean Elab Command Meta

/- Transitive dependency footprint of a declaration, over value? and type,
   restricted to this project's own modules. -/
partial def collect (env : Environment) (seen : Std.HashSet Name) (todo : List Name) :
    Std.HashSet Name :=
  match todo with
  | [] => seen
  | n :: rest =>
    if seen.contains n then collect env seen rest
    else
      match env.find? n with
      | none => collect env (seen.insert n) rest
      | some ci =>
        let cs := (ci.type.getUsedConstants ++ (ci.value?.map Expr.getUsedConstants).getD #[])
        collect env (seen.insert n) (cs.toList ++ rest)

run_cmd Command.liftTermElabM do
  let env ← getEnv
  let proj (n : Name) : Bool :=
    if let some idx := env.getModuleIdxFor? n then
      (env.header.moduleNames[idx.toNat]!).toString.startsWith "RequestProject"
    else false
  for tgt in [`GateR.height_sublevels, `GateR.halving_representatives, `GateR.bounded_halving,
              `GateR.every_point_torsion, `GateR.h41_rank_zero] do
    let all := collect env {} [tgt]
    let mine := all.toList.filter (fun n => proj n && n != tgt && !n.isInternal)
    let names := (mine.map Name.toString).toArray.qsort (· < ·)
    IO.println s!"### {tgt}  — {names.size} project dependencies"
    for n in names do IO.println s!"    {n}"
    IO.println ""
