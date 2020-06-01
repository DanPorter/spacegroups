"""
General functions
"""


def invert_sym(sym_op):
    """
    Invert the sign of the given symmetry operation
    Usage:
      new_op = invert_sym(sym_op)
      sym_op = str symmetry operation e.g. 'x,y,z'
      new_op = inverted symmetry

    From Dans_Diffraction.functions_crystallography

    E.G.
      new_op = invert_sym('x,y,z')
      >> new_op = '-x,-y,-z'
    """
    sym_op = sym_op.lower()
    new_op = sym_op.replace('x', '-x').replace('y', '-y').replace('z', '-z').replace('--', '+').replace('+-', '-')
    return new_op


def gen_sym_pos(sym_ops, x, y, z):
    """
    Generate positions from symmetry operations
    Usage:
      uvw = gen_sym_pos(sym_ops,x,y,z)
      sym_ops = [n*'x,y,z'] array of string symmetry operations
      x,y,z = fractional coordinates of atomic posiiton to be modified by symmetry
      uvw = [[nx3]] array of symmetry defined factional coordinates [u,v,w]

    From Dans_Diffraction.functions_crystallography

    E.G.
      uvw = gen_sym_pos(['x,y,z','y,-x,z+1/2'],0.1,0.2,0.3)
      uvw >> [[0.1,0.2,0.3] , [0.2,-0.1,0.8]]
    """
    uvw = []
    for n in range(len(sym_ops)):
        sym = sym_ops[n]
        sym = sym.lower()
        # Evaluate string symmetry operation in terms of x,y,z
        sym = sym.replace('/', './')
        sym = sym.strip('\"\'')
        out = list(eval(sym, {'x': x, 'y': y, 'z': z})[:3])
        uvw += [out]
    return uvw


def gen_sym_moment(sym_ops, x, y, z):
    """
    Generate magnetic moments from symmetry operations
     - doesn't apply translations
     - inverts time odd operations
    Usage:
      mom = gen_sym_moment(sym_ops,x,y,z)
      sym_ops = n*['x,y,z'] array of string symmetry operations
      x,y,z = fractional coordinates of atomic posiiton to be modified by symmetry
      mom = [[nx3]] array of symmetry defined moment directions [x,y,z]

    E.G.
      xyz = gen_sym_moment(['x,y,z, +1','y,-x,z+1/2, -1'],0.1,0.2,0.3)
      xyz >> [[0.1, 0.2, 0.3] , [-0.2, 0.1, -0.3]]
    """

    translations = ['+1/2', '+1/3', '+1/4', '+1/6', '+2/3', '+3/4', '+5/6']

    uvw = []
    for sym in sym_ops:
        sym = sym.lower()
        # Evaluate string symmetry operation in terms of x,y,z
        for t in translations:
            sym = sym.replace(t, '')
        sym = sym.strip('\"\'')

        if sym[-2:] == '-1':
            sym = invert_sym(sym)

        out = list(eval(sym, {'x': x, 'y': y, 'z': z})[:3])
        uvw += [out]
    return uvw


def gen_sym_mat(sym_ops):
    """
     Generate transformation matrix from symmetry operation
     Currently very ugly but it seems to work

     From Dans_Diffraction.functions_crystallography

     sym_mat = gen_syn_mat(['x,y,z','y,-x,z+1/2'])
     sym_mat[0] = [[ 1.,  0.,  0.,  0.],
                   [ 0.,  1.,  0.,  0.],
                   [ 0.,  0.,  1.,  0.]])
     sym_mat[1] = [[ 0. ,  1. ,  0. ,  0. ],
                   [-1. ,  0. ,  0. ,  0. ],
                   [ 0. ,  0. ,  1. ,  0.5]]
    """
    sym_mat = []
    for sym in sym_ops:
        sym = sym.lower()
        ops = sym.split(',')
        mat = [[0., 0., 0., 0.],
               [0., 0., 0., 0.],
               [0., 0., 0., 0.]]

        for n in range(len(ops)):
            op = ops[n]
            op = op.strip('\"\'')
            if 'x' in op:
                mat[n][0] = 1
            if '-x' in op:
                mat[n][0] = -1
            if 'y' in op:
                mat[n][1] = 1
            if '-y' in op:
                mat[n][1] = -1
            if 'z' in op:
                mat[n][2] = 1
            if '-z' in op:
                mat[n][2] = -1

            # remove these parts
            op = op.replace('-x', '').replace('x', '')
            op = op.replace('-y', '').replace('y', '')
            op = op.replace('-z', '').replace('z', '')
            op = op.replace('+', '')
            op = op.replace('/', './')  # Allow float division

            if len(op.strip()) > 0:
                mat[n][3] = eval(op)
        sym_mat += [mat]
    return sym_mat
