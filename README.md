# spacegroups
Load spacegroup and magnetic spacegroup information

### Usage:
``` Python
>> from spacegroups import load_spacegroup
>> sg = load_spacegroup(61)
>> sg.general_positions
['x,y,z', '-x+1/2,-y,z+1/2', '-x,y+1/2,-z+1/2', 'x+1/2,-y+1/2,-z', '-x,-y,-z', 'x+1/2,y,-z+1/2', 'x,-y+1/2,z+1/2', '-x+1/2,y+1/2,z']

>> msg = load_spacegroup(61.433)
>> msg.positions_general
['x,  y,  z, +1', 'x+1/2,  -y+1/2,  -z, +1', '-x,  y+1/2,  -z+1/2, +1', '-x+1/2,  -y,  z+1/2, +1', '-x,  -y,  -z, +1', '-x+1/2,  y+1/2,  z, +1', 'x,  -y+1/2,  z+1/2, +1', 'x+1/2,  y,  -z+1/2, +1']
```

### Spacegroup Information
SpaceGroup properties are extracted from [Bilbao Crystallographic Server](https://www.cryst.ehu.es/)
*Aroyo, et al., Zeitschrift fuer Kristallographie (2006), 221, 1, 15-27.*

Magnetic SpaceGroup properties are extracted from [Bilbao Crystallographic Server](https://www.cryst.ehu.es/cgi-bin/cryst/programs/magget_gen.pl)
*S. V. Gallego, et al., J. Appl. Cryst. (2012), 45(6), 1236-1247.*
