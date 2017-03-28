"""

res_scaper
    - Scrape SERPENT _res.m files for specific variables at specific burnup points 

A. Johnson
  
"""
from os.path import exists
from datetime import datetime
import numpy as np
import messages
from mat2py import vec2list

validBurntypes = ('BURN_STEP', 'BURNUP', 'DAYS')


class SerpResFile(object):
    """SERPENT _res.m output object
    
    Class for extracting, printing, and (eventually) plotting group constant values 
        from SERPENT output files 
    """  # TODO: Fill this out better

    def __init__(self, resfile: str, process: bool, gculist: list, varlist: list, burnlist: list, burntype: str):
        """
        
        :param resfile: 
        :param process: 
        :param gculist:
        :param varlist: 
        :param burnlist: 
        :param burntype: 
        """
        self.resfile = resfile
        self.gculist = gculist
        self.varlist = varlist
        self.burnlist = burnlist
        self.burntype = burntype
        if process:
            self.gcuvals = res_scraper(resfile, gculist, varlist, burnlist, burntype)
            self.time = str(datetime.now())
        else:
            self.time = None
            self.gcuvals = {gcu: None for gcu in gculist}
            # purpose of this section is to define the variables here, but then have a method later on
            # that can write the contents of this file in a syntax for easy rereading without reprocessing
            # i.e. having a file that declares an instance of this class, with a given list of variables, but then
            # defines those variables directly
            # time should be read in from external file and written everytime the output files are written


def res_scraper(resfile, gculist, varlist, burnlist, burntype):
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

    gcu_vals = {gcu: None for gcu in gculist}

    with open(resfile, 'r') as res:
        line = res.readline()
        # find the correct burnup point
        while line[:len(burntype)] != burntype:
            line = res.readline()
