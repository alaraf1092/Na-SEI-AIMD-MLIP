\# Day 3 — Na(100) Surface Relaxation



\*\*Date:\*\* 2026-09-14



\## Objective



The objective of Day 3 was to obtain a relaxed Na(100) surface structure that can be used as the starting substrate for the later Na–electrolyte interface calculations.



\## Starting Structure



A 3×3 Na(100) surface slab was used as the starting structure.



\- Crystal structure: BCC Na

\- Surface orientation: Na(100)

\- Surface supercell: 3×3

\- Number of atoms: 90 Na atoms

\- Surface dimensions: approximately 12.87 × 12.87 Å

\- Vacuum region: approximately 10 Å

\- Periodic boundary conditions: x and y directions only



The initial structure was generated using ASE and stored as:



`structures/POSCAR\_Na100\_3x3`



\## DFT Relaxation Setup



The Na(100) slab was structurally relaxed using VASP.



Important settings:



```text

ENCUT = 200 eV

PREC = Accurate

EDIFF = 1E-6

ISMEAR = 0

SIGMA = 0.2

IBRION = 2

NSW = 100

ISIF = 2

EDIFFG = -0.02 eV/Å

ISPIN = 1

LREAL = Auto



A Γ-point-only 1×1×1 k-point mesh was used for this diagnostic slab relaxation.



The calculation was performed on the HPC cluster using VASP with Intel oneAPI and Intel MPI. The working execution method used mpirun rather than srun.



Relaxation Result



The relaxation completed successfully under Slurm (Job 550).



VASP reported:



reached required accuracy - stopping structural energy minimisation



The final force values were:



Maximum force = 0.012948 eV/Å

RMS force     = 0.008985 eV/Å



The maximum force is below the specified convergence criterion of 0.02 eV/Å.



The total energy decreased during the relaxation. For example:



Ionic step	Free energy F (eV)

3	-116.45851

4	-116.48562

5	-116.51150



The final relaxed structure was saved as:



structures/POSCAR\_Na100\_3x3\_relaxed



Structural Inspection



The relaxed Na(100) surface was inspected using OVITO.



The slab remained structurally intact after relaxation, with no obvious detached atoms or pathological structural deformation observed.



The visual inspection, together with the converged force criterion, indicates that the structure is suitable as an intermediate relaxed surface model.



Scientific Interpretation



Surface relaxation allows the Na atoms to adjust from their ideal bulk-truncated positions to positions that minimize the DFT-calculated forces.



This step is important before introducing electrolyte molecules because an unrelaxed surface could introduce artificial forces and distortions into subsequent Na–electrolyte calculations.



The relaxed Na(100) slab will therefore serve as the substrate for constructing the initial Na–EC interface.



Important Limitations



The present relaxation is a working intermediate rather than the final production-quality surface calculation.



Further convergence/validation is still required for:



final ENCUT selection for the complete Na–C–H–O system,

reliable k-point sampling for metallic Na,

slab thickness convergence,

vacuum thickness convergence,

and final production settings for the Na–EC interface.



Therefore, the current relaxed structure should be regarded as a validated working model, not yet the final converged production surface.



Day 3 Workflow

Na(100) 3×3 slab

&#x20;      ↓

VASP structural relaxation

&#x20;      ↓

Check force convergence

&#x20;      ↓

Inspect structure in OVITO

&#x20;      ↓

Save relaxed Na(100)

&#x20;      ↓

Next: construct Na(100) + EC interface

Completed

&#x20;Built 90-atom Na(100) 3×3 slab

&#x20;Prepared VASP relaxation calculation

&#x20;Successfully ran relaxation on HPC

&#x20;Achieved maximum force below 0.02 eV/Å

&#x20;Inspected relaxed structure in OVITO

&#x20;Saved relaxed Na(100) structure

&#x20;Complete final surface convergence tests

&#x20;Construct Na(100) + EC interface

Day 3 Status



Na(100) surface relaxation completed successfully.



The relaxed surface is now ready to be used as the starting structure for the next stage of the project: constructing the Na(100)–EC interface.

