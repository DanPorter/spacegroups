"""
Spacegroup functions
"""

import os
import json
import difflib

from .spacegroup_classes import SpaceGroup, SpaceGroupMagnetic
from .spacegroup_names import all_spacegroups, all_magnetic_spacegroups
from .spacegroup_names import spacegroup_names, magnetic_spacegroup_names

thisdir = os.path.abspath(os.path.dirname(__file__))
file_spacegroups = os.path.join(thisdir, 'data/SpaceGroups.json')
file_magnetic_spacegroups = os.path.join(thisdir, 'data/SpaceGroupsMagnetic.json')


def spacegroups():
    """Read spacegroup file, return dict"""
    with open(file_spacegroups, 'r') as fp:
        sg = json.load(fp)
    return sg


def spacegroups_magnetic():
    """Read SapceGroupsMagetic file, return dict"""
    with open(file_magnetic_spacegroups, 'r') as fp:
        magnetic_spacegroups = json.load(fp)
    return magnetic_spacegroups


def load_spacegroup(sg_number):
    """
    Load spacegroup or magnetic spacegroup using number
    :param sg_number: int, float, str
    :return: SpaceGroup/ SpaceGroupmMgnetic
    """

    sg_number = str(sg_number)
    if '.' in sg_number:
        # Magnetic
        magnetic_spacegroups = spacegroups_magnetic()
        return SpaceGroupMagnetic(magnetic_spacegroups[sg_number])
    return SpaceGroup(spacegroups()[sg_number])


def find_spacegroup(sg_name):
    """
    Load spacegroup using symmetry name
    :param sg_name: str
    :return: SpaceGroup or None if not available
    """
    # remove spaces
    sg_name = sg_name.replace(' ', '')

    if '\'' in sg_name:
        return find_magnetic_spacegroup(sg_name)

    try:
        idx = spacegroup_names.index(sg_name)
        return load_spacegroup(all_spacegroups[idx])
    except ValueError:
        close_match = difflib.get_close_matches(sg_name, magnetic_spacegroup_names)
        print('Spacegroup: %s not in list' % sg_name)
        print('Perhaps you meant one of these: %s' % (', '.join(close_match)))
        return None


def find_magnetic_spacegroup(msg_name):
    """
    Load magnetic spacegroup using symmetry name
    :param msg_name: str
    :return: SpaceGroupMagnetic or None if not available
    """
    # remove spaces
    msg_name = msg_name.replace(' ', '')

    try:
        idx = magnetic_spacegroup_names.index(msg_name)
        return load_spacegroup(all_magnetic_spacegroups[idx])
    except ValueError:
        close_match = difflib.get_close_matches(msg_name, magnetic_spacegroup_names)
        print('Spacegroup: %s not in list' % msg_name)
        print('Perhaps you meant one of these: %s' % (', '.join(close_match)))
        return None


