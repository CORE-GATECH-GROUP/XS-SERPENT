"""

test_scraper
    - Testing for the _res.m scraper

A. Johnson

This script will compare the output from the res_scraper function with the anticipated output by reading a result file
with various group constant universe values and burnup points.
Eventually this will also compare the human-readable outputs
"""
# TODO: I'm not sure how reliable/general/portable these import statements will be. Should investigate better setup
import unittest
from scraper import res_scraper

resfile = 'testing/coreWithDep_res.m'
gculist = ('4501', '4502')
varlist = ('INF_TOT', 'INF_FISS', 'MACRO_E', 'INF_S0')
burnlist = (0, 2.45753E-01)
burntype = 'BURNUP'

gcuouts = res_scraper(resfile, gculist, varlist, burnlist, burntype)


class TestGCUVals(unittest.TestCase):
    def test_file_exist(self):
        """Make sure that the method properly returns a -1 if the file given to res_scraper does not exist"""
        self.assertEqual(res_scraper('badfile', gculist, varlist, burnlist, burntype), -1)

    def test_bad_burntype(self):
        """Make sure the method return -2 if the burntype given to res_scraper is not in validBurnTypes"""
        self.assertEqual(res_scraper(resfile, gculist, varlist, burnlist, 'bad'), -2)


if __name__ == '__main__':
    unittest.main()
