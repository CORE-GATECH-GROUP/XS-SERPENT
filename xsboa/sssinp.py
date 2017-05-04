"""
sssinp

Andrew Johnson

Module for performing operations on SERPENT input file such as 

#. Obtaining cross section parameters
#. Writing branched outputs

Classes: 

"""
import itertools
import os.path as path
from string import ascii_letters

import xsboa.messages as xbmessages
from xsboa.readparam import readparam


class SSSInput(object):
    """SERPENT input file
    
    Arguments
    
    Attributes
    ----------
    
    ``branches``: Dictionary where each key is the name of a branch
    with a vector of perturbed values as value, e.g. ::
    
        {'mod_dens': (['water'], 'mdens', [6.0E-2, 6.5E-2]),
        ... }
    
    """

    def __init__(self, iname: str, rtype: str, **kwargs):
        self.iname = iname
        params = readparam(iname, args=kwargs)
        if params[0][0] is False:
            xbmessages.fatal('Could not open file {}'.format(iname),
                             'SSSInput()', kwargs)
        self.paramloc = params[0]
        self.nominal = params[1]
        self.branches = params[2]
        self.bnames = sorted(list(self.branches.keys()))
        self.b_combs = self.branch_combinations()

        self.exe = params[3]
        self.vars = params[4]
        self.univs = params[5]
        if rtype == 'p':
            pass
            self.children = [iname + '_' + bb for bb in self.branches]
            self.children.append(iname + '_nom')
        elif rtype in ('c', 'x'):
            self.children = []
            for _pert in self.b_combs:
                b_params = dict()
                for _nn, _xx in enumerate(_pert):
                    for _matl in self.branches[self.bnames[_nn]][0]:
                        if _matl not in b_params:
                            b_params[_matl] = []
                        b_params[_matl].append(
                            (self.branches[self.bnames[_nn]][1],
                             self.branches[self.bnames[_nn]][2][_xx]))
                pfile = self.make_file(_pert, b_params)
                self.children.append((_pert, pfile))

    def __str__(self):
        return "SERPENT input file - {0}".format(self.iname)

    def make_file(self, pert_comb: (tuple, list), branchparam: dict):
        """Create a branched input file after making desired edits.
        
        :param pert_comb: Tuple of integers corresponding to this
        unique file
        :param branchparam:  dictionary with the perturbed branched
        parameters as keys and then conditions as values
        :return: name of new file
        """
        suffix = ''.join([aa + str(ll) for aa, ll in zip(
            ascii_letters[:len(pert_comb)], pert_comb
        )])
        newfile = self.iname[:self.iname.find('.')] + '_' + suffix
        if self.iname.find('.') != -1:
            newfile += self.iname[self.iname.find('.'):]
        with open(newfile, 'w') as _nn:
            _nn.write('/* xsboa: {0}\n'.format(self.iname))
            _nn.write('\n'.join(['{0}: {1}'.format(val, branchparam[val])
                                 for val in branchparam]))
            _nn.write('\n*/\n')
            # todo make all the necessary edits to the output file as we go

        return newfile

    def branch_combinations(self):
        """Class method to obtain branch combination generator"""
        return branch_combinations(self.branches, self.bnames)


def branch_combinations(branch_dict: dict, bnames: (list, tuple)):
    """Create a generator of the various perturbation branches.
    
    :param branch_dict: Dictionary of branch states 
    :param bnames: Optional - name of branches [keys in ``branch_dict``
    
    :return: Generator yielding branch states
     
    Returned generator yields a tuple for each execution.
    The vales in the tuple correspond to the specific perturbed 
    value in each of the branches. ::
        
        branches = {'m_dens': (['water'], 'mdens', [0.06, 0.07]),
                        'f_temp': ('fuel'], 'temp', [800., 1000., 1300.])}
        bnames = ('m_dens', 'f_temp')
        b_comps = branch_combinations(branches, bnames)
        
        for pert in b_comps:
            print(pert)
            for nn, xx in enumerate(pert):
                print('  ', self.branches[self.bnames[nn]],
                      self.branches[self.bnames[nn]][2][xx])
        
        # prints
        (0, 0)
         'm_dens', 0.06
         'f_temp', 800.
        (0, 1)
         'm_dens', 0.07
         'f_temp', 800.
        (1, 0)
         'm_dens', 0.06
         'f_temp', 1000.
         ...
         (2, 1)
          'm_dens', 0.07
          'f_temp', 1300.
    """

    nvals = [len(branch_dict[_bb][2]) for _bb in bnames]
    return itertools.product(*[range(_vv) for _vv in nvals])


if __name__ == '__main__':
    # tfile = path.join('testing', 'uo2assem', 'uo2assem.txt')
    tfile = path.join('testing', 'uo2mox', 'uo2mox.txt')
    test = SSSInput(tfile, 'c')
    pert = None
    for pert in test.b_combs:
        print(pert)
        for nn, xx in enumerate(pert):
            print(' ', test.bnames[nn], test.branches[test.bnames[nn]][2][xx])
    for pp, ff in test.children:
        print(pp, ff)
