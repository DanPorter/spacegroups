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
url_mag = "https://www.cryst.ehu.es/cryst/magnext.php?radical=%d" # Magnetic operators
url_mag_coord = "https://www.cryst.ehu.es/cgi-bin/cryst/programs/nph-magtrgen?gnum=%s" # General Positions of the Group 
url_mag_group = "https://www.cryst.ehu.es/cryst/magnext.php%s"

# Symmetry Generators as text
url_gen = "https://www.cryst.ehu.es/cgi-bin/cryst/programs/nph-getgen?what=text&gnum=%d"
# Wyckoff Positions
url_wyk = "https://www.cryst.ehu.es/cgi-bin/cryst/programs/nph-wp-list?gnum=%d&standard=True"
# Wyckoff Site info
url_point = "https://www.cryst.ehu.es/cgi-bin/cryst/programs/find_comp_op?ita=%d&standard=True&xc=%s&yc=%s&zc=%s" # num,x,y,z

spacegroup = {}
mag_group = {}

for sg in range(1,231):
    # Space Group - Magnetic Space Group list
    res = requests.get(url_mag%sg)
    html_page = res.content.decode()
    # Just look at the items listed under BNS setting - this is wrong!
    #list_st = html_page.index('BNS setting')
    #list_nd = html_page.index('OG setting')
    #maglist = html_page[list_st:list_nd]
    href = re.findall('<a href="\?gnum=.+?>', html_page)  

    print('\nSG #%s' % sg)
    spacegroup[str(int(sg))] = [] 

    # Loop over each magnetic space group link
    # Some have two links - a BNS setting and an OG settings, record both
    for p in href:
        if 'radical_sub_subsub' in p:
            setting = 'OG'
        else:
            setting = 'BNS'
        number = re.findall('gnum=\S+?&', p)[0][5:-1]
        label = re.findall('&label=\S+?&', p)[0][7:-1]

        if number in mag_group.keys(): 
            print('\tSpace Group: %s, Mag Group: #%s %s Already Stored' % (sg, number, label))
            continue

        # Navigate to magnetic group positions page
        res = requests.get(url_mag_group%p[9:-2])
        group_page = res.content.decode()

        # Group title
        ttl=re.findall('<h3>.+?</h3>',group_page)[0][4:-5]
        type_name = re.findall('Type \D+? \(\D+?\)', ttl)[0]

        # Related group
        rel=re.findall('<h4>.+?</h4>',group_page)[0][5:-6]
        if 'href' in rel:
            # Catch the sub-heading being a link
            rel = re.findall('\[.+?</a',rel)[0][1:-3]
            rel = rel.replace(']','') # number outside brackets
        rel = rel.replace('<sub>','_').replace('</sub>', '')
        print(rel)
        rel_setting = rel[:rel.index(':')]
        rel_name = rel[rel.index(':')+1:rel.index('#')].strip()
        rel_number = rel[rel.index('#')+1:]

        # Operators
        xyz_op = re.findall('<nobr>.+?<br>', group_page)
        xyz_op = [op[6:-4] for op in xyz_op]
        xyz_op = [op.replace('<font color=#ff0000>','').replace('</font>','') for op in xyz_op]

        # Magnetic Operators
        mxmymz_op = re.findall('<br>.+?</nobr>', group_page)
        mxmymz_op = [op[4:-7].replace('<sub>','').replace('</sub>','').strip() for op in mxmymz_op]
        mxmymz_op = [op.replace('<font color=#ff0000>','').replace('</font>','') for op in mxmymz_op]

        # Time symmetry
        time = re.findall('<u>\S+?</u>', group_page)
        time = [t[3:-4] for t in time]

        print("\tSpace Group: %3s, Mag Group: #%-10s %-14s : %3s %3d %3d %3d" % (sg, number, label, setting, len(xyz_op), len(mxmymz_op), len(time)))

        group_info = {
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
        }
        mag_group[number] = group_info
        spacegroup[str(int(sg))] += [number]

print(spacegroup)
print(mag_group)


# Save as json file
with open('SpaceGroupsMagnetic.json', 'w') as fp:
    json.dump(mag_group, fp, sort_keys=True, indent=4)

print('Saved spacegroups to "SpaceGroupsMagnetic.json"')


# Test Load
with open('SpaceGroups.json', 'r') as fp:
    prev_spacegroups = json.load(fp)

for key, item in spacegroup.items():
    prev_spacegroups[key]['magnetic space groups'] = item

# Save as json file
with open('SpaceGroups.json', 'w') as fp:
    json.dump(prev_spacegroups, fp, sort_keys=True, indent=4)

print('Saved spacegroups to "SpaceGroups.json"')