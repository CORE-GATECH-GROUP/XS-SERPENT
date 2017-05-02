"""
Messages
    -

D. Kotlyar

Functions:
    - perturb_mat: the function can modify:
        * the material line;
        * prefix of the nuclide densities
        * replace the nuclide density
    - The function can modify only a single material 
"""

import os
import re

#import xsboa.messages as messages
import messages as messages

def perturb_mat(inpfile, outfile, mat, dens, tmp, prf, opt, args=None):
    '''
    Perturb the _bumat# file to include the branched conditions (new temperature and prefix)
    :param inpfile: _bumat input file
    :param outfile: the new name of the perturbed file
    :param mat: The name of the burnable material (str)
    :param dens: The name of the original burnable material (str)
    :param tmp: The temperature in Kelvins (str)
    :param prf: The prefix for cross-sections, e.g. '.09c' (str)
    :param opt: Case option 1)
    :return:
    '''

    # Default matching prefixes and temperatures
    validPrfTypes = ('.03c', '.06c', '.09c', '.12c', '.15c', '.18c')
    validTmpTypes = (300, 600, 900, 1200, 1500, 1800)

    # Thermal scattering libraries for lights water (lwj), heavy water (hwj) and graphite (grj) respectively
    thermsctrlwj = ([(294, 'lwj3.00t'), (324, 'lwj3.01t'), (374, 'lwj3.03t'), (424, 'lwj3.05t'), (474, 'lwj3.07t'),(524, 'lwj3.09t'), (574, 'lwj3.11t'), (624, 'lwj3.13t'), (647, 'lwj3.14t'), (800, 'lwj3.18t'),(1000, 'lwj3.20t')])
    thermsctrhwj = ([(294, 'hwj3.00t'), (324, 'hwj3.01t'), (374, 'hwj3.03t'), (424, 'hwj3.05t'), (474, 'hwj3.07t'),(524, 'hwj3.09t'), (574, 'hwj3.11t'), (644, 'hwj3.14t')])
    thermsctrgrj = ([(294, 'grj3.00t'), (400, 'grj3.04t'), (500, 'grj3.08t'), (600, 'grj3.12t'), (700, 'grj3.16t'),(800, 'grj3.18t'), (1000, 'grj3.20t'), (1200, 'grj3.22t'), (1600, 'grj3.24t'), (1999, 'grj3.26t')])


    if args is None:
        args = {'verbose': True, 'output': None}

    if not os.path.exists(inpfile):
        messages.warn('File {} does not exist and cannot be modified'.format(os.path.join(os.getcwd(), inpfile)),
                      'perturb_mat()', args)
        return -1

    if prf not in validPrfTypes:
        messages.warn('Prefix specifier {0} not supported at this time. Please use one of the following: {1}\n'
                      .format(prf, ' '.join(validPrfTypes)), 'perturb_mat()', args)
        return -2

    if (float(tmp) < validTmpTypes[0]) | (float(tmp) > (validTmpTypes[len(validTmpTypes) - 1])):
        messages.warn('The temperature [K] for material {0} is not in the range {1}-{2}. \n'
                      .format(mat, validTmpTypes[0], validTmpTypes[(len(validTmpTypes) - 1)]), 'perturb_mat()', args)
        return -2


    fid_in = open(inpfile, 'r')  # original file
    fid_out = open(outfile, 'w')  # modified file

    flag_eof = 0

    # Reset variables
    moder = [] # for S(alpha,beta) - thermal scattering
    cond_tmp = 0 # registers the existence of a tmp card

    while ('dens' in opt) | ('temp' in opt):

        if flag_eof == 1:  # end-of-file indicator
            break
        tline = fid_in.readline()  # read every line in the file
        if tline == '':  # checks end-of-file
            break


        if (mat in tline)& ('mat' in tline):  # material found
            vars_tline = tline.split()  # separate the variables in the line
            for idx in range(len(vars_tline)):  # loop over the variables in the list
                if vars_tline[idx] == mat:  # density of the material
                    if dens!= []: # modify the original density
                        vars_tline[idx+1] = dens
                if (tmp != []) & ('tmp' in vars_tline[idx]): # tmp card exists
                    cond_tmp = 1
                    vars_tline[idx+1] = tmp  # upate the temperature
                if vars_tline[idx] == 'moder':
                    moder = vars_tline[idx+1]  # register the scattering material

            if cond_tmp:
                tline = (' '.join(vars_tline)) + ' tmp ' + tmp
            else:
                tline = (' '.join(vars_tline))

            tline = tline + '\n'
            fid_out.writelines(tline)  # write the new mat line

            # A loop over the nuclides
            while ('temp' in opt): # must include temperature perturbation
                tline = fid_in.readline()
                if tline == '':  # checks end-of-file
                    flag_eof = 1
                    break
                if tline == '\n':  # empty line
                    fid_out.writelines('\n')
                    flag_eof = 1
                    break
                idxPrf = re.search('\.\d+c', tline)  # identify the prefix

                if idxPrf != None:  # prefix found, e.g. 8016.09c 4.6E-02
                    tline = tline.replace(tline[idxPrf.end() - 4:idxPrf.end()], prf)
                    fid_out.writelines(tline)
                else:
                    fid_out.writelines('\n')
                    break



    fid_in.close()
    fid_out.close()

    # update the temperature of moder S(alpha,beta) material if such exists
    # open the file again search for this material and replace the temperature
    if (moder != []) & (tmp != []):
        fid_out = open(outfile, 'r')
        tlines = fid_out.readlines()
        fid_out.close()
        scttherm = []
        for tline in tlines:
            if ('therm' in tline) & (moder in tline):
                if 'lwj' in tline: # obtain the nearest (temperature-wise) library
                    for itmp in range(len(thermsctrlwj)):
                        if (thermsctrlwj[itmp][0]>float(tmp)):
                            if itmp ==0:
                                 scttherm = thermsctrlwj[itmp][1]
                            elif (thermsctrlwj[itmp][0] - float(tmp))>(float(tmp) - thermsctrlwj[itmp-1][0]):
                                 scttherm = thermsctrlwj[itmp-1][1]
                            else:
                                 scttherm = thermsctrlwj[itmp][1]
                            break
                if 'hwj' in tline: # obtain the nearest (temperature-wise) library
                    for itmp in range(len(thermsctrhwj)):
                        if (thermsctrhwj[itmp][0]>float(tmp)):
                            if itmp ==0:
                                 scttherm = thermsctrhwj[itmp][1]
                            elif (thermsctrhwj[itmp][0] - float(tmp))>(float(tmp) - thermsctrhwj[itmp-1][0]):
                                 scttherm = thermsctrhwj[itmp-1][1]
                            else:
                                 scttherm = thermsctrhwj[itmp][1]
                            break
                if 'grj' in tline: # obtain the nearest (temperature-wise) library
                    for itmp in range(len(thermsctrgrj)):
                        if (thermsctrgrj[itmp][0]>float(tmp)):
                            if itmp ==0:
                                 scttherm = thermsctrgrj[itmp][1]
                            elif (thermsctrgrj[itmp][0] - float(tmp))>(float(tmp) - thermsctrgrj[itmp-1][0]):
                                 scttherm = thermsctrgrj[itmp-1][1]
                            else:
                                 scttherm = thermsctrgrj[itmp][1]
                            break
            if scttherm!=[]:
                tline = 'therm moder ' + scttherm
        fid_out.writelines(tline)
    fid_out.close()


    # if everything is ok
    return 0


# ----------------------------------------------------------------------
#                        testing
# ----------------------------------------------------------------------
inpfile = '../testing/uo2material'
outfile = '../testing/waterperturb'

mat='water'
dens='-0.54321'
tmp='666'
prf='.07c'
opt='temperature, density'

perturb_mat(inpfile, outfile, mat, dens, tmp, prf, opt)
a=1

