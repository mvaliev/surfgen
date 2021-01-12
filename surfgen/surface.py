from ase.io import read, write
from ase.build import cut, surface, niggli_reduce, make_supercell
import numpy
from ase.visualize import view


def make_surface(input,output,plane=(1,0,0), nlayers=2, vacuum=0, supercell=None, displace=None):
    crys = read(input)
    if displace is not None:
        crys.translate(displace)
    surf = surface(crys, plane, nlayers, vacuum=vacuum, periodic=True)
    if supercell is not None:
        multiplier = numpy.identity(3)
        for i in range(3):
            multiplier[i][i] = supercell[i]
        surf = make_supercell(surf, multiplier)
    write(output, surf)
    return crys

