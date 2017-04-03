"""

test_readparam.py
    - Testing for the parameter reader function
    
A. Johnson

Test should be ran from the same directory as the setup file (home directory)

"""
import os
import unittest

from xsboa import readparam

args = {'quiet': True, 'output': None}
inpfile = os.path.join('testing', 'uo2mox.txt')

# Intended outputs
rLoc = (0, 19)
rNom = {'UO2': {'temp': 900, 'adens': 6.5800E-02}, 'MOX1': {'temp': 900}, 'MOX2': {'temp': 900}, 'MOX3': {'temp': 900},
        'water1': {'mdens': 7.088200E-02, 'temp': 600}}
rExe = 'qsub -v INPARG={} serp.pbs'
rBranch = {'hUO2': {'UO2': {'temp': 1200}}, 'hFuel': {'UO2': {'temp': 1200}, 'MOX1': {'temp': 1200},
                                                      'MOX2': {'temp': 1200}, 'MOX3': {'temp': 1200}},
           'void40b0': {'water1': {'void': 40}, 'burn': 1}}
rBurn = ['burn 1 4 5R5 keep 1 30', 'burn 1 4 5R5 keep 1 30']

# Actual outputs
oLoc, oNom, oBranch, oBurn, oExe = readparam(inpfile, args)


class TestReadParam(unittest.TestCase):
    def test_file_exists(self):
        """Make sure the method returns (False, -1) if bad file"""
        self.assertEquals(oLoc, (False, -1))
