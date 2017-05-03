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
import textwrap

import xsboa.messages as messages

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

_defaults = {
    'lib': 'endfb7',
    'verbose': False,
    'quiet': False,
    'output': None,
}

perts = ('adens', 'mdens', 'temp', 'void')
perfDefs = ('Atomic density overwrite', 'Mass density overwrite',
            'Temperature overwrite', 'Density update based on void fraction')

burntypes = ('daystep', 'daytot', 'bustep', 'butot', 'decstep', 'dectot')
burnDefs = ('interval depletion step [days]', 'cummulative depletion step [days]',
            'interval depletion step [MWd/kgU]', 'cummulative depletion step [MWd/kgU]',
            'interval decay step [days]', 'cummulative decay step [days]')


def showdefaults(**args: dict):
    """Show the default and supported parameters.
    
    Raises system exit
    """
    if 'verbose' in args:
        vv = args['verbose']
    else:
        vv = False
    nestgap = '  '

    print('\nxsboa defaults\n')
    keylen = len(max(list(_defaults.keys()), key=len))
    for defkey in _defaults:
        print(nestgap + '{} : {}'.format(
            textwrap.indent(defkey, ' ' * (keylen - len(defkey))),
            _defaults[defkey]))

    if vv:
        print('\nSupported suffixes and temperatures '
              'in default cross section library')
    else:
        print('\nSupported material suffixes in default cross section library')
    keylen = len(max(list(_xslib[_defaults['lib']].keys()), key=len))
    for dlib in _xslib[_defaults['lib']]:
        print(nestgap + '{} '.format(
            textwrap.indent(dlib, ' ' * (keylen - len(dlib)))), end='')
        if vv:
            newdent = len(nestgap) * 2 + keylen
            tmps = nestgap.join([str(tt) for tt in
                                 sorted(list(_xslib[_defaults['lib']][dlib].keys()))])
            print(''.join(textwrap.wrap(tmps, width=55, initial_indent='\n' + ' ' * newdent,
                                        subsequent_indent='\n' + ' ' * newdent)))
        else:
            print('')
    if vv:
        prettyprint_supports('Supported perturbations', perts, nestgap,
                             extras=perfDefs)
        prettyprint_supports('Supported burnup strings', burntypes, nestgap,
                             extras=burnDefs)
    else:
        prettyprint_supports('Supported perturbations', perts, nestgap)
        prettyprint_supports('Supported burnup strings', burntypes, nestgap)

    raise SystemExit


def prettyprint_supports(tstr: str, supports: (list, tuple), init_gap: str,
                         extras=None):
    """Print the supported string in a nice way"""
    print('\n', tstr)
    keylen = len(max(supports, key=len))
    for nn, sup in enumerate(supports):
        print(init_gap, '{}'.format(
            textwrap.indent(sup, ' ' * (keylen - len(sup)))
        ), end='')
        if extras is not None:
            print(':', extras[nn])
        else:
            print('')


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
    """Return the correct library suffix for a given temperature.
    
    ``SERPENT`` requires that the nuclide library used be from the 
    closest temparature below the desired temperature to properly
    broaden the cross sections.
    
    Ex. Given valid temperatures 300, 600, 900, and 1200, plus a 
    desired  temperature of 1000, ``SERPENT`` could accept the 300-
    900K  libraries, but the 900K library would be the most accurate.
    
    :param temp: Material temperature in K
    :param libtype: Type of library. Typical cases included ``'c'`` for
    continuous energy and various thermal scattering  libraries. For 
    the case of generality, the current _xslib structure includes
    unique keys for light and heavy water media, as well as graphite.
    The libtype arguments for these scattering libraries would be
    ``'lw'``, ``'hw'``, and ``'gr'`` respectively.
    :param args: Arguments to pass into messages, or to obtain a 
    user specified library.
    
    :return: Valid library suffix
     
     For errors:
     
        #. -1: Specified temperature is below the lowest temperature
        in the library (typically 300K)
    """
    if 'lib' not in args:
        libn = _defaults['lib']
    else:
        libn = args['lib']
        if libn not in _xslib:
            messages.fatal('Library type {} not found in _xslib'.format(libn),
                           'constants.tempsuffix()', args)

    tvec = sorted(list(_xslib[libn][libtype].keys()))
    if min(tvec) < temp < max(tvec):
        diff = [tt - temp for tt in tvec]
        nn = 0
        while nn < len(diff):
            if diff[nn] <= 0 < diff[nn + 1]:
                return _xslib[libn][libtype][tvec[nn]]
            nn += 1

    else:
        if temp < min(tvec):
            return -1
        elif temp == min(tvec):
            return _xslib[libn][libtype][temp]
        if temp >= max(tvec):
            return _xslib[libn][libtype][max(tvec)]
    # if we've made it here, then something didn't work right, maybe in the while loop?
    raise RuntimeError('Did not properly return from constants.tempsuffix()'
                       ' temp: {}, libtype: {}'.format(temp, libtype))


def checkargs_defaults(argdict: dict):
    """Return a dictionary with the default parameters added, if not present."""
    for arg in _defaults:
        if arg not in argdict:
            argdict[arg] = _defaults[arg]
    return argdict


# Testing
if __name__ == '__main__':
    showdefaults(**{'verbose': True})
