"""

res_scaper
    - Scrape SERPENT _res.m files for specific variables at specific burnup points 

A. Johnson
  
Functions:
    - res_scraper: Parse a SERPENT _res.m output file for desired variables, universes, and burnup points
    - expand_res_kwords: Expand any variable keywords into actual SERPENT variables.
    
Classes:
    - SerpResFile: Class object for stanard SERPENT _res.m outputs files. 
"""
import os
from datetime import datetime

import xsboa.constants as xbcons
import xsboa.messages as xbmessages
from xsboa.mat2py import vec2list


class SerpResFile(object):
    """SERPENT _res.m output object.
    
    Class for extracting, printing, and (eventually) plotting group constant values 
        from SERPENT output files 
    
    Attributes:
        - resfile: Original SERPENT result file
        - gculist: list/tuple of desired universes
        - varlist: list/tuple of desired variables
        - burnlist: list/tuple of desired burnup points
        - burntype: string indicating that the original burnup points were determined by BURN_STEP, BURNUP, or
            BURN_DAYS values from SERPENT
        - gcuvals: dictionary of universes and their values as described in res_scraper docstring
        - time: string indicating the time the 
        
    Methods:
        
    """

    def __init__(self, resfile: str, process: bool, gculist: (tuple, list),
                 varlist: (tuple, list), burnlist: (tuple, list, None),
                 burntype: str, args=None):
        """
        Initialize the attributes by either reading from resfile or initialize
        to None and read from a file (laterimplemetation)
        :param resfile: SERPENT result file (typically ending in _res.m) to be parsed 
        :param process: If True, then read from self.resfile
            Otherwise, initialize the variables and then (eventually) read the 
            variables in from a processed output file
        :param gculist: List of tuple of desired universes to be processed
        :param varlist: List or tuple of desired variables to be processed
        :param burnlist: List or tuple of relevant burnup points to be processed
        :param burntype: Specific type of burnup paramter (i.e. BURN_DAYS) to 
        use as flag for reading burnup and storing burnup points
        :param args: Optional parameter passed to the processing scripts. 
        If None, all warning and error messages in res_scraper will be 
        printed to the stdout. 
        Otherwise, args must be a dictionary with 'verbose': bool and 
        'output': str key-value pairs
        """
        self.resfile = resfile
        self.gculist = gculist
        self.varlist = varlist
        self.burnlist = burnlist
        self.burntype = burntype
        if process:
            self.gcuvals = res_scraper(resfile, gculist, varlist, burnlist, burntype, args)
            self.time = str(datetime.now())
        else:
            self.time = None
            self.gcuvals = {gcu: None for gcu in gculist}
            # purpose of this section is to define the variables here, but then have a method later on
            # that can write the contents of this file in a syntax for easy rereading without reprocessing
            # i.e. having a file that declares an instance of this class, with a given list of variables, but then
            # defines those variables directly
            # time should be read in from external file and written everytime the output files are written


