"""

test_modmat.py
    - Testing for the material perturbation file
    

D. Kotlyar

Test should be ran from the same directory as the setup file (home directory)

"""
import os
import unittest

from xsboa import bumat

args = {'quiet': True, 'output': None}
inpfile = os.path.join('testing', 'uo2material.txt')
outfile1 = os.path.join('testing', 'waterperturbation_density')
outfile2 = os.path.join('testing', 'waterperturbation_temperature')
outfile3 = os.path.join('testing', 'mox1_density')
outfile4 = os.path.join('testing', 'mox2_temperature')

mat_test = 'water'
bad_mod_mats = 'nomaterial'
prf_test = '.15c'
tmp_test = '499'
dens_test = '4'

class TestReadParam(unittest.TestCase):

    def test_no_file(self):
        """Verify that the file not found error return -1..."""
        self.aflag = modmat.perturb_mat('bad.txt', outfile1, 'water', '-1.999', '499', '.15c', 'density, temperature', args)
        self.assertEqual(self.aflag, -1)

    def test_mat_temps(self):
        """Verify that the correct error is thrown for len(mat) != len(temp)..."""
        self.assertEqual(-2, modmat.perturb_mat(inpfile, outfile1, 'water', '-1.999', '99', '.15c', 'density, temperature', args))

    def test_mat_prefix(self):
        """Verify that the correct error is thrown for len(mat) != len(prefix)..."""
        self.assertEqual(-2, modmat.perturb_mat(inpfile, outfile1, 'water', '-1.999', '499', '.29c', 'density, temperature', args))

    def test_no_mat(self):
        """Verify that the correct error is thrown for len(mat) != len(prefix)..."""
        self.assertEqual(-3, modmat.perturb_mat(inpfile, outfile1, 'nomaterial', '-1.999', '499', '.06c', 'density, temperature', args))

    def test_good_modmat(self):
        """Verify that the bumat modifier script is working..."""
        self.assertEqual(0, modmat.perturb_mat(inpfile, outfile1, 'water', '-0.71234', '499', '.15c', 'density', args))
        self.assertEqual(0, modmat.perturb_mat(inpfile, outfile2, 'water', '-0.71234', '453', '.06c', 'density, temperature', args))
        self.assertEqual(0, modmat.perturb_mat(inpfile, outfile1, 'MOX1', '0.015678', '1275.15', '.12c', 'density', args))
        self.assertEqual(0, modmat.perturb_mat(inpfile, outfile1, 'MOX2', '4.015678', '1475.15', '.15c', 'density, temperature', args))