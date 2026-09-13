from ase.build import bulk
from ase.io import write

# Build conventional cubic BCC Na
na = bulk("Na", "bcc", a=4.29, cubic=True)

print(na)
print("Number of atoms:", len(na))
print("Lattice parameters:", na.cell.lengths())

# Save structure in VASP POSCAR format
write("POSCAR_Na_cubic", na, format="vasp", direct=True)
