"""
spacegroups
Display spacegroup and magnetic spacegroup properties

Usage:
    ***From Terminal***
    cd /location/of/file
    ipython -m spacegroups 194 P63/mmc 61.433

By Dan Porter, PhD
Diamond
2020
"""
if __name__ == '__main__':

    import sys
    import spacegroups
    from spacegroups import load_spacegroup, find_spacegroup, find_magnetic_spacegroup

    print('\nspacegroups version %s, %s\n By Dan Porter, Diamond Light Source Ltd.' % (
        spacegroups.__version__, spacegroups.__date__))
    print('Added to workspace: spacegroups, load_spacegroup, find_spacegroup, find_magnetic_spacegroup')

    for arg in sys.argv:
        try:
            sg = load_spacegroup(arg)
        except KeyError:
            sg = find_spacegroup(arg)
        if sg is not None:
            print(sg.info())
