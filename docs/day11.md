# Day 11 — Final Na(100)/EC Interface Relaxation

## Objective

Finalize and validate the Na(100)/EC interface geometry for subsequent AIMD simulations using the selected optB86b-vdW methodology.

## Starting Interface

The interface contains:

- 54 Na atoms forming a 6-layer Na(100) slab
- 10 atoms in one EC molecule
- Total = 64 atoms
- Bottom 2 Na layers (18 atoms) frozen
- Remaining 46 atoms fully relaxed

The production functional and pseudopotential setup were retained from the previous screening:

- Exchange-correlation: optB86b-vdW
- Na: PAW_PBE Na_pv
- O/C/H: standard PBE PAWs
- ENCUT = 500 eV
- ISPIN = 2
- Γ-centered 3 × 3 × 1 k-point mesh
- Dipole correction along z
- EDIFFG = −0.02 eV/Å

## Problem with Initial Relaxation

The first interface relaxation using:

```text
IBRION = 2
POTIM  = 0.15
```

did not converge satisfactorily. After 58 ionic steps, the maximum force remained approximately:

```text
Fmax = 0.1275 eV/Å
```

The force history was oscillatory, with the largest residual forces concentrated on the EC molecule rather than the frozen Na layers.

Structural checks nevertheless showed that:

- The bottom two Na layers were correctly frozen.
- EC remained intact.
- Minimum Na–EC distance was ≈ 3.88 Å.
- The dipole position was appropriate.

## Improved Ionic Relaxation

The relaxation was restarted from the converged endpoint of Job 693 using:

```text
IBRION = 1
POTIM  = 0.15
NSW    = 150
EDIFFG = -0.02
```

All other physical and structural settings were retained.

## Job 719 Result

The restarted calculation converged in 6 ionic steps.

Maximum force evolution:

| Step | Fmax (eV/Å) |
|------|-------------|
| 1 | 0.126937 |
| 2 | 0.146880 |
| 3 | 0.093345 |
| 4 | 0.044283 |
| 5 | 0.027638 |
| 6 | 0.019834 |

The final force was:

$$F_{\max} = 0.019834\ \text{eV/Å}$$

which satisfies the convergence criterion:

$$F_{\max} < 0.020\ \text{eV/Å}$$

VASP explicitly reported:

```text
reached required accuracy - stopping structural energy minimisation
```

Therefore, the Na(100)/EC interface geometry is considered successfully relaxed.

## Final Structural Checks

The final structure was verified to have:

- 54 Na + 10 EC = 64 atoms
- 18 frozen Na atoms
- 46 free atoms
- EC bond-count check: passed
- Minimum Na–EC distance: ≈ 3.88 Å
- Appropriate dipole position
- No evidence of atomic overlap or EC structural failure

## Final Production Geometry

The converged structure from Job 719 was saved as:

```text
POSCAR_Na100_EC_6layer_optb86b_relaxed
```

A backup copy was also created:

```text
CONTCAR_job719_final
```

This structure is now designated as the production starting geometry for Na/EC AIMD.

## Conclusion

The final Na(100)/EC interface was successfully relaxed using optB86b-vdW with the bottom two Na layers constrained. Switching the ionic optimizer from `IBRION = 2` to `IBRION = 1` resolved the previous force oscillation and produced a converged geometry with a maximum residual force of 0.019834 eV/Å.