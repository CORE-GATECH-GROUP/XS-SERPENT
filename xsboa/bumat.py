"""
Messages
    - 

D. Kotlyar

Functions:
    - perturb_bumat: Modifies the temperature and prefix for a specific material
    - 

"""

import os
from datetime import datetime

import messages as messages


def perturb_bumat(inpfile, outfile, mat, temp, prf, args=None):
    '''
    Perturb the _bumat# file to include the branched conditions (new temperature and prefix)
    :param inpfile: _bumat input file
    :param outfile: the new name of the perturbed file
    :param mat: The name of the burnable material (str)
    :param temp: The temperature in Kelvins (str)
    :param prf: The prefix for cross-sections, e.g. '.09c' (str)
    :return: 
    '''

    validPrfTypes = ('.03c', '.06c', '.09c', '.12c', '.15c', '.18c')
    validTmpTypes = (300, 600, 900, 1200, 1500, 1800)

    if args is None:
        args = {'verbose': True, 'output': None}

    if args is None:
        args = {'verbose': True, 'output': None}

    if not os.path.exists(inpfile):
        messages.warn('File {} does not exist and cannot be scraped'.format(os.path.join(os.getcwd(), inpfile)),
                      'perturb_bumat()', args)
        return -1

    if prf not in validPrfTypes:
        messages.warn('Prefix specifier {0} not supported at this time. Please use one of the following: {1}\n'
                      .format(prf, ' '.join(validPrfTypes)), 'perturb_bumat()', args)
        return -1

    if (float(temp) < validTmpTypes[0]) | (float(temp) > (validTmpTypes[len(validTmpTypes)-1])):
        messages.warn('The temperature [K] for material {0} is not in the range {1}-{2}. \n'
                      .format(mat, validTmpTypes[0], validTmpTypes[(len(validTmpTypes)-1)]), 'perturb_bumat()', args)
        return -2

    if float(temp)< validTmpTypes[validPrfTypes.index(prf)]:
        messages.warn('The temperature [K] for material {0} and prefix {1} must be above {2}. \n'
                      .format(mat, prf, validTmpTypes[validPrfTypes.index(prf)]), 'perturb_bumat()', args)
        return -2

    messages.status('Processing file {}'.format(inpfile), args)


    import re


    fid_in = open(inpfile, 'r')  # original _bumat file
    fid_out = open(outfile, 'w')  # modified (perturbed) _bumatfile

    flag_eof = 0

    while True:

        if flag_eof == 1:  # end-of-file indicator
            break
        tline = fid_in.readline()  # read every line in the _bumat file
        if tline == '':  # checks end-of-file
            break

        if (mat in tline) & ('mat' in tline):  # material found
            ND = 'sum'
            condV = False
            vars_tline = tline.split()  # separate the variables in the line
            for idx in range(len(vars_tline)):  # loop over the variables in the list
                if vars_tline[idx] == 'vol':  # Register the volume of the material, if given
                    condV = True
                    vol = vars_tline[idx + 1]

                if vars_tline[idx] == mat:  # Register the nuclide density of the material
                    ND = vars_tline[idx + 1]

            if temp == []:
                tline = 'mat   ' + '  ' + mat + '  ' + ND + '  '
            else:
                tline = 'mat   ' + '  ' + mat + '  ' + ND + '  ' + '  tmp  ' + temp

            if condV == True:
                tline = tline + '  vol ' + vol  # print the registered volume

            tline = tline + '\n'
            fid_out.writelines(tline)  # write the new mat line

            # A loop over the nuclides
            while True:
                tline = fid_in.readline()
                if tline == '':  # checks end-of-file
                    flag_eof = 1
                    break
                if tline == '\n':  # empty line
                    break
                idxPrf = re.search('\.\d+c', tline)  # identify the prefix

                if idxPrf != None:  # prefix found, e.g. 8016.09c 4.6E-02
                    tline = tline.replace(tline[idxPrf.end() - 4:idxPrf.end()], prf)

                fid_out.writelines(tline)

        fid_out.writelines(tline)

    fid_in.close()
    fid_out.close()


# testing
inpfile = '../testing/SINP020.bumat0'
outfile = '../testing/brached.bumat0'
mat = 'fuel2p80001r1'
temp = '1043.57'
prf = '.09c'
perturb_bumat(inpfile, outfile, mat, temp, prf, args=None)




