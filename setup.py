"""

Setup
    - Properly install xsboa
    
A. Johnson
    
Executing this script will correctly install xsboa and submdoules and allow the user to use commands like
 `from xsboa.<submodule> import <subfunction>` from any directory.
 
Status
    WIP
"""

from setuptools import setup

long_description = r"""
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

""".strip()

vRelease = 0
vMacro = 1
vMicro = 5

vDevel = ''  # 'dev' for developing features, '' for completed features
vDevelMicro = 4  # empty string if feature is complete (i.e. vDevel = '')

if vDevel:
    version = "{}.{}.{}.{}{}".format(vRelease, vMacro, vMicro, vDevel, vDevelMicro)
else:
    version = "{}.{}.{}".format(vRelease, vMacro, vMicro)

installReqs = (
    None
)  # this is where any necessary and additional modules will be added like numpy, pandas, or matplotlib


if __name__ == '__main__':
    setup(
        name='xsboa',
        version=version,
        description='A cross section preparation and processing utility for SERPENT',
        long_description=long_description,
        maintainer='Computational Reactor Engineering Lab - Georgia Institute of Technology',
        url='https://github.com/CORE-GATECH-GROUP/XS-SERPENT',
        install_requires=installReqs,
        packages=['xsboa'],
        test_suite='testing'
    )
