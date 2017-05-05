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
import xsboa.scraper as scraper
from xsboa.readparam import readparam


class SSSInput(object):
    """SERPENT input file.
    
    Arguments
    ---------
    
        #. ``iname``: Name of the input file
        #. ``rtype``: string character indicating to *c*reate input 
            files, create and e*x*ecute each input file, or *p*rocess 
            the  group constant data from ``_res.m`` files
    
    Attributes
    ----------
    
        #. ``iname``: Main input file
        #. ``paramloc``: Tuple indicating the start and end of the 
            ``xsboa`` data block - zero indexed
        #. ``nominal``: Dictionary of nominal conditions. Can be 
        ``None``.
        #. ``branches``: Dictionary where each key is the name of a 
            branch with a vector of perturbed values as value, e.g. ::
        
                {'mod_dens': (['water'], 'mdens', [6.0E-2, 6.5E-2]),
                ... }
                
        #. ``bnames``: Sorted list of the names of each branch. Used to
            keep track of perturbed parameters, and maybe some output
        #. ``b_combs``: Generator that yields combinations of indexes 
            for each branched value. See ``branch_combinations()`` for
            a more detailed description
        #. ``exe``: Formattable string that takes one argument [file 
            name] and will be used to execute all the ``SERPENT`` runs
        #. ``vars``: Variables to scrape from the ``_res.m`` files
        #. ``univs``: Universes to look for in the ``_res.m`` files
        #. ``children``: Names of each branched file
    
    """

    def __init__(self, iname: str, rtype: str, nomfile=None, **kwargs):
        self.iname = iname
        params = readparam(iname, args=kwargs)
        if params[0][0] is False:
            xbmessages.fatal('Could not open file {}'.format(iname),
                             'SSSInput()', kwargs)
        self.paramloc = params[0]
        self.nominal = params[1]
        self.branches = params[2]
        if self.nominal is not None:
            self.update_branches()

        self.bnames = sorted(list(self.branches.keys()))
        self.b_combs = self.branch_combinations()

        self.exe = params[3]
        self.vars = scraper.expand_res_kwords(params[4], args=kwargs)
        self.univs = params[5]

        if nomfile is not None:
            self.nomfile = nomfile
        else:
            self.nomfile = self.iname

        # generate the list of branched files
        self.children = []
        numfiles = 0
        for _pert in self.b_combs:
            b_params = self.getpert_params(_pert)
            if self.check_nompert(b_params):
                # all material properties match the nominal conditions
                self.children.append((_pert, self.nomfile))
            else:
                pfile = self.make_file(_pert, b_params, rtype)
                numfiles += 1
                self.children.append((_pert, pfile))

        if rtype in ('c', 'x'):
            xbmessages.status(
                '\nCreated {} branched input files'.format(numfiles), kwargs)
            xbmessages.status('Len children: {}'.format(len(self.children)),
                              kwargs)

    def getpert_params(self, pert):
        """Shortcut to get the branch parameters for a given perturbation.
        
        See getpert_params() for more detail
        """
        return getpert_params(pert, self.branches, self.bnames)

    def update_branches(self):
        """Add the nominal conditions to the branching dictionary."""
        for branch in self.branches:
            for nmatl in self.nominal:
                if nmatl in self.branches[branch][0]:
                    for val in self.nominal[nmatl]:
                        if val == self.branches[branch][1]:
                            if self.nominal[nmatl][val] not in \
                                    self.branches[branch][2]:
                                self.branches[branch][2].insert(
                                    0, self.nominal[nmatl][val])

    def check_nompert(self, _bparams):
        """See if this specific perturbation set matches the nominal case.
        
        :param _bparams: Dictionary of ``matl: [(p0, v0), (p1, v1), ...
        ]`` pairs corresponding to this specific branch.
        
        :return: True if the material properties match the nominal 
            conditions specified in self.nom"""

        for _bmatl in _bparams:
            if _bmatl not in self.nominal or \
                    (_bmatl in self.nominal and
                             self.nominal[_bmatl] != dict(_bparams[_bmatl])):
                return False
        return True

    def __str__(self):
        return "SERPENT input file - {0}".format(self.iname)

    def make_file(self, pert_comb: (tuple, list), branchparam: dict, rtype: str):
        """Create a branched input file after making desired edits.
        
        :param pert_comb: Tuple of integers corresponding to this
        unique file
        :param branchparam:  dictionary with the perturbed branched
        parameters as keys and then conditions as values
        :param rtype: single character string indicating if just
        creating of processing. If processing, don't make the file, 
        just return the file name.
        Also supports 'd' for dry run (just return file name)
        :return: name of new file
        """
        suffix = ''.join([aa + str(ll) for aa, ll in zip(
            ascii_letters[:len(pert_comb)], pert_comb
        )])
        newfile = self.iname[:self.iname.find('.')] + '_' + suffix
        if self.iname.find('.') != -1:
            newfile += self.iname[self.iname.find('.'):]

        if rtype in ('d', 'p'):
            return newfile

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


def getpert_params(pert: (tuple, list), branches: dict,
                   bnames: (list, tuple)):
    """Get the specific material properties for this perturbation set.
    
    :param pert: Vector of integers where each index corresponds to a 
    specific branch name, and the items correspond to the values of 
    those material perturbations
    :param branches: Dictionary of branches with keys as branch names
    and values as tuples/lists of material names, perturbation types, 
    and sequence of values
    :param bnames: Names of each of the branches. Best to use
    ``sorted(list(branches.keys()))`` but left open for generality
    
    :return: dictionary of material - perturbation pairs as 
    ``matl: [(p0, v0), (p1, v1), ... (pN, vN)]`` where each
    ``pi`` is a perturbation type and each ``vi`` is the value 
    to be used (material density, temperature, etc.)
    """

    params = dict()
    for _nn, _xx in enumerate(pert):
        for _matl in branches[bnames[_nn]][0]:
            if _matl not in params:
                params[_matl] = []
            params[_matl].append((branches[bnames[_nn]][1],
                                  branches[bnames[_nn]][2][_xx]))
    return params


if __name__ == '__main__':
    tfile = path.join('testing', 'uo2assem', 'uo2assem.txt')
    # tfile = path.join('testing', 'uo2mox', 'uo2mox.txt')
    test = SSSInput(tfile, 'c')
    print(', '.join(test.bnames))
    for pp, ff in test.children:
        print(pp, ff)
