"""
Spacegroup Classes
"""

from .general_functions import gen_sym_pos, gen_sym_mat, gen_sym_moment


class SpaceGroup:
    """
    Spacegroup class
    """
    def __init__(self, sg_dict):
        self.sg = sg_dict

        self.general_positions = sg_dict['general positions']
        self.positions_general = sg_dict['general positions']
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

    def info(self):
        """Return str of spacegroup properties"""
        outstr = 'Spacegroup: %s : %s\n' % (self.spacegroup_number, self.spacegroup_name)
        sg = self.sg
        outstr += '%24s  :  %s\n' % ('space group name html', sg['space group name html'])
        outstr += '%24s  :  %s\n' % ('web address generator', sg['web address generator'])
        outstr += '%24s  :  %s\n' % ('web address site check', sg['web address site check'])
        outstr += '%24s  :  %s\n' % ('web address wyckoff', sg['web address wyckoff'])
        outstr += '%24s  :  %s\n' % ('general positions', sg['general positions'])
        outstr += '%24s  :  %s\n' % ('positions centring', sg['positions centring'])
        outstr += '%24s  :  %s\n' % ('positions coordinates', sg['positions coordinates'])
        outstr += '%24s  :  %s\n' % ('positions multiplicity', sg['positions multiplicity'])
        outstr += '%24s  :  %s\n' % ('positions symmetry', sg['positions symmetry'])
        outstr += '%24s  :  %s\n' % ('positions wyckoff letter', sg['positions wyckoff letter'])
        outstr += '%24s  :  %s\n' % ('magnetic space groups', sg['magnetic space groups'])
        outstr += '%24s  :  %s\n' % ('subgroup index', sg['subgroup index'])
        outstr += '%24s  :  %s\n' % ('subgroup name', sg['subgroup name'])
        outstr += '%24s  :  %s\n' % ('subgroup number', sg['subgroup number'])
        outstr += '%24s  :  %s\n' % ('subgroup type', sg['subgroup type'])
        return outstr

    def calc_symmetric_positions(self, x, y, z):
        """
        Return list of symmetric postions to (x, y, z)
        :param x: float
        :param y: float
        :param z: flaot
        :return: list [[x,y,z]]
        """
        return gen_sym_pos(self.general_positions, x, y, z)

    def calc_matrices(self):
        """
        Return list of matrices for symmetry operations
        :return: list
        """
        return gen_sym_mat(self.general_positions)

    def __repr__(self):
        fmt = 'SpaceGroup(%s: %s, Npos: %d)'
        return fmt % (self.spacegroup_number, self.spacegroup_name, len(self.general_positions))


class SpaceGroupMagnetic:
    """
    Magnetic Spacegroup class
    """
    def __init__(self, msg_dict):
        self.sg = self.msg = msg_dict

        self.operators_general = msg_dict['operators general']
        self.operators_magnetic = msg_dict['operators magnetic']
        self.operators_time = msg_dict['operators time']
        self.parent_number = msg_dict['parent number']
        self.positions_general = msg_dict['positions general']
        self.general_positions = msg_dict['positions general']
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

    def info(self):
        """Return str of spacegroup properties"""
        outstr = 'Magnetic Spacegroup: %s : %s\n' % (self.spacegroup_number, self.spacegroup_name)
        msg = self.sg
        outstr += '%24s  :  %s\n' % ('setting', msg['setting'])
        outstr += '%24s  :  %s\n' % ('type name', msg['type name'])
        outstr += '%24s  :  %s\n' % ('parent number', msg['parent number'])
        outstr += '%24s  :  %s\n' % ('related group', msg['related group'])
        outstr += '%24s  :  %s\n' % ('related name', msg['related name'])
        outstr += '%24s  :  %s\n' % ('related setting', msg['related setting'])
        outstr += '%24s  :  %s\n' % ('positions general', msg['positions general'])
        outstr += '%24s  :  %s\n' % ('positions magnetic', msg['positions magnetic'])
        outstr += '%24s  :  %s\n' % ('operators general', msg['operators general'])
        outstr += '%24s  :  %s\n' % ('operators magnetic', msg['operators magnetic'])
        outstr += '%24s  :  %s\n' % ('operators time', msg['operators time'])
        outstr += '%24s  :  %s\n' % ('wyckoff position', msg['wyckoff position'])
        outstr += '%24s  :  %s\n' % ('wyckoff representative', msg['wyckoff representative'])
        outstr += '%24s  :  %s\n' % ('wyckoff site symmetry', msg['wyckoff site symmetry'])
        return outstr

    def calc_symmetric_positions(self, x, y, z):
        """
        Return list of symmetric postions to (x, y, z)
        :param x: float
        :param y: float
        :param z: flaot
        :return: list [[x,y,z]]
        """
        return gen_sym_pos(self.general_positions, x, y, z)

    def calc_symmetric_moments(self, x, y, z):
        """
        Return list of symmetric moment directions to (x, y, z)
            - Tranlations not applied
            - time odd operations are inverted
        :param x: float
        :param y: flaot
        :param z: flat
        :return: list [[x,y,z]]
        """
        return gen_sym_moment(self.general_positions, x, y, z)

    def calc_matrices(self):
        """
        Return list of matrices for symmetry operations
        :return: list
        """
        return gen_sym_mat(self.general_positions)

    def __repr__(self):
        fmt = 'SpaceGroupMagnetic(%s: %s (Setting:%s, %s, Npos: %d)'
        return fmt % (self.spacegroup_number, self.spacegroup_name,
                      self.setting, self.type_name, len(self.positions_general))
