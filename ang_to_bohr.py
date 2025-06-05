import sys

ANGSTROM_TO_BOHR = 1.8897259886  # CODATA 2018

def convert_xyz_to_bohr(input_file, decimals=12):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    try:
        num_atoms = int(lines[0])
    except ValueError:
        print("First line must be the number of atoms.")
        return

    comment_line = lines[1].strip()
    atom_lines = lines[2:]

    if len(atom_lines) != num_atoms:
        print("Mismatch between number of atoms and coordinate lines.")
        return

    fmt = f"{{:2}} {{:>20.{decimals}f}} {{:>20.{decimals}f}} {{:>20.{decimals}f}}"

    print(num_atoms)
    print(f"{comment_line} (converted to Bohr)")

    for line in atom_lines:
        parts = line.split()
        if len(parts) < 4:
            print(f"Invalid atom line: {line}")
            continue
        element = parts[0]
        x, y, z = map(float, parts[1:4])
        x_b = x * ANGSTROM_TO_BOHR
        y_b = y * ANGSTROM_TO_BOHR
        z_b = z * ANGSTROM_TO_BOHR
        print(fmt.format(element, x_b, y_b, z_b))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python xyz_to_bohr.py input_file.xyz [decimals]")
    else:
        input_file = sys.argv[1]
        decimals = int(sys.argv[2]) if len(sys.argv) > 2 else 12
        convert_xyz_to_bohr(input_file, decimals)
