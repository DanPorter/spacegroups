"""
Example Script for loading Spacegroup
"""

from spacegroups import load_spacegroup, find_spacegroup

sg = load_spacegroup(61)

msg = load_spacegroup(61.433)

print(sg)
print(msg)

print(msg.info())

fsg = find_spacegroup('P4/mmm1\'')
print(fsg)

print('')
print(msg)
print(msg.calc_symmetric_positions(0, 0, 0))
print(msg.calc_symmetric_moments(0, 1, 0))

print('')
print(sg.calc_matrices())
