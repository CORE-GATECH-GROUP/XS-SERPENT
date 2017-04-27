"""

test_bumat.py
    - Testing for the fuel perturbation file
    

D. Kotlyar

Test should be ran from the same directory as the setup file (home directory)

"""
import os
import unittest

from xsboa import readparam
from xsboa import bumat

args = {'quiet': True, 'output': None}
inpfile = os.path.join('testing', 'SINP020.bumat0')
outfile = os.path.join('testing', 'perturbed.bumat0')

mat_test = ['fuel1', 'fuel2', 'fuel11', 'fuel111', 'fuel4']
prf_test = ['.03c', '.06c', '.09c', '.12c', '.15c']
tmp_test = ['300', '600', '900', '1200', '1500']

class TestReadParam(unittest.TestCase):
    def setUp(self):
        self.flag = 0
    def test_no_file(self):
        """Validate output if the file does not exist (False, -2)."""
        self.aflag = fuel_branch(inpfile, outfile, mat_test, tmp_test, prf_test, args=None)
        self.assertEqual(flag, (False, -1))


    def test_loc(self):
        """Validate location of parameter block - zero indexed."""
        self.assertEqual(self.aloc, self.loc)

    def test_burn(self):
        """Validate burnup list."""
        self.assertEqual(self.aloc, self.loc)



