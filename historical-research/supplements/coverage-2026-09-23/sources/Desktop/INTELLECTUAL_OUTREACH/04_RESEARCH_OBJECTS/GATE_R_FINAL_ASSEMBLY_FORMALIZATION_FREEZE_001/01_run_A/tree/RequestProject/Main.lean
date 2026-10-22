/-
Gate R overnight pilot.  TWO independent bounded targets, no automatic continuation.

  R1 (PRIMARY)   R1.h41_multiplicative_duplication_height   — RequestProject/R1/Height.lean
  R0 (SECONDARY) R0.properHeightTwoDescentTorsion           — RequestProject/R0/Torsion.lean

R0 imports nothing from the frozen chain and is independent of R1.
-/
import RequestProject.P01.TwoTorsion
import RequestProject.P01.Instances
import RequestProject.P01.PortedRunB
import RequestProject.P03a.PointMaps
import RequestProject.P03b.Additivity
import RequestProject.P03c.Kernels
import RequestProject.P03d.Composites
import RequestProject.P03e.Bridge
import RequestProject.P04a.Cokernels
import RequestProject.SDyadic.Saturation
import RequestProject.SDyadic.Instances
import RequestProject.P04b.Reconnect
import RequestProject.P04c.TwoDescent
import RequestProject.R1.Height
import RequestProject.R0.Torsion
