from ase.io import read, write
import numpy as np


# Input structures
slab_file = "structures/POSCAR_Na100_3x3_final"
ec_file = "structures/POSCAR_EC_relaxed"

# Parameters
interface_distance = 3.5  # Angstrom
vacuum_above_ec = 15.0     # Angstrom

# Read structures
slab = read(slab_file)
ec = read(ec_file)

# Determine the top of the Na slab
slab_zmax = slab.positions[:, 2].max()

# Move EC so that its lowest atom is interface_distance
# above the top Na layer
ec_zmin = ec.positions[:, 2].min()
ec.translate([0.0, 0.0, slab_zmax + interface_distance - ec_zmin])

# Center EC above the middle of the Na surface
slab_center = slab.cell[:2, :2].diagonal() / 2
ec_center = ec.positions[:, :2].mean(axis=0)

ec.translate([
    slab_center[0] - ec_center[0],
    slab_center[1] - ec_center[1],
    0.0
])

# Combine Na slab and EC
interface = slab + ec

# Expand the cell in z to provide vacuum above EC
new_zmax = interface.positions[:, 2].max()
old_cell = slab.cell.copy()

new_z = new_zmax + vacuum_above_ec
new_cell = old_cell.copy()
new_cell[2] = [0.0, 0.0, new_z]

interface.set_cell(new_cell)
interface.pbc = [True, True, False]

# Save interface structure
output_file = "structures/POSCAR_Na100_EC_initial"
write(output_file, interface, format="vasp", direct=True)

# Print summary
print("=" * 60)
print("Initial Na(100)/EC interface constructed")
print("=" * 60)
print(f"Na atoms:        {len(slab)}")
print(f"EC atoms:        {len(ec)}")
print(f"Total atoms:     {len(interface)}")
print(f"Interface gap:   {interface_distance:.2f} A")
print(f"Vacuum above EC: {vacuum_above_ec:.2f} A")
print(f"Cell z:          {new_z:.2f} A")
print(f"Output:          {output_file}")
print("=" * 60)