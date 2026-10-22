import RequestProject.GateR.Assembly
open Lean Elab Command Meta

-- Print every theorem of this project with its FULL elaborated type, grouped by
-- source module, and separate source-declared from compiler-generated.  The type
-- always comes from the environment, never from a regex over the source.
run_cmd Command.liftTermElabM do
  let env ← getEnv
  let mut rows : Array (String × String × String) := #[]
  for (nm, info) in env.constants.toList do
    match info with
    | .thmInfo ti =>
      if let some idx := env.getModuleIdxFor? nm then
        let ms := (env.header.moduleNames[idx.toNat]!).toString
        if ms.startsWith "RequestProject" && !nm.isInternal then
          let t ← withOptions (fun o => (o.setBool `pp.fullNames true)) <| Lean.Meta.ppExpr ti.type
          rows := rows.push (ms, nm.toString, toString t)
    | _ => pure ()
  let sorted := rows.qsort (fun a b => if a.1 == b.1 then a.2.1 < b.2.1 else a.1 < b.1)
  let mut cur := ""
  let mut nSrc := 0
  let mut nGen := 0
  for (m, nm, t) in sorted do
    let path := "RequestProject/" ++ ((m.splitOn ".").drop 1 |>.foldl (fun a s => if a == "" then s else a ++ "/" ++ s) "") ++ ".lean"
    let src ← IO.FS.readFile path
    let leaf := (nm.splitOn ".").getLast!
    let declared := (src.splitOn ("theorem " ++ leaf)).length > 1 || (src.splitOn ("lemma " ++ leaf)).length > 1
    if declared then nSrc := nSrc + 1 else nGen := nGen + 1
    if m != cur then
      IO.println ""
      IO.println s!"===== {m}   ({path}) ====="
      cur := m
    IO.println ""
    IO.println (if declared then s!"{nm} :" else s!"{nm} :   [compiler-generated]")
    for line in (t.splitOn "\n") do IO.println s!"    {line}"
  IO.println ""
  IO.println s!"===== TOTALS: {nSrc} source-declared, {nGen} compiler-generated, {nSrc+nGen} theorem-kind declarations ====="
