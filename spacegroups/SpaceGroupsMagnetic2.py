# -*- coding: utf-8 -*-
"""
Get SpaceGroup general positions from Bilbao Crystallographic Server:
https://www.cryst.ehu.es/

Aroyo, et. al. Zeitschrift fuer Kristallographie (2006), 221, 1, 15-27.

Saves data to SpaceGroupsMagnetic.json
Load with:
import json
with open('SpaceGroupsMagnetic.json', 'r') as fp:
    magnetic_spacegroups = json.load(fp)

magnetic_spacegroups['61.433']:
        'parent number': sg,
        'space group number': number,
        'space group name': label,
        'setting': setting,
        'type name': type_name,
        'related group': rel_number,
        'related name': rel_name,
        'related setting': rel_setting,
        'operators general': xyz_op,
        'operators magnetic': mxmymz_op,
        'operators time': time,

@author: Dan
"""

import re
import requests
import json

# Bilbao Crystallographic server cgi-bin server requests:
# Magnetic space groups for each space group
url_mag_coord = "https://www.cryst.ehu.es/cgi-bin/cryst/programs/nph-magtrgen?gnum=%s" # General Positions of the Group 
url_mag_wykof = "https://www.cryst.ehu.es/cgi-bin/cryst/programs/nph-magwplist?gnum=%s" # Wyckoff Positions

# Regex for replacing html tags
tagregex = re.compile('<td.+?>|</td>|<nobr>|</nobr>|<br>|</br>|<sub>|</sub>|<a.+?>|</a>|<font>|</font>')
xyzregex = re.compile('[\+-]*[\+xyz-]+[\+-/\d]*,\s*[\+-]*[\+xyz-]+[\+-/\d]*,\s*[\+-]*[\+xyz-]+[\+-/\d]*,\s*[\+-]1')
magregex = re.compile('[\+-]*m[\+-xyz]+[\+-/\d]*,\s*[\+-]*m[\+-xyz]+[\+-/\d]*,\s*[\+-]*m[\+-xyz]+[\+-/\d]*|0,0,0')

with open('SpaceGroups.json', 'r') as fp:
    spacegroups = json.load(fp)
with open('SpaceGroupsMagnetic.json', 'r') as fp:
    spacegroupsmagnetic = json.load(fp)

mag_space_groups = []
for sg in range(1,231):
    spacegroup = spacegroups[str(sg)]
    mag_space_groups += spacegroup['magnetic space groups'] 

for n, msg in enumerate(mag_space_groups):
    html_page = requests.get(url_mag_coord % msg).content.decode()
    html_page = html_page.replace('\n','')

    rows = re.findall('<tr.+?</tr>', html_page)
    xyzt = []
    mxmymz = []
    time = []
    for row in rows:
        if "/html/gif/paropen.png" not in row: continue
        cols = re.findall('<td.+?</td>', row)
        # Column 1: Number
        number = tagregex.sub('', cols[0])
        # Column 2: (x,y,z) form    
        xyz_form = tagregex.sub('', cols[1])
        xyzt += [xyzregex.findall(xyz_form)[0]]
        mxmymz += [magregex.findall(xyz_form)[0]]
        #xyz, mxmymz = re.split(',\s*\+1|,\s*-1', xyz_form)
        time += [re.findall('\+1|-1', xyz_form)[0]]
        #print('%3s  %s   %s   %s' % (number, xyzt[-1], time[-1], mxmymz[-1]))
        # Column 3: Matrix form 

        # Column 4: Geom. interp.   

        # Column 5: Seitz notation

    # Wyckoff Positions
    html_page2 = requests.get(url_mag_wykof % msg).content.decode()
    html_page2 = html_page2.replace('\n','')

    rows2 = re.findall('<tr><td align=center>\d+</td>.+?</table></td></tr>', html_page2)

    # Bottom table
    idx = html_page2.index('Site Symmetries of the Wyckoff Positions')
    rows2 = re.findall('<tr>.+?</tr>', html_page2[idx:])

    wyckoff = []
    representative = []
    sitesymmetry = []
    for row2 in rows2[1:-1]:
        cols2 = re.findall('<td.+?</td>', row2)

        # Column 1: Number
        wyckoff += [tagregex.sub('', cols2[0])]
        # Column 2: Representative operation   
        representative += [tagregex.sub('', cols2[1])]
        # Column 3: Site Symmetry
        sitesymmetry += [tagregex.sub('', cols2[2])]

    spacegroupsmagnetic[msg]['positions general'] = xyzt
    spacegroupsmagnetic[msg]['positions magnetic'] = mxmymz
    spacegroupsmagnetic[msg]['wyckoff position'] = wyckoff
    spacegroupsmagnetic[msg]['wyckoff representative'] = representative
    spacegroupsmagnetic[msg]['wyckoff site symmetry'] = sitesymmetry


    print('%4d  %6s operators: %3d wyckoff: %3d positions: %3d mxmymz: %3d  %s' % (n, msg, len(spacegroupsmagnetic[msg]['operators general']), len(wyckoff), len(xyzt), len(mxmymz), mxmymz))

    if len(mxmymz) != len(xyzt): stop
    if len(mxmymz) < len(spacegroupsmagnetic[msg]['operators general']): stop


# Save as json file
with open('SpaceGroupsMagnetic.json', 'w') as fp:
    json.dump(spacegroupsmagnetic, fp, sort_keys=True, indent=4)

print('Saved spacegroups to "SpaceGroupsMagnetic.json"')

"""
# Test Load
with open('SpaceGroups.json', 'r') as fp:
    prev_spacegroups = json.load(fp)

for key, item in spacegroup.items():
    prev_spacegroups[key]['magnetic space groups'] = item

# Save as json file
with open('SpaceGroups.json', 'w') as fp:
    json.dump(prev_spacegroups, fp, sort_keys=True, indent=4)

print('Saved spacegroups to "SpaceGroups.json"')
"""

