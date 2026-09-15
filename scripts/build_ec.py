from ase.io import read, write

# Read the verified 3D ethylene carbonate (EC) structure
ec = read("structures/EC.sdf")

# Put EC in a large cubic vacuum box of 15Angstrom
ec.set_cell([15.0, 15.0, 15.0])
ec.center()
ec.pbc = True

print(ec)
print("Number of atoms:", len(ec))
print("Chemical formula:", ec.get_chemical_formula())

# Save EC structure as XYZ
write(
    "structures/EC.xyz",
    ec,
    format="xyz"
)
# Save EC structure as VASP POSCAR
write(
    "structures/POSCAR_EC",
    ec,
    format="vasp",
    direct=True
)