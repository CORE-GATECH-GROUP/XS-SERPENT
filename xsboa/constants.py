"""Constants and default parameters

Andrew Johnson

List supported items and yield functionality to the user to update
any default parameters as they wish

Cross Section Libraries
-----------------------

The main dictionary ``_lib`` holds all the temperatures and associated
suffixes for a few common cross section libraries.
The structure is as follows ::

    'endfb7' : {
        'c':  { # continuous energy library
            <temp>: <suffix>
            }, 
        'gr': {  # graphite thermal scattering library
            <temp>: <suffix>
            },
        'lw': {  # light water thermal scattering library
            <temp>: <suffix>
            },
        'hw': {  # heavy water thermal scattering library
            <temp>: <suffix>
            },
        },
    'jef22': {
        ...
        },
    ...
    
The following libraries are currently supported:

    #. ``endfb7``
    #. ``jef22``
    #. ``jeff31``
    #. `` jeff311``
    
"""

_xslib = dict()

_xslib['endfb7'] = {'c': {300: '03c', 600: '06c', 900: '09c', 1200: '12c', 1500: '15c', 1800: '18c'},
                    'gr': {296: '00t', 400: '04t', 500: '08t', 600: '12t', 700: '16t', 800: '18t', 1000: '20t',
                           1200: '22t', 1600: '24t', 1999: '26t', 294: '00t'},
                    'hw': {296: '00t', 350: '02t', 400: '04t', 450: '06t', 500: '08t', 600: '12t', 800: '18t',
                           1000: '20t', 294: '00t', 550: '10t', 650: '14t', 324: '01t', 374: '03t', 424: '05t',
                           474: '07t', 524: '09t', 574: '11t', 674: '14t', 644: '14t'},
                    'lw': {296: '00t', 350: '02t', 400: '04t', 450: '06t', 500: '08t', 600: '12t', 800: '18t',
                           1000: '20t', 294: '00t', 550: '10t', 650: '14t', 324: '01t', 374: '03t', 424: '05t',
                           474: '07t', 524: '09t', 574: '11t', 624: '13t', 647: '14t'}}

_xslib['jef22'] = {'c': {300: '03c', 600: '06c', 900: '09c', 1200: '12c', 1500: '15c', 1800: '18c'},
                   'gr': {296: '00t', 400: '04t', 500: '08t', 600: '12t', 700: '16t', 800: '18t', 1000: '20t',
                          1200: '22t', 1600: '24t', 1999: '26t', 294: '00t'},
                   'hw': {296: '00t', 350: '02t', 400: '04t', 450: '06t', 500: '08t', 600: '12t', 800: '18t',
                          1000: '20t', 294: '00t', 550: '10t', 650: '14t', 324: '01t', 374: '03t', 424: '05t',
                          474: '07t', 524: '09t', 574: '11t', 674: '14t', 644: '14t'},
                   'lw': {296: '00t', 350: '02t', 400: '04t', 450: '06t', 500: '08t', 600: '12t', 800: '18t',
                          1000: '20t', 294: '00t', 550: '10t', 650: '14t', 324: '01t', 374: '03t', 424: '05t',
                          474: '07t', 524: '09t', 574: '11t', 624: '13t', 647: '14t'}}

_xslib['jeff31'] = {'c': {300: '03c', 600: '06c', 900: '09c', 1200: '12c', 1500: '15c', 1800: '18c'},
                    'gr': {296: '00t', 400: '04t', 500: '08t', 600: '12t', 700: '16t', 800: '18t', 1000: '20t',
                           1200: '22t', 1600: '24t', 1999: '26t', 294: '00t'},
                    'hw': {296: '00t', 350: '02t', 400: '04t', 450: '06t', 500: '08t', 600: '12t', 800: '18t',
                           1000: '20t', 294: '00t', 550: '10t', 650: '14t', 324: '01t', 374: '03t', 424: '05t',
                           474: '07t', 524: '09t', 574: '11t', 674: '14t', 644: '14t'},
                    'lw': {296: '00t', 350: '02t', 400: '04t', 450: '06t', 500: '08t', 600: '12t', 800: '18t',
                           1000: '20t', 294: '00t', 550: '10t', 650: '14t', 324: '01t', 374: '03t', 424: '05t',
                           474: '07t', 524: '09t', 574: '11t', 624: '13t', 647: '14t'}}

_xslib['jeff311'] = {'c': {300: '03c', 600: '06c', 900: '09c', 1200: '12c', 1500: '15c', 1800: '18c'},
                     'gr': {296: '00t', 400: '04t', 500: '08t', 600: '12t', 700: '16t', 800: '18t', 1000: '20t',
                            1200: '22t', 1600: '24t', 1999: '26t', 294: '00t'},
                     'hw': {296: '00t', 350: '02t', 400: '04t', 450: '06t', 500: '08t', 600: '12t', 800: '18t',
                            1000: '20t', 294: '00t', 550: '10t', 650: '14t', 324: '01t', 374: '03t', 424: '05t',
                            474: '07t', 524: '09t', 574: '11t', 674: '14t', 644: '14t'},
                     'lw': {296: '00t', 350: '02t', 400: '04t', 450: '06t', 500: '08t', 600: '12t', 800: '18t',
                            1000: '20t', 294: '00t', 550: '10t', 650: '14t', 324: '01t', 374: '03t', 424: '05t',
                            474: '07t', 524: '09t', 574: '11t', 624: '13t', 647: '14t'}}


def getxslib(path: str):
    """Return a dictionary structured according to the docstring
    
    :param path: Path to ``SERPENT`` data file, e.g. 
    ``/xsdata/sss_endfb7u.xsdata``
    
    :return: dictionary with library types as keys with dictionaries of 
    temp: suffix pairs
    """
    xstemps = {'c': {}}
    xsprefs = {'c': []}
    with open(path, 'r') as xsp:
        line = xsp.readline()
        while line != '':
            try:
                libid = line.index('.')
            except ValueError:
                print('Possible formatting error in file {}. Will not proceed'.format(path))
                return xstemps, xsprefs
            pref = line[libid + 1: libid + 4]
            if pref[-1] == 'c':
                if pref not in xsprefs['c']:
                    xsprefs['c'].append(pref)
                    xstemps['c'][int(line[48:53])] = pref
            else:
                if line[3:5] not in xstemps:
                    xsprefs[line[3:5]] = [pref, ]
                    xstemps[line[3:5]] = {int(line[48:53]): pref}
                elif pref not in xsprefs:
                    xsprefs[line[3:5]].append(pref)
                    xstemps[line[3:5]][int(line[48:53])] = pref
            line = xsp.readline()
    return xstemps


def tempsuffix(temp: (int, float), libtype='c', **args):
    """
    
    :param temp: 
    :param libtype: 
    :param args: 
    :return: 
    """
