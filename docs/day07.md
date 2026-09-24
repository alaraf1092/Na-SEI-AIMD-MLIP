# Day 07 - Converged Na(100)/EC Interface Relaxation

## Overview

Day 07 completed the structural relaxation of the Na(100)/EC interface using the cleaned PBE + D3(BJ) setup.

The final geometry was obtained from the continuation of the validated interface relaxation and passed the requested VASP force-convergence criterion.

## 1. Final Relaxation

The relaxation was performed using:

- Na(100)/EC interface
- 100 atoms total
- 90 Na + 10 EC atoms
- ENCUT = 500 eV
- Gamma-centered 3 x 3 x 1 k-point mesh
- PBE exchange-correlation functional
- D3(BJ) dispersion correction (IVDW = 12)
- 27 frozen Na atoms
- 73 mobile atoms
- Force convergence criterion: 0.02 eV/Angstrom

The final VASP calculation reached:

- Maximum force = 0.019345 eV/Angstrom
- RMS force = 0.008154 eV/Angstrom

VASP reported:

eached required accuracy - stopping structural energy minimisation

## 2. Structural Validation

The final POSCAR was checked after relaxation.

The selective-dynamics constraints were preserved:

- 27 atoms: F F F
- 73 atoms: T T T

The relaxed interface retained a physically separated Na surface and EC molecule.

The minimum three-dimensional Na-EC distance was calculated as:

**3.8866 Angstrom**

## 3. Final Structure

The converged interface structure was saved as:

structures/relaxed/POSCAR_Na100_EC_relaxed

This structure is now the validated starting geometry for subsequent simulations.

## Milestone

**Converged Na(100)/EC interface geometry obtained and added to the project repository.**

## Next Milestone

Use the relaxed Na(100)/EC structure as the starting configuration for the next DFT/AIMD stage.
