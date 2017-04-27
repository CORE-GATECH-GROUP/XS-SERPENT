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

Developed by Computational Reactor Engineering Group at Georgia Institute 
of Technology

"""
import argparse


def main():
    """Process input arguments.
    
    Return:
        input arguments in dictionary form
            i.e. d['verbose'] -> verbose flag
    """
    parser = argparse.ArgumentParser(description=__doc__, prefix_chars='->',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     usage=('[-h] [-q | -v ] (-c | -p | -x)'
                                            ' file -o OUTPUT'))
    parser.add_argument('file', help='nominal SERPENT input file',
                        type=argparse.FileType('w'))
    status = parser.add_mutually_exclusive_group()
    status.add_argument('-q', '--quiet', action='store_true',
                        help='only print fatal messages')
    status.add_argument('-v', '--verbose', action='store_true',
                        help='show status messages along the way')
    parser.add_argument('>', '-o', '--output',
                        help='write messages to file of your choice')
    optype = parser.add_mutually_exclusive_group(required=True)
    optype.add_argument('-c', action='store_true',
                        help='option to create the input files')
    optype.add_argument('-p', action='store_true',
                        help='option to process output data')
    optype.add_argument('-x', action='store_true',
                        help='create and execute branched files')

    args = vars(parser.parse_args())

    kwargs = {}
    for key in ('verbose', 'quiet', 'output'):
        kwargs[key] = args[key]
        del args[key]


if __name__ == '__main__':
    main()
