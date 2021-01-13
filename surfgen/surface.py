from ase.io import read, write
from ase.build import cut, surface, make_supercell
import numpy


def make_surface(input_file, output_file, plane=(1, 0, 0),
                 nlayers=2, vacuum=0, supercell=(1,1), displace=0):
    """
    :param input_file: input file containing unit cell
    :param output_file: output file for generated surface
    :param plane: surface plane
    :param nlayers: number of layers
    :param vacuum: vacuum padding around the surface
    :param supercell: supercell dimensions
    :param displace: displacement of atoms within unit cell
    :return:
    """
    unit_cell = read(input_file)
    if displace != 0:
        unit_cell.translate(displace)
    surf = surface(unit_cell, plane, nlayers, vacuum=vacuum, periodic=True)
    if supercell != (1, 1):
        multiplier = numpy.identity(3)
        for i in range(2):
            multiplier[i][i] = supercell[i]
        surf = make_supercell(surf, multiplier)
    write(output_file, surf)
    return unit_cell

