r"""
     __   __ _____ ____   ____
     \ \ / // ____|  _ \ / __ \   /\
      \ V /| (___ | |_) | |  | | /  \
       > <  \___ \|  _ <| |  | |/ /\ \
      / . \ ____) | |_) | |__| / ____ \
     /_/ \_\_____/|____/ \____/_/    \_\

                    XSBOA
A wrapper program for generating homogenized
macroscopic cross sections and group constant
parameters with SERPENT.

Developed by Computational Reactor Physics
Group at Georgia Institute of Technology

"""
import argparse


def get_args():
    """Process input arguments
    
    Return:
        input arguments in dictionary form
            i.e. d['verbose'] -> verbose flag
    """
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
                                     prefix_chars='->')
    parser.add_argument('file', help='nominal SERPENT input file', type=argparse.FileType('w'))
    status = parser.add_mutually_exclusive_group()
    status.add_argument('-q', '--quiet', action='store_true', help='only print fatal messages')
    status.add_argument('-v', '--verbose', action='store_true', help='show status messages along the way')
    parser.add_argument('>', '-o', '--output', help='write messages to file of your choice')
    op_regimes = parser.add_mutually_exclusive_group(required=True)
    op_regimes.add_argument('-c', action='store_true', help='option to create the input files')
    op_regimes.add_argument('-p', action='store_true', help='option to process output data')
    return parser.parse_args().keyvalues()


if __name__ == '__main__':
    # Process input arguments
    args = get_args()

    if args['output'] is None:
        print(__doc__)
    else:
        with open(args['output'], 'w') as out:
            out.write(__doc__)
