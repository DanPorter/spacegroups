"""
Example Script for loading Spacegroup
"""

from spacegroups import load_spacegroup

sg = load_spacegroup(61)

msg = load_spacegroup(61.433)

print(sg)
print(msg)