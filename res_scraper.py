"""

res_scaper
    - Scrape SERPENT _res.m files for specific variables at specific burnup points 

A. Johnson
  
"""
from os.path import exists
import numpy as np
import messages
from mat2py import vec2list

validBurntypes = ('BURN_STEP', 'BURNUP', 'DAYS')


def res_scraper(resfile, gculist, varlist, burnlist, burntype, nfg=None):
    """
    Parse the _res.m file and return a dictionary where the keys are specified ` constant universes
    and the values are matrices of the desired variables at the desired points.
    Matrix returned has the following syntax: gcu_vals[v, b, e] where v is the index in varlist for this variable 
    (i.e. INF_TOT, B1_FLX, etc), b is the index in burnlist that corresponds to the burnup step at this point, 
    and e is the energy group (highest to lowest).
    :param resfile: Output file to be scraped.
    :param gculist: List of group constant universes to be returned
    :param varlist: List of variables the user desires to return
    :param burnlist: List of burnup points (can be given in days of in burnup as specified by burntype)
    :param burntype: One of three values indicating what burnup values to look for
        BURN_STEP: unitless burnup point, BURNUP: value of burnup in MWd/kgU, BURN_DAYS: day in the burnup cycle
    :param nfg: Number of collapsed energy groups returned. Also the length of the group constant vectors
        If given, the matrices to be returned can be generated immediately. Otherwise, must wait until the number 
        of energy groups can be determined
    :return: gcu_vals dictionary where the keys are strings corresponding to the group constant universes, and the 
        corresponding values are the matrices gcu_vals[v, b, e]
        For errors:
            -1: resfile does not exist
            -2: incorrect burntype
    """
    if not exists(resfile):
        messages.warn('File {} does not exist and cannot be scraped'.format(resfile), 'res_scraper()')
        return -1

    if burntype not in validBurntypes:
        messages.warn('Burntype specifier {0} not supported at this time. Please use one of the following: {1}\n'
                      .format(burntype, ' '.join(validBurntypes)), 'res_scraper()')
        return -2
    # TODO add some potential error handling for non-positive integer values of nfg

    if nfg is None:
        gcu_vals = {gcu: None for gcu in gculist}
    else:
        gcu_vals = {gcu: np.zeros((len(varlist), len(burnlist), nfg), dtype=float) for gcu in gculist}

    with open(resfile, 'r') as res:
        line = res.readline()
        # find the correct burnup point
        while line[:len(burntype)] != burntype:
            line = res.readline()
