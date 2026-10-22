import RequestProject.GateRFinite.Finiteness
open Lean Elab Command Meta
partial def collect (env : Environment) (seen : Std.HashSet Name) (todo : List Name) : Std.HashSet Name :=
  match todo with
  | [] => seen
  | n :: rest =>
    if seen.contains n then collect env seen rest
    else match env.find? n with
      | none => collect env (seen.insert n) rest
      | some ci =>
        let cs := (ci.type.getUsedConstants ++ (ci.value?.map Expr.getUsedConstants).getD #[])
        collect env (seen.insert n) (cs.toList ++ rest)
run_cmd Command.liftTermElabM do
  let env ← getEnv
  let proj (n : Name) : Bool :=
    if let some idx := env.getModuleIdxFor? n then
      (env.header.moduleNames[idx.toNat]!).toString.startsWith "RequestProject" else false
  let all := collect env {} [`GateRFinite.h41_finite]
  let mine := (all.toList.filter (fun n => proj n && n != `GateRFinite.h41_finite && !n.isInternal)).map Name.toString
  let names := mine.toArray.qsort (· < ·)
  IO.println s!"PROJECT DEPENDENCIES OF GateRFinite.h41_finite: {names.size}"
  -- which of the five Gate-R outputs are actually consumed
  for k in ["GateR.height_sublevels","GateR.halving_representatives","GateR.bounded_halving",
            "GateR.every_point_torsion","GateR.h41_rank_zero","GateR.translateMax",
            "R1.h41_multiplicative_duplication_height","R0.properHeightTwoDescentTorsion",
            "P04c.card_twoE_quotient"] do
    let mark := if names.contains k then "USED    " else "NOT USED"
    IO.println s!"  {mark}  {k}"
