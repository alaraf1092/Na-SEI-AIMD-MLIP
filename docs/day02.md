# Day 2 — DFT Convergence, Na(100) Surface & HPC VASP Setup

**Project:** AIMD + ML Interatomic Potentials for SEI Formation in Na-Ion Batteries  
**Day:** 2  
**Date:** 2026-09-13  
**Main tools:** ASE, VASP, Slurm, OVITO  
**System:** BCC Na → Na(100) surface

---

## Objectives

The main objectives of Day 2 were:

- Perform preliminary DFT convergence testing for bulk BCC Na.
- Construct a Na(100) surface slab using ASE.
- Transfer the surface structure to the HPC cluster.
- Set up VASP calculations using Slurm.
- Diagnose the VASP execution failure encountered for the larger surface model.
- Establish a reliable VASP execution method on the HPC.
- Successfully perform a DFT calculation for the 90-atom Na(100) slab.

---

## 1. Bulk BCC Na — ENCUT Convergence

A conventional cubic BCC Na unit cell was used for the initial DFT tests.

### Structure

- Crystal structure: BCC
- Lattice parameter: **4.29 Å**
- Number of atoms: **2**
- Exchange-correlation functional: **PBE**
- Pseudopotential: **PAW-PBE Na**

The Na POTCAR used was **PAW_PBE Na 08Apr2002**.

The pseudopotential parameters were:

- **ENMAX = 101.968 eV**
- **ENMIN = 76.476 eV**

### ENCUT values tested

| ENCUT (eV) | Energy (eV/cell) |
|---:|---:|
| 100 | -2.5884434 |
| 125 | -2.5914221 |
| 150 | -2.5948408 |
| 175 | -2.5959722 |
| 200 | -2.5963139 |

The total energy became progressively more stable as the plane-wave cutoff was increased.

A preliminary value of **200 eV** was therefore used for the subsequent Na-only slab calculations.

> **Note:** 200 eV is only a preliminary working value. The final production ENCUT must be re-evaluated once C, H, and O are introduced because the complete Na–C–H–O system must be converged consistently.

---

## 2. Bulk BCC Na — k-point Testing

Gamma-centered k-point meshes were tested:

- 3 × 3 × 3
- 5 × 5 × 5
- 7 × 7 × 7
- 9 × 9 × 9
- 11 × 11 × 11
- 13 × 13 × 13

Na is metallic, and the calculated energies showed non-monotonic behavior depending on the k-point density and smearing treatment.

Because of this behavior, a final production k-point mesh was **not selected** from this preliminary test.

Further k-point convergence testing will be performed using an appropriate treatment for metallic Na before production calculations.

---

## 3. Construction of Na(100) Surface

A Na(100) surface slab was constructed using the Atomic Simulation Environment (ASE).

The conventional cubic BCC Na structure was generated using:

    from ase.build import bulk

    na = bulk("Na", "bcc", a=4.29, cubic=True)

The Na(100) surface was then constructed using:

    from ase.build import surface

    slab = surface(
        na,
        (1, 0, 0),
        layers=5,
        vacuum=10.0
    )

A 3 × 3 surface supercell was created:

    slab = slab.repeat((3, 3, 1))

### Final Na(100) slab

| Property | Value |
|---|---|
| Material | Na |
| Crystal structure | BCC |
| Surface orientation | (100) |
| Number of layers | 5 |
| Surface repetition | 3 × 3 |
| Number of atoms | 90 |
| Surface dimensions | ~12.87 × 12.87 Å |
| Vacuum | 10 Å |
| Periodicity | x and y |
| Cell z-length | ~39.305 Å |

The structure was visualized using OVITO to verify the geometry.

The final structure was saved as **POSCAR_Na100_3x3**.

---

## 4. HPC VASP Setup

The calculations were performed on the Ahmed Lab HPC cluster using the Slurm scheduler.

### HPC environment

- Scheduler: **Slurm**
- Partition: **defq**
- Nodes: **1**
- CPUs/tasks: **4**
- VASP version: **6.5.1**
- Intel oneAPI: **2025**
- Intel MPI: **2021.17**

The Intel MPI launcher was:

    /cm/shared/apps/intel-oneapi/2025/mpi/2021.17/bin/mpirun

---

## 5. VASP Execution Problem

The initial attempts to run the 90-atom Na(100) slab using:

    srun vasp_std

resulted in repeated VASP failures and segmentation faults.

Several configurations were tested during troubleshooting, including:

- VASP 6.6.0
- VASP 6.5.1
- 1 MPI task
- 4 MPI tasks
- Gamma-only k-point sampling
- `LREAL = Auto`
- HDF5 file-locking settings

The smaller 2-atom BCC Na calculation successfully ran on the same HPC environment, demonstrating that the basic VASP installation and Intel runtime were functional.

The 90-atom slab consistently crashed after entering the electronic self-consistency loop when launched using `srun`.

---

## 6. MPI Launcher Investigation

The execution method was changed from:

    srun vasp_std

