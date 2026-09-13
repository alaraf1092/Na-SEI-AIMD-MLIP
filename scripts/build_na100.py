from ase.build import bulk, surface
from ase.io import write

# Build conventional cubic BCC Na
na = bulk("Na", "bcc", a=4.29, cubic=True)

# Build Na(100) surface slab
slab = surface(
    na,
    (1, 0, 0),
    layers=5,
    vacuum=10.0
)

# Create a 3x3 surface supercell
slab = slab.repeat((3, 3, 1))

print(slab)
print("Number of atoms:", len(slab))
print("Cell lengths:", slab.cell.lengths())
print("Periodic boundary conditions:", slab.pbc)

# Save as VASP POSCAR
write(
    "POSCAR_Na100_3x3",
    slab,
    format="vasp",
    direct=True
)
