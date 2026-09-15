# Day 04 - EC Optimization and Final Na(100) Slab Relaxation

## Overview

Day 04 focused on completing the DFT geometry optimization of ethylene carbonate (EC) and obtaining a converged Na(100) surface structure for the subsequent Na/EC interface model.

---

## 1. Ethylene Carbonate (EC) DFT Relaxation

The verified 3D EC structure (C3H4O3) was optimized using VASP.

### Final settings

- ENCUT = 500 eV
- PREC = Accurate
- EDIFF = 1E-6
- EDIFFG = -0.01 eV/A
- ISMEAR = 0
- SIGMA = 0.05 eV
- IBRION = 1
- POTIM = 0.1
- NSW = 60
- ISIF = 2
- LREAL = .FALSE.
- NCORE = 4
- KPOINTS = Gamma-only (1x1x1)

The EC relaxation successfully reached the required accuracy.

### Final force

- Maximum force = 0.007463 eV/A
- RMS force = 0.003845 eV/A

The optimized EC structure was saved as:

`structures/POSCAR_EC_relaxed`

---

## 2. Na(100) Slab Final Relaxation

The Na(100) slab consists of:

- BCC Na
- (100) surface
- 5 atomic layers
- 3x3 surface repetition
- 90 Na atoms
- Surface dimensions approximately 12.87 x 12.87 A
- Vacuum approximately 10 A

The initial slab relaxation was performed using lower-cost diagnostic settings. A subsequent final relaxation was performed using higher-accuracy settings.

### Final Na(100) settings

- ENCUT = 500 eV
- PREC = Normal
- EDIFF = 1E-5
- EDIFFG = -0.01 eV/A
- ISMEAR = 1
- SIGMA = 0.1 eV
- IBRION = 2
- POTIM = 0.1
- NSW = 100
- ISIF = 2
- LREAL = Auto
- NCORE = 4
- KPOINTS = 8x8x1 Gamma-centered
- ISPIN = 1

---

## 3. HPC Relaxation and Restart

The first final Na(100) relaxation (Job 555) did not converge within the 3-hour walltime and was terminated by Slurm due to timeout.

The calculation was not restarted from the original geometry. Instead, the latest `CONTCAR` from Job 555 was used as the starting `POSCAR` for a continuation run.

The continuation was performed using:

- 16 MPI tasks
- 24-hour walltime
- `mpirun`
- VASP 6.5.1
- Intel oneAPI 2025

Job 556 completed successfully in approximately 1 h 38 min.

---

## 4. Final Na(100) Convergence

VASP reported:

`reached required accuracy - stopping structural energy minimisation`

Final force:

- Maximum force = 0.008129 eV/A
- RMS force = 0.005977 eV/A

Since the maximum force is below the convergence criterion of 0.01 eV/A, the Na(100) geometry was considered converged.

The final structure was saved as:

`structures/POSCAR_Na100_3x3_final`

---

## 5. Computational Lessons

Several practical HPC lessons were established during the calculation:

1. Slurm `TIMEOUT` should be distinguished from an actual VASP failure.
2. `mpirun` provided a stable execution method on the AhmedLab system.
3. Increasing the MPI task count from 4 to 16 reduced the observed wall-clock time for the 90-atom Na(100) relaxation.
4. A partially relaxed `CONTCAR` can be used as the starting geometry for a continuation run.
5. Convergence should be verified from the VASP output and final forces rather than relying only on Slurm reporting `COMPLETED`.

---

## 6. Milestone

At the end of Day 04:

- EC optimized geometry obtained.
- Na(100) slab successfully converged.
- Final structures archived in the repository.
- DFT input parameters archived for reproducibility.

### Next milestone

Construct and inspect the initial Na(100)/EC interface using the converged Na(100) slab and optimized EC molecule.