def res_scraper(resfile: str, gculist, varlist, burnlist=None, burntype=None, args=None):
    """Parse resfile for variables from desired universes and burnup points.
    
    Return a dictionary where the keys are specified constant universes
    and the values are matrices of the desired variables at the desired points.
    If ``burnlist`` is not None, but is a list, then only burnup points in
    ``burnlist`` will be returned. For the case there could be no burnup
    points in the file, all values fitting the gcu and varlist parameters
    will be returned

    :param resfile: Output file to be scraped.
    :param gculist: List of group constant universes to be returned
    :param varlist: List of variables the user desires to return
    :param burnlist: List of burnup points (can be given in days of in burnup as specified by burntype)
    :param burntype: One of three values indicating what burnup values to look for
        BURN_STEP: unitless burnup point, BURNUP: value of burnup in MWd/kgU, BURN_DAYS: day in the burnup cycle
    :param args: Optional parameter for output arguments. If None, then creates a dictionary indicating to print
        all status messages to the screen. Otherwise, must be a dictionary with two keys: 'verbose': <bool>, and 
        'output': <str>
        
    :return: gcu_vals dictionary where the keys are strings corresponding to the group constant universes, and the
        corresponding keys and dictionaries of variables. 
        return ::
        
        {'0': {'INF_TOT': [[b0v0, b0u0, b0v1, b0u1, ...], [b1v0, b1u0, b1v1, b1u1, ...]], 
              'INF_NFS': [[b0v0, b0u0, b0v1, b0u1, ...], [b1v0, b1u0, b1v1, b1u1, ...]], ... }
        '1': {'INF_TOT': [[b0v0, b0u0, b0v1, b0u1, ...], [b1v0, b1u0, b1v1, b1u1, ...]], 
              'INF_NFS': [[b0v0, b0u0, b0v1, b0u1, ...], [b1v0, b1u0, b1v1, b1u1, ...]], ... },
        ... } 
        
        where ``b<n>`` indicates the burnup point values ``v<m>``
         and uncertainties ``u<m>`` are pulled from
         
        For errors:
           
            #. -1: resfile does not exist
            #. -2: incorrect burntype
            #. -3: burnlist not iterable
    """

    if args is None:
        args = {'verbose': True, 'output': None}
    elif isinstance(args, dict):
        for arg, deflt in zip(('verbose', 'output', 'quiet'), (True, None, False)):
            if arg not in args:
                args[arg] = deflt

    if not os.path.exists(resfile):
        xbmessages.warn('File {} does not exist and cannot be scraped'.format(os.path.join(os.getcwd(), resfile)),
                        'res_scraper()', args)
        return -1

    if burnlist is not None:
        if burntype not in xbcons.validBurntypes:
            xbmessages.warn('Burntype specifier {0} not supported at this time. Please use one of the following: {1}\n'
                            .format(burntype, ' '.join(xbcons.validBurntypes)), 'res_scraper()', args)
            return -2
        try:
            iter(burnlist)
        except TypeError:
            xbmessages.warn('burnlist {0} not iterable'.format(type(burnlist)) +
                            str(burnlist), 'res_scraper()', args)
            return -3

    xbmessages.status('Processing file {}'.format(resfile), args)

    maxvarlen = max(25, len(max(varlist, key=len)))
    # maximum length of any anticipated SERENT variable

    if burnlist is not None:
        bflag = False
    else:
        bflag = True

    burnloc = 0
    gcu_ = -1

    gcu_vals = {}
    for gcu_ in gculist:
        gcu_vals[gcu_] = {}
        for var in varlist:
            if burnlist is not None:
                gcu_vals[gcu_][var] = [None] * len(burnlist)
            else:
                gcu_vals[gcu_][var] = [None, ]

    uflag = False
    with open(resfile, 'r') as res:
        line = res.readline()
        lcount = 1
        while line != '':  # empty string indicates end of file
            line_var = line[:maxvarlen].rstrip(' ')
            if burnlist is not None and line_var == burntype:
                burnval = float(line.split()[-2])  # specific burnup point
                if burnval in burnlist:
                    bflag = True
                    burnloc = burnlist.index(burnval)
                else:
                    bflag = False
            elif bflag and line_var == 'GC_UNIVERSE_NAME':
                gcu_ = line[line.index("'") + 1:line.index("' ;")]
                if gcu_ in gculist:
                    uflag = True
                else:
                    uflag = False
            elif bflag and uflag and line_var in varlist:
                gcu_vals[gcu_][line_var][burnloc] = vec2list(line.split('=')[1])
            line = res.readline()
            lcount += 1

    xbmessages.status(' -done', args)
    return gcu_vals


def expand_res_kwords(inkeys: list, args=None):
    """
    Expand any variable keywords into actual SERPENT variables.
    The parameter block specifies what variables the user desires from the _res.m files.
    Since the number of useful variables could be several dozen (cross sections, discontinuity factors, 
    kinetic parameters, etc.), the user can specify specific keywords which will be expanded to include
    commonly used values.
    :param inkeys: Iterator of keywords from parameter block. Can be a mixed bag of direct SREPENT variables
    and expandable keywords
    :param args: arguments for status updates and errors
        if not None, then must be a dictionary with the following keys:
        - 'verbose' or 'quiet' -> boolean
        - 'output': either None for printing to stdout, or the name of a file for appending messages
    :return: Expanded list of variables to be scraped from _res.m
    """

    if args is None:
        args = xbcons.defaults
    elif isinstance(args, dict):
        args = xbcons.checkargs_defaults(args)

    for ndx in range(len(inkeys)):
        if inkeys[ndx] in xbcons.validKeywords:
            kwrd = inkeys.pop(ndx)
            inkeys.extend(xbcons.validKeywords[kwrd])
            xbmessages.status('Expanded and removed keyword '
                              '{} from parameter string'.format(kwrd), args)
        elif len(inkeys[ndx]) < 5:
            xbmessages.status('Did not recognize {} as a valid keyword. '
                              'Possible typo or short SERPENT variable'.format(inkeys[ndx]), args)
    return inkeys
