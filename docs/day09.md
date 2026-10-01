# Day 09 - EC Crystal Validation and Production Functional Selection

## Overview

Day 09 validated the organic/condensed-phase side of the DFT methodology before rebuilding the Na(100)/EC slab for AIMD.

An experimental ethylene carbonate crystal structure was obtained from the Cambridge Crystallographic Data Centre (CCDC 2342820). The deposited structure is monoclinic C2/c and was measured at 86 K.

## 1. Experimental EC Crystal

The CIF contains:

- Chemical formula: C3H4O3
- Space group: C2/c
- Z = 4
- Temperature: 86 K

Experimental unit-cell parameters:

- a = 8.84779 Angstrom
- b = 6.25128 Angstrom
- c = 6.69149 Angstrom
- alpha = 90 degrees
- beta = 99.326 degrees
- gamma = 90 degrees
- Volume = 365.2144 Angstrom^3

The CIF contained six symmetry-independent atomic sites and eight C2/c symmetry operations.

Applying the deposited symmetry operations generated the complete 40-atom conventional cell:

- C = 12
- H = 16
- O = 12

The generated POSCAR was verified to contain 40 coordinate lines and no invalid fractional coordinates.

## 2. optB86b-vdW EC Crystal Validation

The experimental crystal was relaxed using:

- optB86b-vdW
- ENCUT = 600 eV
- Gamma-centered 3 x 3 x 3 k-point mesh
- ISMEAR = 0
- ISIF = 3
- EDIFFG = -0.02 eV/Angstrom
- C/H/O PBE PAW potentials
- GGA = MK
- PARAM1 = 0.1234
- PARAM2 = 1.0
- AGGAC = 0.0
- LUSE_VDW = .TRUE.
- LASPH = .TRUE.

The relaxation converged successfully.

Relaxed cell:

- a = 8.68245 Angstrom
- b = 6.23913 Angstrom
- c = 6.53117 Angstrom
- alpha = 90 degrees
- beta = 99.31199 degrees
- gamma = 90 degrees
- Volume = 349.13709 Angstrom^3

Relative to experiment, the relaxed volume is approximately 4.40% smaller.

The calculated beta angle remains very close to experiment.

## 3. rev-vdW-DF2 EC Crystal Validation

The same experimental structure was also relaxed using rev-vdW-DF2 with otherwise matching validation settings.

The relaxation converged successfully.

Relaxed cell:

- a = 8.70472 Angstrom
- b = 6.23987 Angstrom
- c = 6.56893 Angstrom
- alpha = 90 degrees
- beta = 99.38962 degrees
- gamma = 90 degrees
- Volume = 352.01990 Angstrom^3

Relative to experiment, the relaxed volume is approximately 3.61% smaller.

rev-vdW-DF2 gives a slightly smaller volume deviation than optB86b-vdW, while both preserve the experimental monoclinic C2/c structure.

## 4. Spin-Polarization Compatibility

Spin-polarized bulk-Na tests were performed for the two main nonlocal-vdW candidates.

### optB86b-vdW

- ISPIN = 2
- Final magnetic moment approximately -0.0003 mu_B
- Calculation completed successfully

### rev-vdW-DF2

- ISPIN = 2
- Final magnetic moment = 0.0000 mu_B
- Calculation completed successfully

Both methods therefore run correctly with spin polarization on the AhmedLab VASP environment.

## 5. Final Functional Selection

Combining the Day 8 Na bulk and Na/EC interaction screening with the Day 9 EC crystal and spin tests gave the following evidence.

### Na bulk

- PBE: 4.19547 Angstrom
- PBE+D3 zero damping: 4.16202 Angstrom
- optB86b-vdW: 4.17666 Angstrom
- rev-vdW-DF2: 4.16805 Angstrom

### Fixed-geometry Na/EC interaction

- PBE: -0.089857 eV
- PBE+D3 zero damping: -0.153635 eV
- optB86b-vdW: -0.193608 eV
- rev-vdW-DF2: -0.159933 eV

### EC crystal validation

- optB86b-vdW volume error: approximately -4.40%
- rev-vdW-DF2 volume error: approximately -3.61%

Considering the combined Na-metal, Na/EC, EC-crystal, and spin-compatibility checks, optB86b-vdW was selected as the production functional for the P5 workflow.

## Production DFT Method

The working production recipe is:

- Exchange-correlation: optB86b-vdW
- Na potential: Na_pv
- O/C/H: standard PBE PAW potentials
- ENCUT = 500 eV for production interface calculations
- GGA = MK
- PARAM1 = 0.1234
- PARAM2 = 1.0
- AGGAC = 0.0
- LUSE_VDW = .TRUE.
- LASPH = .TRUE.
- ISPIN = 2 for reactive AIMD

The EC crystal validation used ENCUT = 600 eV as a dedicated condensed-phase validation calculation.

## Milestone

The production DFT methodology for the P5 Na/EC workflow was selected after bulk-metal, interface-interaction, condensed-phase organic, and spin-compatibility checks.

## Next Milestone

Rebuild the Na(100) slab using the selected functional and its consistent Na lattice parameter, define the frozen layers by atomic height, place EC using the previous interface as a structural reference, and perform a quick interface relaxation before AIMD.
