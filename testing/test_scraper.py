"""

test_scraper
    - Testing for the _res.m scraper

A. Johnson

This script will compare the output from the res_scraper function with the anticipated output by reading a result file
with various group constant universe values and burnup points.
Eventually this will also compare the human-readable outputs.

Test should be ran with the working directory as the same directory as the setup file
"""

import os
import unittest

from xsboa.scraper import SerpResFile, res_scraper

resfile = os.path.join('testing', 'coreWithDep_res.m')
gculist = ('4501', '4507')
varlist = ('INF_TOT', 'INF_FISS', 'INF_S0')
burnlist = (0, -1)  # 2.45754E-01
burntype = 'BURNUP'
args = {'quiet': True, 'output': None}

SerpOut = SerpResFile(resfile, True, gculist, varlist, burnlist, burntype, args)

intendedouts = {
    '4501': {'INF_TOT': ((5.36358E-01, 0.00203, 1.39301E+00, 0.00236), (5.35548E-01, 0.00120, 1.38270E+00, 0.00210)),
             'INF_FISS': ((2.10687E-03, 0.00729, 4.20513E-02, 0.00779), (2.11309E-03, 0.00651, 4.16105E-02, 0.00430)),
             'INF_S0': ((5.09216E-01, 0.00201, 1.89036E-02, 0.00663, 1.10315E-03, 0.06162, 1.32692E+00, 0.00257),
                        (5.08407E-01, 0.00115, 1.87531E-02, 0.00742, 1.04182E-03, 0.06599, 1.31528E+00, 0.00236))},
    '4507': {'INF_TOT': ((5.11183E-01, 0.00065, 1.29825E+00, 0.00133), (5.11823E-01, 0.00098, 1.30188E+00, 0.00121)),
             'INF_FISS': ((2.09280E-03, 0.00274, 4.17435E-02, 0.00226), (2.08014E-03, 0.00281, 4.09216E-02, 0.00174)),
             'INF_S0': ((4.85582E-01, 0.00059, 1.75469E-02, 0.00270, 1.08619E-03, 0.02358, 1.23375E+00, 0.00142),
                        (4.86132E-01, 0.00099, 1.75992E-02, 0.00226, 1.08030E-03, 0.03278, 1.23529E+00, 0.00125))}
}

missingstr = 'not in res_scraper output'


class TestGCUVals(unittest.TestCase):
    def test_file_exist(self):
        """Make sure that the method  returns a -1 for non-existent file"""
        self.assertEqual(res_scraper('badfile', gculist, varlist, burnlist, burntype, args), -1)

    def test_bad_burntype(self):
        """Make sure the method return -2 for invalid burntypes"""
        self.assertEqual(res_scraper(resfile, gculist, varlist, burnlist, 'bad', args), -2)

    def test_universe(self):
        """Make sure the correct universes are given as keys in output of correct res_scraper"""
        for gcu in gculist:
            with self.subTest():
                self.assertIn(gcu, SerpOut.gcuvals, msg='Universe {} {}'.format(gcu, missingstr))

    def test_variables(self):
        """Make sure the correct variables are stored for each group constant dictionary"""
        for gcu in gculist:
            if gcu in SerpOut.gcuvals:
                for var in varlist:
                    with self.subTest():
                        self.assertIn(var, SerpOut.gcuvals[gcu],
                                      msg='Variable {} of universe {} {}'.format(var, gcu, missingstr))

    def test_len_burnup_vars(self):
        """Make sure correct number of burnup states for each variable is scraped"""
        for gcu in gculist:
            if gcu in SerpOut.gcuvals:
                for var in varlist:
                    if var in SerpOut.gcuvals[gcu]:
                        with self.subTest():
                            self.assertEqual(len(intendedouts[gcu][var]), len(SerpOut.gcuvals[gcu][var]),
                                             msg='len(out[{}][{}] is {} should be {}'.
                                             format(gcu, var, len(SerpOut.gcuvals[gcu][var]),
                                                    len(intendedouts[gcu][var])))

    def test_no_burnup_none(self):
        """Make sure the burnup values have been properly initialized"""
        for gcu in gculist:
            if gcu in SerpOut.gcuvals:
                for var in varlist:
                    if var in SerpOut.gcuvals[gcu]:
                        if len(intendedouts[gcu][var]) == len(SerpOut.gcuvals[gcu][var]):
                            for bb in range(len(intendedouts[gcu][var])):
                                self.assertIsNotNone(SerpOut.gcuvals[gcu][var],
                                                     msg='Bp {} of var {} of GCU {} is None'.format(bb, var, gcu))

    def test_len_burnup_values(self):
        """Make sure correct number of values is assigned to each burnup point"""
        for gcu in gculist:
            if gcu in SerpOut.gcuvals:
                for var in varlist:
                    if var in SerpOut.gcuvals[gcu]:
                        if len(intendedouts[gcu][var]) == len(SerpOut.gcuvals[gcu][var]):
                            for bb in range(len(intendedouts[gcu][var])):
                                if SerpOut.gcuvals[gcu][var][bb] is not None:
                                    with self.subTest():
                                        self.assertEqual(len(intendedouts[gcu][var][bb]),
                                                         len(SerpOut.gcuvals[gcu][var][bb]),
                                                         msg='len(out[{}][{}][{}] is {} should be {}'.
                                                         format(gcu, var, bb, len(SerpOut.gcuvals[gcu][var][bb]),
                                                                len(intendedouts[gcu][var][bb])))

    def test_burnup_variables(self):
        """Make sure the end resulting values are correct"""
        for gcu in gculist:
            if gcu in SerpOut.gcuvals:
                for var in varlist:
                    if var in SerpOut.gcuvals[gcu]:
                        if len(intendedouts[gcu][var]) == len(SerpOut.gcuvals[gcu][var]):
                            for bb in range(len(intendedouts[gcu][var])):
                                if SerpOut.gcuvals[gcu][var][bb] is not None:
                                    if len(intendedouts[gcu][var][bb]) == len(SerpOut.gcuvals[gcu][var][bb]):
                                        for valindx in range(len(intendedouts[gcu][var][bb])):
                                            with self.subTest():
                                                # even values will be actual group constant values, odds are uncertainty
                                                # except for energy widths
                                                msg_ = 'len([{}][{}][{}][{}] is {} should be {}'. \
                                                    format(gcu, var, bb, valindx,
                                                           SerpOut.gcuvals[gcu][var][bb][valindx],
                                                           intendedouts[gcu][var][bb][valindx])
                                                if valindx % 2 == 0:
                                                    self.assertAlmostEqual(intendedouts[gcu][var][bb][valindx],
                                                                           SerpOut.gcuvals[gcu][var][bb][valindx],
                                                                           places=7, msg=msg_)
                                                else:
                                                    self.assertAlmostEqual(intendedouts[gcu][var][bb][valindx],
                                                                           SerpOut.gcuvals[gcu][var][bb][valindx],
                                                                           places=5, msg=msg_)


if __name__ == '__main__':
    unittest.main()
