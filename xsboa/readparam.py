"""
readparam
    - retrieve relevant parameters from data block

Andrew Johnson
    
Functions:

    #. readparam(): take in the original SERPENT input file with data 
        block, and return important parameters
    #. paramsplit(): take in a split parameter line and return a 
    dictionary with parameter: value pairs
    #. test_exe(): Make sure execution string is valid

Usage
-----
    
Input file should be a valid SERPENT input file with the data block 
encompased in C/C++ style block comments with xsboa in each line ::

    /* start xsboa .... <data> ... stop xsboa */ 
    /* xsboa ... <data> ... xsboa */

Nominal material properties are given on each line in the form 
``nom <mName> <p0 v0 p1 v1... pN vN>`` where ``pn`` is the specific 
parameter and ``vN`` is the nominal value.
Not all materials must have nominal conditions, nor are nominal 
conditions required.
    
Branches
--------

In order to cover the design space, ``xsboa`` will generate several
inputs corresponding to a full set of perturbations. This is 
accomplished by specifying the distinct material perturbations in the 
main input file with ::

    branch <bname> <mname> <type> <p0> <p1> ...
    branch mod_dens water mdens 6E-02 6.5E-02
    branch fuel_temp fuel temp 800 1000 1100
    branch fuels_temp fuel1,fuel2,fuel3 temp 800 1000 1100
    
This allows branches to be created for each combination of nominal and
branched conditions. Multiple materials can be perturbed at for one
branch by use of comma-separated list.

Parameters that can be perturbed at this point:

    #. temperature 
    #. density (adens or mdens)
    #. void  (specify the void fraction so new density 
    :math:`\rho' = \rho(1-vf)`

Burnup
------

Currently, the user must supply the nominal burnup chain with
bumat files for each burnup branch point. The syntax for burnup is ::

    burn <btype> <bsteps> [keep <keeppoints]
    
In later versions, this string will write a valid ``SERPENT`` burnup 
string to the nominal file, execute burnup calculations, and grab
bumat files corresponding to the points in ``keeppoints`` for burnup
branches.
    
Executing SERPENT
-----------------

The variable ``exe_str`` is a single-entry formattable string that will
be used to initiate the branched ``SERPENT`` calculations, e.g. :: 

    exe_str ~/sss2 {} &
    exe_str ~/ss2 {0} > {0}.o &
    # the following two are invalid
    exe_str ~/sss2 file
    exe_str ~/sss2 {0} -omp {1} > {0}.o
    
Errors will be thrown if using the ``.format`` method does not change
the value of ``exe_str``, or if an ``IndexError`` is raised.

"""
import os

import xsboa.messages as xbmessages


def paramsplit(lsplit: (list, tuple), start_indx: int, lcount: int,
               args: dict):
    """Convert a xsboa parameter line into a dictionary of parameter
     value pairs.
    Starting at the index of the first parameter, the pattern is as 
    follows: ``['p0', 'v0', 'p1', 'v1', ...]``
    Each value v<n> will be converted to float. If not, a fatal error 
    is raised.
    
    :param lsplit: List/tuple of line that has been split
    :param start_indx: Index of the first parameter 
    :param lcount: current location in file (used in fatal error)
    :param args: Argument dictionary
        
        'file': input file
        'output' as key and either None or output file as value
        
    :return: dictionary of {'p0': v0, 'p1': v1, ...}
    """
    params = dict()
    for indx in range(start_indx, len(lsplit), 2):
        try:
            params[lsplit[indx]] = float(lsplit[indx + 1])
        except ValueError:
            xbmessages.fatal(
                'Non-numerical value {} in line {} of file {}'.format(
                    lsplit(indx), lcount, args['file']),
                'readparams() - paramsplit', args)
        except IndexError as ie:
            print(lsplit, start_indx, lcount)
            raise ie
    return params


def test_exe(exe_str: str, args: dict):
    """Two simple tests to make sure ``exe_str`` is valid"""
    msg_str = 'Need single formattable argument for exe_str, ' \
              'not {}'.format(exe_str)
    try:
        if exe_str.format('test') == exe_str:
            xbmessages.fatal(msg_str, 'test_exe()', args)
        return True
    except IndexError:
        xbmessages.fatal(msg_str, 'test_exe()', args)


