r"""
                __   __ _____ ____   ____
                \ \ / // ____|  _ \ / __ \   /\
                 \ V /| (___ | |_) | |  | | /  \
                  > <  \___ \|  _ <| |  | |/ /\ \
                 / . \ ____) | |_) | |__| / ____ \
                /_/ \_\_____/|____/ \____/_/    \_\

                              XSBOA
A wrapper program for generating homogenized macroscopic cross sections
and group constant parameters with SERPENT.

Developed by Computational Reactor Engineering
Group at Georgia Institute of Technology


"""
import argparse

import xsboa.constants as xbcons

VERSION = '0.1.9'


def get_args():
    """Process input arguments.
    
    Return:
        input arguments in dictionary form
            i.e. d['verbose'] -> verbose flag
    """
    usage = ('python xsboa -h : show this message',
             'python xsboa run [-h] [-v|-q] (-c|-x|-p) file -o OUTPUT '
             ': run xsboa',
             'python xsboa show [-h] [-v] (-D|-L|-V) : show defaults, '
             'license, or version information')
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='subcommands:\n  ' + '\n  '.join(usage[1:]))

    subparsers = parser.add_subparsers()

    # create the subparser handling running xsboa
    runxsboa = subparsers.add_parser('run',
                                     help='run XSBOA', usage=usage[1])
    runxsboa.add_argument('-o', '--output',
                          help='write messages to file of your choice')
    runxsboa.add_argument('file', help='nominal SERPENT input file',
                          type=argparse.FileType('w'))

    runarg = runxsboa.add_mutually_exclusive_group(required=True)
    runarg.add_argument('-c', action='store_true',
                        help='option to create the input files')
    runarg.add_argument('-x', action='store_true',
                        help='option to create and execute the input files')
    runarg.add_argument('-p', action='store_true',
                        help='option to process output data')

    # create the subparser handling showing defaults and information
    showcmds = subparsers.add_parser('show',
                                     help='display various features',
                                     usage=usage[2])

    showopts = showcmds.add_mutually_exclusive_group(required=True)
    showopts.add_argument('-D', '--defaults', help='show default parameters and exit',
                          action='store_true')
    showopts.add_argument('-L', '--license', action='store_true',
                          help='show license and exit')
    showopts.add_argument('-V', '--version', action='version',
                          version='xsboa {}'.format(VERSION),
                          help='show license and exit')

    status = runxsboa.add_mutually_exclusive_group()
    status.add_argument('-q', '--quiet', help='only print fatal messages',
                        action='store_true')
    status.add_argument('-v', '--verbose', action='store_true',
                        help='print status messages along the way')

    showcmds.add_argument('-v', '--verbose', action='store_true',
                          help='show detailed information on defaults')

    return parser.parse_args()


if __name__ == '__main__':
    # Process input arguments
    args = get_args()

    if len(args._get_kwargs()) == 0:
        raise SystemExit('Arguments required. '
                         'Use python xsboa -h for argument explanations')

    if 'defaults' in args:
        if args.defaults:
            xbcons.showdefaults(**{'verbose': args.verbose})
        elif args.license:
            raise NotImplementedError('License functionality not fully complete available yet')

    kwargs = {
        'verbose': args.verbose,
        'output': args.o,
        'quiet': args.quiet,
    }
    file = args.file
    if args.c:
        runtype = 'c'
    elif args.x:
        runtype = 'x'
    elif args.p:
        runtype = 'p'
    else:
        raise RuntimeError('Somehow managed to run xsboa without specifying runtype')

    if kwargs['output'] is None:
        print(__doc__)
    else:
        with open(kwargs['output'], 'w') as out:
            out.write(__doc__)

