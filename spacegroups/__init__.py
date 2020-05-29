"""
Get SpaceGroup general positions from Bilbao Crystallographic Server:
https://www.cryst.ehu.es/

Aroyo, et. al. Zeitschrift fuer Kristallographie (2006), 221, 1, 15-27.

Usage:
    from spacegroups import load_spacegroup
    sg = load_spacegroup(61)
    msg = load_spacegroup(61.433)

sg:
        'space group number': sg,
        'space group name html': html_name,
        'space group name': name,
        'web address generator': url_gen%sg,
        'web address wyckoff:': url_wyk%sg,
        'web address site check': url_point%(sg, "%s", "%s", "%s"))
        'general positions': general_positions,
        'positions multiplicity': multiplicity,
        'positions wyckoff letter': wyckoff_letter,
        'positions symmetry': site_symmetry,
        'positions coordinates': coordinates

msg:
        'parent number': sg,
        'space group number': number,
        'space group name': label,
        'setting': setting,
        'type name': type_name,
        'related group': rel_number,
        'related name': rel_name,
        'related setting': rel_setting,
        'positions general',
        'positions magnetic',
        'operators general': xyz_op,
        'operators magnetic': mxmymz_op,
        'operators time': time,
        'wyckoff position',
        'wyckoff representative',
        'wyckoff site symmetry'

By Dan Porter
Beamline Scientists, I16
Diamond Light Source Ltd.
May 2020
"""

__version__ = '1.0.0'

from .func import load_spacegroup, spacegroups, spacegroups_magnetic