def readparam(infile: str, args=None):
    """Read the SERPENT template file for xsboa parameters.
    
    :param infile: path to SERPENT input file
    :param args: Additional arguments for printing status and error 
        messagesIf not given, defaults to status updates given and 
        printing to screen
    
    :return: 
        
        #.locs - tuple of start and end indices of data block.
            Note: Will be zero indexed i.e. line 1 is read as line 0
        #. nom_d - dictionary of materials and their nominal conditions.
            None if no nominal conditions given
        #. branch_d - dictionary of branch names with perturbed 
            parameters as values. If a perturbed branch has burnup, 
            then a key ``'burn': <burnstring>`` is added, where 
            ``<burnstring>`` indicates the freeform burnup schedule
        #. exe_str - Formatable string to execute ``SERPENT`` runs. 
            The format argument will be the filename. 
            e.g. ``./sss2 {0} > {0}.o``
        #. var_l: List of variables/keywords to be expanded and then 
            scraped in res_scraper. Will not be used for creation and 
            execution of SERPENT input files. Should not be none for 
            processing. Or else what is the point?
        #. gcu_l: List of universes to extract from _res.m files 
            eventually
            
    For errors:
    
        #. ``locs = (False, -1)`` -> Could not open file
        #. ``locs = (<block start>, -1)`` -> Read through file, but 
            could not find end of xsboa block
        #. ``locs = (True, -2)`` -> Read through file, but could not 
            find start of xsboa block 

    """
    if args is None:
        args = {'verbose': True, 'output': None}

    nom_d = dict()
    branch_d = dict()
    exe_str = ''
    var_l = []
    gcu_l = []

    if not os.path.exists(infile):
        xbmessages.warn('File {} '.format(os.path.join(os.getcwd(), infile) +
                                          'does not exist'),
                        'readparam()', args)
        return (False, -1), nom_d, branch_d, exe_str, var_l, gcu_l

    with open(infile, 'r') as inobj:
        line = inobj.readline()
        lcount = 0
        while line != '':
            if '/*' in line and 'xsboa' in line:
                block_start = lcount
                block_end = -1
                xbmessages.status('Found start of data block - '
                                  'line {}'.format(lcount + 1), args)

                line = inobj.readline()
                lcount += 1
                while 'xsboa' not in line and '*/' not in line:
                    if line.strip() != '':
                        lsplit = line.split()
                        if lsplit[0] == 'nom':
                            nom_d[lsplit[1]] = paramsplit(lsplit, 2,
                                                          lcount + 1, args)
                        elif lsplit[0] == 'burn':
                            nom_d['burn'] = ' '.join(lsplit[1:])
                        elif lsplit[0] == 'exe_str':
                            exe_str = ' '.join(lsplit[1:])

                        elif lsplit[0] == 'var':
                            var_l.extend(lsplit[1:])
                        elif lsplit[0] == 'gcu':
                            gcu_l.extend(lsplit[1:])
                        elif lsplit[0] == 'branch':
                            bvals = [float(bb) for bb in lsplit[4:]]
                            branch_d[lsplit[1]] = (lsplit[2].split(','),
                                                   lsplit[3], bvals)
                    if line == '':
                        return (block_start, block_end), nom_d, branch_d, \
                               exe_str, var_l, gcu_l
                    line = inobj.readline()
                    lcount += 1

                block_end = lcount
                xbmessages.status('  done', args)
                return (block_start, block_end), nom_d, branch_d, exe_str, \
                       var_l, gcu_l
            line = inobj.readline()
            lcount += 1
        return (True, -2), nom_d, branch_d, exe_str, var_l, gcu_l


# testing
if __name__ == '__main__':
    locs, nom, branches, exe, var_lst, gcu = \
        readparam(os.path.join('testing', 'uo2mox', 'uo2mox.txt'), None)
    print(locs)
    print('--')
    for each in nom:
        print(each, nom[each])
    print('--')
    for branch in branches:
        print(branch, branches[branch])
    print('--\n', exe)
    print('--\n', var_lst)
    print('--\n', gcu)
