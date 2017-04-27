"""

test_bumat.py
    - Testing for the fuel perturbation file
    

D. Kotlyar

Test should be ran from the same directory as the setup file (home directory)

"""
import os
import unittest

from xsboa import bumat

args = {'quiet': True, 'output': None}
inpfile = os.path.join('testing', 'SINP020.bumat0')
outfile = os.path.join('testing', 'perturbed.bumat0')

mat_test = ['fuel1', 'fuel2', 'fuel11', 'fuel111', 'fuel4']
bad_mod_mats = ['fuel1p80001r1', 'fuel2p80001r1', 'fuel11p80001r1', 'fuel111p80001r1']
prf_test = ['.03c', '.06c', '.09c', '.12c', '.15c']
tmp_test = ['300', '600', '900', '1200', '1500']


class TestReadParam(unittest.TestCase):

    def test_no_file(self):
        """Verify that the file not found error return -1..."""
        self.aflag = bumat.fuel_branch('bad.txt', outfile, mat_test, tmp_test, prf_test, args)
        self.assertEqual(self.aflag, -1)

    def test_mat_temps(self):
        """Verify that the correct error is thrown for len(mat) != len(temp)..."""
        self.assertEqual(-2, bumat.fuel_branch(inpfile, outfile, mat_test, [1], prf_test, args))

    def test_mat_prefix(self):
        """Verify that the correct error is thrown for len(mat) != len(prefix)..."""
        self.assertEqual(-2, bumat.fuel_branch(inpfile, outfile, mat_test, tmp_test, [1], args))

    def test_bad_pref(self):
        """Verify that the correct error is thrown for bad prefix..."""
        self.assertEqual(-3, bumat.fuel_branch(inpfile, outfile, mat_test, tmp_test,
                                               ['.03c', '.06c', '.09c', '.20c', '.15c'], args))

    def test_bad_temp(self):
        """Verify that the correct error is thrown for bad temperature..."""
        self.assertEqual(-3, bumat.fuel_branch(inpfile, outfile, mat_test, ['30', '600', '900', '1200', '1500'],
                                               prf_test, args))

    def test_num_mod_mat(self):
        """Verity that the correct error is thrown for incorrect # materials..."""
        self.assertEqual((-4, []), bumat.match_materials(inpfile, mat_test, bad_mod_mats, args))

    def test_good_bumat(self):
        """Verify that the bumat modifier script is working..."""
        self.assertEqual(0, bumat.fuel_branch(inpfile, outfile, mat_test, tmp_test, prf_test, args))
