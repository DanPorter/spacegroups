"""
Get SpaceGroup general positions from Bilbao Crystallographic Server:
https://www.cryst.ehu.es/
Ref: Aroyo, et. al. Zeitschrift fuer Kristallographie (2006), 221, 1, 15-27.

Magnetic SpaceGroup properties are extracted from Bilbao Crystallographic Server:
https://www.cryst.ehu.es/cgi-bin/cryst/programs/magget_gen.pl
Ref: S. V. Gallego, et al., J. Appl. Cryst. (2012), 45(6), 1236-1247.

Usage:
    from spacegroups import load_spacegroup
    sg = load_spacegroup(61)
    msg = load_spacegroup(61.433)

    print(sg.general_positions)
    >> ['x,y,z', '-y,x-y,z', '-x+y,-x,z', '-x,-y,z+1/2', 'y,-x+y,z+1/2', 'x-y,x,z+1/2', 'y,x,-z', 'x-y,-y,-z',
    '-x,-x+y,-z', '-y,-x,-z+1/2', '-x+y,y,-z+1/2', 'x,x-y,-z+1/2', '-x,-y,-z', 'y,-x+y,-z', 'x-y,x,-z', 'x,y,-z+1/2',
    '-y,x-y,-z+1/2', '-x+y,-x,-z+1/2', '-y,-x,z', '-x+y,y,z', 'x,x-y,z', 'y,x,z+1/2', 'x-y,-y,z+1/2', '-x,-x+y,z+1/2']

Spacegoup proeprties are stored in JSON files, accessible as a dict. Each spacegroup is a dict within this.

E.G.
from spacegroups import spacegroups, spacegroups_magnetic
sg = spacegroups()['61']
{
     'general positions': ['x,y,z',...,'-x+1/2,y+1/2,z'],
     'magnetic space groups': ['61.433',...,'73.6.648'],
     'positions centring': ['x,y,z'],
     'positions coordinates': [ ['x,y,z',...,'-x+1/2,y+1/2,z'],
                                ['0,0,1/2',..., '1/2,1/2,1/2'],
                                ['0,0,0',..., '1/2,1/2,0']],
     'positions multiplicity': [8, 4, 4],
     'positions symmetry': ['1', '-1', '-1'],
     'positions wyckoff letter': ['c', 'b', 'a'],
     'space group name': 'Pbca',
     'space group name html': '<i>P</i><i>b</i><i>c</i><i>a</i> (No. 61)',
     'space group number': 61,
     'subgroup index': ['2', '2', '2', '3', '5', '7'],
     'subgroup name': ['P21/c', 'P212121', 'Pca21', 'Pbca', 'Pbca', 'Pbca'],
     'subgroup number': ['14', '19', '29', '61', '61', '61'],
     'subgroup type': ['t', 't', 't', 'k', 'k', 'k'],
     'web address generator': 'https://www.cryst.ehu.es/cgi-bin/cryst/programs/nph-getgen?what=text&gnum=61',
     'web address site check': 'https://www.cryst.ehu.es/cgi-bin/cryst/programs/find_comp_op?ita=61&standard=True&xc=%s&yc=%s&zc=%s',
     'web address wyckoff': 'https://www.cryst.ehu.es/cgi-bin/cryst/programs/nph-wp-list?gnum=61&standard=True'
 }

msg = spacegroups_magnetic()['61.433']
{
     'operators general': ['x,y,z',...,'-x+1/2,y+1/2,z'],
     'operators magnetic': ['mx,my,mz',...,'mx,-my,-mz'],
     'operators time': ['+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1'],
     'parent number': 61,
     'positions general': ['x,  y,  z, +1',...,'x+1/2,  y,  -z+1/2, +1'],
     'positions magnetic': ['mx,my,mz',...,'-mx,-my,mz'],
     'related group': '61.1.497',
     'related name': 'Pbca',
     'related setting': 'OG',
     'setting': 'BNS',
     'space group name': 'Pbca',
     'space group number': '61.433',
     'type name': 'Type I (Fedorov)',
     'wyckoff position': ['4a', '4b', '8c'],
     'wyckoff representative': ['(0,0,0 | mx,my,mz)',...,'(x,y,z | mx,my,mz)'],
     'wyckoff site symmetry': ['-1', '-1', '1']
}

By Dan Porter
Beamline Scientists, I16
Diamond Light Source Ltd.
May 2020
"""

__version__ = '1.1.0'
__date__ = '01/06/2020'

from .spacegroup_functions import load_spacegroup, spacegroups, spacegroups_magnetic
from .spacegroup_functions import find_spacegroup, find_magnetic_spacegroup
from .spacegroup_names import all_spacegroups, all_magnetic_spacegroups