to:

    mpirun -np $SLURM_NTASKS vasp_std

Additional runtime settings were included:

    ulimit -s unlimited
    export OMP_STACKSIZE=512m
    export OMP_NUM_THREADS=1
    export HDF5_USE_FILE_LOCKING=FALSE

The final working Slurm script was:

    #!/bin/bash
    #SBATCH --job-name=Na100_slab
    #SBATCH --partition=defq
    #SBATCH --nodes=1
    #SBATCH --ntasks=4
    #SBATCH --time=00:30:00

    module load intel-oneapi/2025
    module load vasp/6.5.1

    ulimit -s unlimited
    export OMP_STACKSIZE=512m
    export OMP_NUM_THREADS=1

    export HDF5_USE_FILE_LOCKING=FALSE

    # Test Intel MPI launcher independently of srun
    mpirun -np $SLURM_NTASKS vasp_std > vasp.out

This configuration successfully ran the 90-atom Na(100) slab.

---

## 7. Successful Na(100) DFT Calculation

A single-point electronic DFT calculation was performed for the 90-atom Na(100) slab.

### Main VASP settings

    ENCUT  = 200 eV
    PREC   = Accurate
    EDIFF  = 1E-6
    ISMEAR = 0
    SIGMA  = 0.2
    IBRION = -1
    NSW    = 0
    ISPIN  = 1

This was intentionally a **single-point calculation**.

Since `IBRION = -1` and `NSW = 0`, the atomic positions were not relaxed.

---

## 8. Job Completion

The successful Slurm job was:

| Parameter | Result |
|---|---|
| Job ID | 549 |
| Job name | Na100_slab |
| Partition | defq |
| Allocated CPUs | 4 |
| State | **COMPLETED** |
| Exit code | **0:0** |

This confirms that the 90-atom Na(100) system can successfully be executed with VASP on the HPC cluster.

---

## 9. Electronic SCF Convergence

The VASP calculation completed the electronic self-consistency cycle
successfully. The final reported electronic iteration was:

DAV: 22

The final energy reported in the VASP output was:

F = -116.43534 eV

The OUTCAR reported:

free  energy   TOTEN  =      -116.43533977 eV

The calculation completed successfully with the specified electronic
convergence criterion (EDIFF = 1E-6).

---

## 10. Scientific Interpretation

The successful calculation represents the electronic energy of the **unrelaxed Na(100) slab geometry**.

It should not yet be treated as the final optimized surface structure.

The current calculation establishes that:

1. The Na(100) structure is valid.
2. The VASP input files are valid.
3. The Na POTCAR is working correctly.
4. The HPC environment can run the 90-atom surface.
5. The electronic self-consistent calculation can converge successfully.

The next step is to obtain a properly relaxed and validated Na(100) surface before introducing electrolyte molecules.

---

## 11. Current Computational Workflow

The project has now progressed from a simple bulk structure to a working DFT surface model:

    BCC Na
       ↓
    Na(100) surface
       ↓
    3 × 3 surface supercell
       ↓
    90 atoms
       ↓
    VASP + Slurm on HPC
       ↓
    Successful DFT calculation

This surface will eventually serve as the Na-metal interface for studying electrolyte decomposition and SEI formation.

---

## 12. What Was Completed Today

- [x] Generated conventional BCC Na using ASE
- [x] Performed preliminary ENCUT convergence
- [x] Performed preliminary k-point testing
- [x] Constructed Na(100) surface
- [x] Created 3 × 3 Na(100) surface supercell
- [x] Obtained a 90-atom surface model
- [x] Visualized the surface using OVITO
- [x] Transferred the structure to HPC
- [x] Set up VASP with Slurm
- [x] Diagnosed repeated VASP execution failures
- [x] Tested different VASP/MPI configurations
- [x] Established a working Intel MPI + VASP execution method
- [x] Successfully completed a 90-atom Na(100) DFT calculation

---

## 13. Remaining Work

The following items remain before moving to the Na–EC system:

- [ ] Finalize ENCUT convergence for the complete Na–C–H–O system
- [ ] Establish a reliable k-point setup for metallic Na
- [ ] Relax the Na(100) slab
- [ ] Verify slab and vacuum convergence
- [ ] Determine an appropriate surface model for electrolyte adsorption
- [ ] Construct the ethylene carbonate (EC) molecule
- [ ] Build the Na(100) + EC interface
- [ ] Perform initial Na–EC DFT calculations
- [ ] Prepare the system for AIMD

---

## 14. Next Step

The immediate next step is to **relax and validate the Na(100) surface**.

Once a stable Na(100) surface has been obtained, ethylene carbonate (EC) can be introduced to begin studying the initial chemistry associated with SEI formation.

---

# Day 2 Status

## ✅ COMPLETED

**Major milestone:** Successfully performed the first DFT calculation of the **90-atom Na(100) surface on the HPC cluster using VASP**.

The computational infrastructure is now functional, and the project can move from HPC/VASP debugging toward the actual surface and electrolyte chemistry.
