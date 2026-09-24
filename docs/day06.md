# Day 06 - Na(100)/EC DFT Relaxation and vdW Validation

## Overview

Day 06 focused on the initial DFT geometry optimization of the Na(100)/EC interface and validation of the dispersion-correction setup used for the interface calculation.

---

## 1. Initial Interface Relaxation

The initial Na(100)/EC interface from Day 05 was used as the starting geometry.

The DFT relaxation was performed using VASP with:

- ENCUT: 500 eV
- k-point mesh: 3x3x1
- PBE exchange-correlation functional
- D3(BJ) dispersion correction
- 27 bottom Na atoms fixed
- Remaining 73 atoms allowed to relax
- Force convergence criterion: 0.02 eV/Å

### Initial relaxation attempts

The first long relaxation (Job 557) progressed through approximately 62 ionic steps before reaching the wall-time limit.

A restart calculation (Job 558) was then performed from the latest valid geometry. The maximum force decreased to approximately 0.030 eV/A, but the calculation again reached the wall-time limit before satisfying the final convergence criterion.

The resulting geometry was preserved as:

`CONTCAR_step16_backup`

This structure was retained as the valid restart geometry for subsequent calculations.

---

## 2. vdW Correction Validation

During subsequent calculations, an unintended combination of dispersion settings was identified involving both:

`IVDW = 12`

and

`LUSE_VDW = .TRUE.`

The calculation was therefore reset to the valid Job 558 geometry, and the vdW setup was rechecked.

For the intended calculation, the dispersion correction was set as:

- `IVDW = 12`
- `LUSE_VDW` omitted

A diagnostic single-point calculation was performed with:

- ENCUT: 500 eV
- IBRION: -1
- NSW: 0

### Job 572

Job 572 completed successfully:

- Runtime: 01:39:42
- Exit code: 0:0
- `IVDW = 12`
- No `LUSE_VDW` setting

The calculated total energy was:

`TOTEN = -187.68471419 eV`

The calculation confirmed that the intended D3(BJ) setup could run successfully for the 100-atom Na(100)/EC interface.

---

## 3. Milestone

At this stage:

- Initial Na(100)/EC interface successfully subjected to DFT relaxation attempts.
- A valid intermediate relaxed interface geometry was preserved.
- Incorrect vdW settings were identified and removed from the workflow.
- Clean D3(BJ) single-point calculation successfully completed.
- Valid starting geometry and corrected DFT setup are available for the next relaxation stage.

### Next milestone

Perform the Na(100)/EC interface geometry optimization using the validated PBE + D3(BJ) setup.
