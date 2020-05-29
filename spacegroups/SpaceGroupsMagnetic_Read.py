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
        'positions general', 
        'positions magnetic',
        'operators general': xyz_op,
        'operators magnetic': mxmymz_op,
        'operators time': time,
        'wyckoff position', 
        'wyckoff representative', 
        'wyckoff site symmetry'

@author: Dan
"""
""" Types
Type I (Fedorov)
Type II (grey group)
Type III (translationgleiche)
Type IV (klassengleiche)
"""
""" Settings
BNS
OG
"""
import json
with open('SpaceGroups.json', 'r') as fp:
    spacegroups = json.load(fp)
with open('SpaceGroupsMagnetic.json', 'r') as fp:
    magnetic_spacegroups = json.load(fp)

keys = magnetic_spacegroups.keys()

mtype = 'Type I (Fedorov)'
ntype = 0
fmt = '%4d %3d %12s %16s %4s  p_ops: %2d, m_pos: %2d'
for n, key in enumerate(keys):
    msg = magnetic_spacegroups[key]
    setting = msg['setting']
    if msg['type name'] == mtype and setting == 'BNS':
        ntype += 1
        parent = spacegroups[str(msg['parent number'])]
        p_name = parent['space group name']
        n_ops_parent = len(parent['general positions'])
        n_ops = len(msg['operators magnetic'])
        n_pos = len(msg['positions magnetic'])

        print(fmt % (n, ntype, p_name, key, setting, n_ops_parent, n_pos))
print('%s: %d' % (mtype, ntype))

mtype = 'Type II (grey group)'
ntype = 0
fmt = '%4d %3d %12s %16s %4s  p_ops: %2d, m_pos: %2d'
for n, key in enumerate(keys):
    msg = magnetic_spacegroups[key]
    setting = msg['setting']
    if msg['type name'] == mtype and setting == 'BNS':
        ntype += 1
        parent = spacegroups[str(msg['parent number'])]
        p_name = parent['space group name']
        n_ops_parent = len(parent['general positions'])
        n_ops = len(msg['operators magnetic'])
        n_pos = len(msg['positions magnetic'])

        print(fmt % (n, ntype, p_name, key, setting, n_ops_parent, n_pos))
print('%s: %d' % (mtype, ntype))

mtype = 'Type III (translationgleiche)'
ntype = 0
fmt = '%4d %3d %12s %16s %4s  p_ops: %2d, m_pos: %2d'
for n, key in enumerate(keys):
    msg = magnetic_spacegroups[key]
    setting = msg['setting']
    if msg['type name'] == mtype and setting == 'BNS':
        ntype += 1
        parent = spacegroups[str(msg['parent number'])]
        p_name = parent['space group name']
        n_ops_parent = len(parent['general positions'])
        n_ops = len(msg['operators magnetic'])
        n_pos = len(msg['positions magnetic'])

        print(fmt % (n, ntype, p_name, key, setting, n_ops_parent, n_pos))
print('%s: %d' % (mtype, ntype))

mtype = 'Type IV (klassengleiche)'
ntype = 0
fmt = '%4d %3d %12s %16s %4s  p_ops: %2d, m_pos: %2d'
for n, key in enumerate(keys):
    msg = magnetic_spacegroups[key]
    setting = msg['setting']
    if msg['type name'] == mtype and setting == 'BNS':
        ntype += 1
        parent = spacegroups[str(msg['parent number'])]
        p_name = parent['space group name']
        n_ops_parent = len(parent['general positions'])
        n_ops = len(msg['operators magnetic'])
        n_pos = len(msg['positions magnetic'])

        print(fmt % (n, ntype, p_name, key, setting, n_ops_parent, n_pos))
print('%s: %d' % (mtype, ntype))



sg = '61'
msgs = spacegroups[sg]['magnetic space groups']
name = spacegroups[sg]['space group name']
n_ops = len(spacegroups[sg]['general positions'])
print('\n\n%3s %12s n_ops: %d' % (sg, name, n_ops))
for key in msgs:
    msg = magnetic_spacegroups[key]
    setting = msg['setting']
    m_type = msg['type name'][:7]
    m_name = msg['space group name']
    m_pos = len(msg['positions magnetic'])
    print('\t%10s %7s %3s %10s n_ops: %d' % (key, m_type, setting, m_name, m_pos))

