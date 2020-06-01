# spacegroups
Load spacegroup and magnetic spacegroup information

### Usage:
*Terminal:*
```
$ cd /location/of/file
$ ipython -m spacegroups 194 P63/mmc 61.433
>> will display spacegroup properties 
```
*Script:*
``` Python
>> from spacegroups import load_spacegroup
>> sg = load_spacegroup(61)
>> sg.general_positions
['x,y,z', '-x+1/2,-y,z+1/2', '-x,y+1/2,-z+1/2', 'x+1/2,-y+1/2,-z', '-x,-y,-z', 'x+1/2,y,-z+1/2', 'x,-y+1/2,z+1/2', '-x+1/2,y+1/2,z']

>> msg = load_spacegroup(61.433)
>> msg.positions_general
['x,  y,  z, +1', 'x+1/2,  -y+1/2,  -z, +1', '-x,  y+1/2,  -z+1/2, +1', '-x+1/2,  -y,  z+1/2, +1', '-x,  -y,  -z, +1', '-x+1/2,  y+1/2,  z, +1', 'x,  -y+1/2,  z+1/2, +1', 'x+1/2,  y,  -z+1/2, +1']
```

### Symmetrise Positions
Create a list of symmetric positions using space group symmetries:
```python
>> from spacegroups import load_spacegroup
>> sg = load_spacegroup(61)
>> sg.calc_symmetric_positions(0.5, 0, 0)
[[0.5, 0, 0], [1.0, 0.5, 0], [-0.5, 0.5, 0.5], [0.0, 0, 0.5], [-0.5, 0, 0], [0.0, 0.5, 0], [0.5, 0.5, 0.5], [1.0, 0, 0.5]]
```

### Symmetrise Magnetic Moments (axial vectors)
Create a list of symmetric moment vectors by applying magnetic spacegroup symmetry, including time operations.
```python
>> from spacegroups import load_spacegroup
>> msg = load_spacegroup(61.488)
>> msg.calc_symmetric_moments(0.5, 0, 0)
[[0.5, 0, 0], [-0.5, 0, 0], [-0.5, 0, 0], [0.5, 0, 0], [-0.5, 0, 0], [0.5, 0, 0], [0.5, 0, 0], [-0.5, 0, 0]]
```

## Spacegroup Information
SpaceGroup properties are extracted from [Bilbao Crystallographic Server](https://www.cryst.ehu.es/)

*Aroyo, et al., Zeitschrift fuer Kristallographie (2006), 221, 1, 15-27.*

Magnetic SpaceGroup properties are extracted from [Bilbao Crystallographic Server](https://www.cryst.ehu.es/cgi-bin/cryst/programs/magget_gen.pl)

*S. V. Gallego, et al., J. Appl. Cryst. (2012), 45(6), 1236-1247.*
