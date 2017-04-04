"""
Messages
    - 

D. Kotlyar

Functions:
    - perturb_bumat: 
    - 

"""

import os
from os.path import exists

#import xsboa.messages as messages

import re

inpfile='../testing/SINP019.bumat0'
outfile='../testing/brached.bumat0'
mat='fuel1p80001r1p80001r1'
temp='943.57'
prf='.06c'

def perturbbumat(inpfile,outfile,mat,temp,prf):
    '''
    Perturb the _bumat# file to include the brached conditions
    :param inpfile: _bumat input file
    :param outfile: perturbed file
    :param mat: The name of the burnable material (str)
    :param temp: The temperature in Kelvins (str)
    :param prf: The prefix for cross-sections, e.g. '.09c' (str)
    :return: 
    '''

    args = {'verbose': True, 'output': None}
    validPrfTypes = ('.03c', '.06c', '.09c', '.12c', '.15c', '.18c')


    if not os.path.exists(inpfile):
        messages.warn('File {} does not exist and cannot be branched'.format(os.path.join(os.getcwd(), inpfile)),
                      'perturb_bumat()', args)
        return -1

    if prf not in validPrfTypes:
        messages.warn('Prefix specifier {0} not supported at this time. Please use one of the following: {1}\n'
                      .format(prf, ' '.join(validPrfTypes)), 'perturb_bumat()', args)
        return -2

    if float(temp) < 300:
        messages.warn('The value of the temperature is too low {0}. Please use values above 300 Kelvin \n'
                      .format(prf), 'perturb_bumat()', args)
        return -2

    messages.status('Processing file {}'.format(inpfile), args)


    fid_in  = open(inpfile,'r') # original _bumat file
    fid_out = open(outfile,'w') # modified (perturbed) _bumatfile

    while True:
        tline=fid_in.readline() # read every line in the _bumat file
        if tline == '': # checks end-of-file
            break

        if (mat in tline)&('mat' in tline): # material found
            ND = 'sum'
            condV = False
            vars_tline = tline.rstrip(' ') # separate the variables in the line
            for idx in range(len(vars_tline)): # loop over the variables in the list
                if vars_tline[idx] == 'vol': # Register the volume of the material, if given
                    condV = True
                    vol = vars_tline[idx+1]

                if vars_tline[idx] == mat: # Register the nuclide density of the material
                    ND = vars_tline[idx+1]

            if temp == []:
                tline = 'mat   ' + '  ' + mat + '  ' + ND + '  '
            else:
                tline = 'mat   ' + '  ' + mat + '  ' + ND + '  ' + '  temp  ' + temp

            if condV == True:
                tline = tline + '  vol '+vol   # print the registered volume


        fid_out.writelines(tline)


    fid_in.close()
    fid_out.close()



