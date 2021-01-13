from surfgen.surface import make_surface

make_surface('../unitcells/hap_unit_cell.pdb','../surfaces/hap-surf.cif',
             plane=(1,1,0), nlayers=10, vacuum=20,
             supercell=(4,8),
             displace=0.02)

