"""
readparam
    - retrieve relevant parameters from data block

A. Johnson    
Functions:
    - readparam(): take in the original SERPENT input file with data block, and return important parameters
    - paramsplit(): take in a split parameter line and return a dictionary with parameter: value pairs
Notes:
    Input file should be a valid SERPENT input file with the data block encompased in C/C++ style block comments
    with xsboa in each line 
    i.e. /* start xsboa .... <data> ... stop xsboa */ 
    or /* xsboa ... <data> ... xsboa */
    
    Nominal material properties are given on each line in the form 
      nom <mName> <p0 v0 p1 v1... pN vN> where pn is the specific parameter and vN is the nominal value
    Not all materials must have nominal conditions, nor are nominal conditions required.
    
    Branch calculations can be multiline and stop when:
      - the first word in the next line is branch or nom, or 
      - the next line is is empty
    Branch syntax is similar to the nominal condition syntax, where perturbed conditions for each material are given
    on a line.
    ex.
        branch hUO2 UO2 temp 1200
        branch hFuel MOX1 temp 1200
        MOX2 temp 1200
        MOX3 temp 1200
        UO2 temp 1200
    
    Two branches are defined here. The first, named hUO2 indicates that the temperature of material 'UO2' should be 
    changed to 1200K. The second, hFuel, changes the temperature for four materials to 1200K
    
    Parameters that can be perturbed at this point:
        temp, dens (adens or mdens), and void (specify the void fraction so new density $\rho' = \rho(1-vf)$
    
    The nominal burnup schedule, if given, will be the first line with 'burn' as the first word. 
    
"""
import os

import xsboa


def paramsplit(lsplit: (list, tuple), start_indx: int, lcount: int, args: dict):
    """Convert a xsboa parameter line into a dictionary of parameter value pairs
    Starting at the index of the first parameter, the pattern is as follows: 
    ['p0', 'v0', 'p1', 'v1', ...]
    Each value v<n> will be converted to float. If not, a fatal error is raised
    :param lsplit: List/tuple of line that has been split
    :param start_indx: Index of the first parameter 
    :param lcount: current location in file (used in fatal error)
    :param args: Argument dictionary
        - ;file': input file
        - 'output' as key and either None or output file as value
    :return: dictionary of {'p0': v0, 'p1': v1, ...}
    """
    params = {}
    for indx in range(start_indx, len(lsplit), 2):
        try:
            params[lsplit[indx]] = float(lsplit[indx + 1])
        except ValueError:
            xsboa.messages.fatal(
                'Non-numerical value {} in line {} of file {}'.format(lsplit(indx), lcount, args['file']),
                'readparams() - paramsplit', args)
    return params


def readparam(infile: str, args=None):
    """Read the SERPENT template file for xsboa parameters.
    
    :param infile: path to SERPENT input file
    :param args: Additional arguments for printing status and error messages
        If not given, defaults to status updates given and printing to screen
    :return: 
        locs - tuple of start and end indices of data block
            - Note: Will be zero indexed i.e. line 1 is read as line 0
        nom_d - dictionary of materials and their nominal conditions
            None if no nominal conditions given
        branch_d - dictionary of branch names with perturbed parameters as values
            If a perturbed branch has burnup, then a key 'burn': indx is added, where indx points to 
            the string in burnstrings that should be used to build this branches burnup
        burnstrings: list of strings corresponding to burnup values with 
            burnstrings[0] corresponding to the nominal branch (could be empty '')
            all other items are burnup regimes for branch states (could not exist)
        exe_str: Formattable string to call for execution of the SERPENT input files
            ex: './sss2 {} > {}.o'
            
    For errors:
        locs = (False, -1) -> Could not open file
        locs = (<block start>, -1) -> Read through file, but could not find end of xsboa block
        locs = (True, -2) -> Read through file, but could not find start of xsboa block 
    """
    if args is None:
        args = {'verbose': True, 'output': None}

    nom_d = {}
    branch_d = {}
    burnstrings = ['', ]
    exe_str = ''

    if not os.path.exists(infile):
        xsboa.messages.warn('File {} does not exist and cannot be processed'.format(os.path.join(os.getcwd(), infile)),
                            'readparam()', args)
        return (False, -1), nom_d, branch_d, burnstrings, exe_str

    with open(infile, 'r') as inobj:
        line = inobj.readline()
        lcount = 0
        while line != '':
            if '/*' in line and 'xsboa' in line:
                block_start = lcount
                block_end = -1
                xsboa.messages.status('Found start of data block - line {}'.format(lcount + 1), args)

                line = inobj.readline()
                lcount += 1
                while 'xsboa' not in line and '*/' not in line:
                    b_flag = False  #
                    if line.strip() != '':
                        lsplit = line.split()
                        if lsplit[0] == 'nom':
                            nom_d[lsplit[1]] = paramsplit(lsplit, 2, lcount + 1, args)
                        elif lsplit[0] == 'burn':
                            burnstrings[0] = line.strip()
                        elif lsplit[0] == 'exe_str':
                            exe_str = ' '.join(lsplit[1:])
                        elif lsplit[0] == 'branch':
                            branch_name = lsplit[1]
                            branch_d[branch_name] = {lsplit[2]: paramsplit(lsplit, 3, lcount + 1, args)}
                            b_flag = True
                            line = inobj.readline()
                            lcount += 1

                            # check if this branch statement is divided over multiple lines

                            while line.strip() != '' and line.split()[0] not in (
                                    'nom', 'branch', 'exe_str') and '*/' not in line:
                                lsplit = line.split()
                                if lsplit[0] == 'burn':
                                    branch_d[branch_name]['burn'] = len(burnstrings)
                                    burnstrings.append(line.strip())
                                else:
                                    branch_d[branch_name][lsplit[0]] = paramsplit(lsplit, 1, lcount + 1, args)
                                line = inobj.readline()
                                lcount += 1
                    if not b_flag:
                        line = inobj.readline()
                        lcount += 1
                    if line == '':
                        return (block_start, block_end), nom_d, branch_d, burnstrings, exe_str
                block_end = lcount
                xsboa.messages.status('  done', args)
                return (block_start, block_end), nom_d, branch_d, burnstrings, exe_str
            line = inobj.readline()
            lcount += 1
        return (True, -2), nom_d, branch_d, burnstrings, exe_str


# testing
if __name__ == '__main__':
    locs, nom, branch, burns = readparam(os.path.join('testing', 'uo2mox.txt'), None)
