# -*- coding: utf-8 -*-
"""
Get SpaceGroup general positions from Bilbao Crystallographic Server:
https://www.cryst.ehu.es/

Aroyo, et. al. Zeitschrift fuer Kristallographie (2006), 221, 1, 15-27.

Saves data to SpaceGroups.json
Load with:
import json
with open('SpaceGroups.json', 'r') as fp:
    spacegroups = json.load(fp)

spacegroups['61']:
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

@author: Dan
"""

import re
import requests
import json

# Bilbao Crystallographic server cgi-bin server requests:
# Symmetry Generators as text
url_gen = "https://www.cryst.ehu.es/cgi-bin/cryst/programs/nph-getgen?what=text&gnum=%d"
# Wyckoff Positions
url_wyk = "https://www.cryst.ehu.es/cgi-bin/cryst/programs/nph-wp-list?gnum=%d&standard=True"
# Wyckoff Site info
url_point = "https://www.cryst.ehu.es/cgi-bin/cryst/programs/find_comp_op?ita=%d&standard=True&xc=%s&yc=%s&zc=%s" # num,x,y,z
# Maximal Subgroups
url_subg = "https://www.cryst.ehu.es/cgi-bin/cryst/programs/nph-lxi?gnum=%d"

def get_spacegroup(sg):

    # General Positions
    res = requests.get(url_gen%sg)
    html_page = res.content.decode()
    pos = re.findall('<big>\d+ \S+</big>',html_page)
    general_positions = [p[5:-6].split()[1] for p in pos]

    # Wyckoff Positions
    res = requests.get(url_wyk%sg)
    html_page = res.content.decode()
    tab = re.findall('<td align=center>\S.{0,10}</td>',html_page) 
    tab = [t[17:-5] for t in tab]
    multiplicity = [int(t) for t in tab[::3]]
    wyckoff_letter = tab[1::3]
    site_symmetry = tab[2::3]
    # Spit Coordinate rows
    coord_start = [m.start(0) for m in re.finditer('<table><tr><td><nobr>',html_page)]
    coord_end = [m.start(0) for m in re.finditer('</table></td></tr>',html_page)]
    coordinates = []
    for st, nd in zip(coord_start, coord_end):
        coord = re.findall('>\(\S+,\S+,\S+\)<',html_page[st:nd])
        coordinates += [[t.strip('<>()') for t in coord]]
    count_coordinates = [len(t) for t in coordinates]

    # Space Group name
    title = re.findall('<h2 align="center">Wyckoff Positions of Group .+?</h2>', html_page)
    html_name = title[0][45:-5].strip()
    name = re.sub('<.+?>','',html_name) # remove html tags
    name = name.split()[0] # remove (No. ###)

    # Centring Operations
    centre = re.findall('Coordinates</th></tr><tr><td align=center>.*?</td>', html_page)
    centre = centre[0][42:-5]
    centre = centre.replace('+',' ').replace('(',' ').replace(')',' ').split()
    # add xyz
    centring_operations = ['x,y,z']
    for n in range(1,len(centre)):
        op = 'x+%s,y+%s,z+%s'%tuple(centre[n].split(','))
        centring_operations += [op.replace('+0','')]

    # Maximal Subgroups
    res = requests.get(url_subg%sg)
    html_page = res.content.decode()
    tab_lines=re.findall('<tr>.+?</tr>', html_page)
    sub_num = []
    sub_name = []
    sub_index = []
    sub_type = []
    for ln in tab_lines[1:]:
        ln = ''.join(re.split('<.+?>',ln)).split()
        sub_num += [ln[1]]
        sub_name += [ln[2]]
        sub_index += [ln[3]]
        sub_type += [ln[4]]

    # Check
    lmult = len(multiplicity)
    lwyck = len(wyckoff_letter)
    lsym = len(site_symmetry)
    lcoord = len(coordinates)
    lcen = len(centring_operations)

    # Check multiplicity
    check_multiplicity = sum([abs(multiplicity[n]-(count_coordinates[n]*lcen)) for n in range(len(multiplicity))])

    fmt = '%3d %-20s GenPos: %3d, Mult: %3d, Wyk: %3d, Sym: %3d, Coord: %3d, Cen: %3d, Check: %3d'
    print(fmt % (sg, name, len(general_positions), lmult, lwyck, lsym, lcoord, lcen, check_multiplicity))

    out = {
        'space group number': sg,
        'space group name html': html_name,
        'space group name': name,
        'web address generator': url_gen%sg,
        'web address wyckoff': url_wyk%sg,
        'web address site check': url_point%(sg, "%s", "%s", "%s"),
        'general positions': general_positions,
        'positions centring': centring_operations,
        'positions multiplicity': multiplicity,
        'positions wyckoff letter': wyckoff_letter,
        'positions symmetry': site_symmetry,
        'positions coordinates': coordinates,
        'subgroup number': sub_num,
        'subgroup name': sub_name,
        'subgroup index': sub_index,
        'subgroup type': sub_type,
    }
    return out

spacegroups = {}
for sg in range(1,231):
    spacegroups[sg] = get_spacegroup(sg)


# Save as json file
with open('SpaceGroups.json', 'w') as fp:
    json.dump(spacegroups, fp, sort_keys=True, indent=4)

print('Saved spacegroups to "SpaceGroups.json"')


# Test Load
with open('SpaceGroups.json', 'r') as fp:
    spacegroups2 = json.load(fp)

print(spacegroups2['61'])
