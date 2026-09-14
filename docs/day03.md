# Day 3 - Na(100) Surface Relaxation

**Project:** AIMD + ML Interatomic Potentials for SEI Formation in Na-Ion Batteries

**Day:** 3

**Date:** 2026-09-14

**Main tools:** VASP, Slurm, OVITO

**System:** Na(100) 3 x 3 surface slab

---

## Objectives

The main objectives of Day 3 were:

- Relax the 90-atom Na(100) surface slab using DFT.
- Verify that the structural relaxation reaches the specified force convergence criterion.
- Inspect the relaxed structure using OVITO.
- Save the relaxed Na(100) structure for subsequent interface calculations.
- Establish a working surface model before introducing electrolyte molecules.

---

## 1. Starting Na(100) Surface

The starting structure was the 3 x 3 Na(100) surface slab constructed previously using ASE.

### Structure

| Property | Value |
|---|---|
| Material | Na |
| Crystal structure | BCC |
| Surface orientation | (100) |
| Number of layers | 5 |
| Surface repetition | 3 x 3 |
| Number of atoms | 90 |
| Surface dimensions | ~12.87 x 12.87 Ã… |
| Vacuum | ~10 Ã… |
| Periodicity | x and y |
| Cell z-length | ~39.305 Ã… |

The initial structure was stored as:

`structures/POSCAR_Na100_3x3`

---

## 2. DFT Relaxation Setup

The Na(100) slab was structurally relaxed using VASP.

The main relaxation settings were:

```text
SYSTEM = Na(100) slab relaxation
ENCUT = 200
PREC = Accurate
EDIFF = 1E-6
ISMEAR = 0
SIGMA = 0.2
IBRION = 2
NSW = 100
ISIF = 2
EDIFFG = -0.02
ISPIN = 1
ISTART = 0
ICHARG = 2
LREAL = Auto
LWAVE = .FALSE.
LCHARG = .FALSE.

