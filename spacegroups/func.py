"""
Spacegroup functions
"""

import os
import json


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


class SpaceGroup:
    """
    Spacegroup class
    """
    def __init__(self, sg_dict):
        self.sg = sg_dict

        self.general_positions = sg_dict['general positions']
        self.magnetic_spacegroups = sg_dict['magnetic space groups']
        self.positions_centring = sg_dict['positions centring']
        self.positions_coordinates = sg_dict['positions coordinates']
        self.positions_multiplicity = sg_dict['positions multiplicity']
        self.positions_symmetry = sg_dict['positions symmetry']
        self.positions_wyckoff_letter = sg_dict['positions wyckoff letter']
        self.spacegroup_name = sg_dict['space group name']
        self.spacegroup_name_html = sg_dict['space group name html']
        self.spacegroup_number = sg_dict['space group number']
        self.subgroup_index = sg_dict['subgroup index']
        self.subgroup_name = sg_dict['subgroup name']
        self.subgroup_number = sg_dict['subgroup number']
        self.subgroup_type = sg_dict['subgroup type']
        self.webaddress_generator = sg_dict['web address generator']
        self.webaddress_sitecheck = sg_dict['web address site check']
        self.webaddress_wyckoff = sg_dict['web address wyckoff']

    def __repr__(self):
        fmt = 'SpaceGroup(%s: %s, Npos: %d)'
        return fmt % (self.spacegroup_number, self.spacegroup_name, len(self.general_positions))


class SpaceGroupMagnetic:
    """
    Magnetic Spacegroup class
    """
    def __init__(self, msg_dict):
        self.sg = msg_dict

        self.operators_general = msg_dict['operators general']
        self.operators_magnetic = msg_dict['operators magnetic']
        self.operators_time = msg_dict['operators time']
        self.parent_number = msg_dict['parent number']
        self.positions_general = msg_dict['positions general']
        self.positions_magnetic = msg_dict['positions magnetic']
        self.related_group = msg_dict['related group']
        self.related_name = msg_dict['related name']
        self.related_setting = msg_dict['related setting']
        self.setting = msg_dict['setting']
        self.spacegroup_name = msg_dict['space group name']
        self.spacegroup_number = msg_dict['space group number']
        self.type_name = msg_dict['type name']
        self.wyckoff_position = msg_dict['wyckoff position']
        self.wyckoff_representative = msg_dict['wyckoff representative']
        self.wyckoff_site_symmetry = msg_dict['wyckoff site symmetry']

    def __repr__(self):
        fmt = 'SpaceGroupMagnetic(%s: %s (Setting:%s, %s, Npos: %d)'
        return fmt % (self.spacegroup_number, self.spacegroup_name,
                      self.setting, self.type_name, len(self.positions_general))
