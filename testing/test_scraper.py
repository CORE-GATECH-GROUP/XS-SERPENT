"""

test_scraper
    - Testing for the _res.m scraper

Andrew Johnson

This script will compare the output from the res_scraper function with
the anticipated output by reading a result file with various group 
constant universe values and burnup points.
Eventually this will also compare the human-readable outputs.

Test should be ran with the working directory as the same 
directory as the setup file
"""

import os
import unittest

from xsboa.scraper import SerpResFile, res_scraper

varlist = ('INF_TOT', 'INF_FISS', 'INF_S0')
args = {'quiet': True, 'output': None}

missingstr = 'not in res_scraper output'


class ScraperErrors(unittest.TestCase):
    def setUp(self):
        self.burnlist = (0,)
        self.gcu = ('0',)
        self.resfile = os.path.join('testing', 'pwrpin300_res.m')
        self.burntype = 'BURNUP'

    def err_file_exist(self):
        """Make sure that the method  returns a -1 for non-existent file"""
        self.assertEqual(res_scraper('badfile', self.gcu, varlist,
                                     self.burnlist, self.burntype, args), -1)

    def err_bad_burntype(self):
        """Make sure the method return -2 for invalid burntypes"""
        self.assertEqual(res_scraper(self.resfile, self.gcu, varlist,
                                     self.burnlist, 'bad', args), -2)

    def err_bad_burnlist(self):
        """Make sure the method returns -3 for non-iterable burnlist"""
        self.assertEqual(-3, res_scraper(self.resfile, self.gcu, varlist,
                                         1, self.burntype, args))


class ScraperDepletion(unittest.TestCase):
    def setUp(self):
        self.resfile = os.path.join('testing', 'coreWithDep_res.m')
        self.gcu = ('4501', '4507')
        self.burnlist = (0, -1)  # 2.45754E-01
        self.burntype = 'BURNUP'
        self.SerpOut = SerpResFile(self.resfile, True, self.gcu, varlist,
                                   self.burnlist, self.burntype, args)
        self.goodouts = {
            '4501': {
                'INF_TOT': ((5.36358E-01, 0.00203, 1.39301E+00, 0.00236),
                            (5.35548E-01, 0.00120, 1.38270E+00, 0.00210)),
                'INF_FISS': (
                    (2.10687E-03, 0.00729, 4.20513E-02, 0.00779),
                    (2.11309E-03, 0.00651, 4.16105E-02, 0.00430)),
                'INF_S0': ((5.09216E-01, 0.00201, 1.89036E-02, 0.00663,
                            1.10315E-03, 0.06162, 1.32692E+00, 0.00257),
                           (5.08407E-01, 0.00115, 1.87531E-02, 0.00742,
                            1.04182E-03, 0.06599, 1.31528E+00, 0.00236))},
            '4507': {
                'INF_TOT': ((5.11183E-01, 0.00065, 1.29825E+00, 0.00133),
                            (5.11823E-01, 0.00098, 1.30188E+00, 0.00121)),
                'INF_FISS': (
                    (2.09280E-03, 0.00274, 4.17435E-02, 0.00226),
                    (2.08014E-03, 0.00281, 4.09216E-02, 0.00174)),
                'INF_S0': ((4.85582E-01, 0.00059, 1.75469E-02, 0.00270,
                            1.08619E-03, 0.02358, 1.23375E+00, 0.00142),
                           (4.86132E-01, 0.00099, 1.75992E-02, 0.00226,
                            1.08030E-03, 0.03278, 1.23529E+00, 0.00125))}
        }

    def test_universe(self):
        """Make sure the correct universes are given as keys in output of correct res_scraper"""
        for gcu in self.gcu:
            self.assertIn(gcu, self.SerpOut.gcuvals, msg='Universe {} {}'.format(gcu, missingstr))

    def test_variables(self):
        """Make sure the correct variables are stored for each group constant dictionary"""
        for gcu in self.gcu:
            if gcu in self.SerpOut.gcuvals:
                for var in varlist:
                    self.assertIn(var, self.SerpOut.gcuvals[gcu],
                                  msg='Variable {} of universe {} {}'.format(var, gcu, missingstr))

    def test_len_burnup_vars(self):
        """Make sure correct number of burnup states for each variable is scraped"""
        for gcu in self.gcu:
            if gcu in self.SerpOut.gcuvals:
                for var in varlist:
                    if var in self.SerpOut.gcuvals[gcu]:
                        self.assertEqual(len(self.goodouts[gcu][var]),
                                         len(self.SerpOut.gcuvals[gcu][var]),
                                         msg='len(out[{}][{}] is {} should be {}'.
                                         format(gcu, var,
                                                len(self.SerpOut.gcuvals[gcu][var]),
                                                len(self.goodouts[gcu][var])))

    def test_no_burnup_none(self):
        """Make sure the burnup values have been properly initialized"""
        for gcu in self.gcu:
            if gcu in self.SerpOut.gcuvals:
                for var in varlist:
                    if var in self.SerpOut.gcuvals[gcu]:
                        if len(self.goodouts[gcu][var]) == len(self.SerpOut.gcuvals[gcu][var]):
                            for bb in range(len(self.goodouts[gcu][var])):
                                self.assertIsNotNone(self.SerpOut.gcuvals[gcu][var],
                                                     msg='Bp {} of var {} of GCU {} is None'.format(bb, var, gcu))

    def test_len_burnup_values(self):
        """Make sure correct number of values is assigned to each burnup point"""
        for gcu in self.gcu:
            if gcu in self.SerpOut.gcuvals:
                for var in varlist:
                    if var in self.SerpOut.gcuvals[gcu]:
                        if len(self.goodouts[gcu][var]) == len(self.SerpOut.gcuvals[gcu][var]):
                            for bb in range(len(self.goodouts[gcu][var])):
                                if self.SerpOut.gcuvals[gcu][var][bb] is not None:
                                    self.assertEqual(len(self.goodouts[gcu][var][bb]),
                                                     len(self.SerpOut.gcuvals[gcu][var][bb]),
                                                     msg='len(out[{}][{}][{}] is {} should be {}'.
                                                     format(gcu, var, bb,
                                                            len(self.SerpOut.gcuvals[gcu][var][bb]),
                                                            len(self.goodouts[gcu][var][bb])))

    def test_burnup_variables(self):
        """Make sure the end resulting values are correct"""
        for gcu in self.gcu:
            if gcu in self.SerpOut.gcuvals:
                for var in varlist:
                    if var in self.SerpOut.gcuvals[gcu]:
                        if len(self.goodouts[gcu][var]) == len(self.SerpOut.gcuvals[gcu][var]):
                            for bb in range(len(self.goodouts[gcu][var])):
                                if self.SerpOut.gcuvals[gcu][var][bb] is not None:
                                    if len(self.goodouts[gcu][var][bb]) == len(self.SerpOut.gcuvals[gcu][var][bb]):
                                        for valindx in range(len(self.goodouts[gcu][var][bb])):
                                            # even values will be actual group constant values, odds are uncertainty
                                            # except for energy widths
                                            msg_ = '[{}][{}][{}][{}] is {} should be {}'. \
                                                format(gcu, var, bb, valindx,
                                                       self.SerpOut.gcuvals[gcu][var][bb][valindx],
                                                       self.goodouts[gcu][var][bb][valindx])
                                            if valindx % 2 == 0:
                                                self.assertAlmostEqual(self.goodouts[gcu][var][bb][valindx],
                                                                       self.SerpOut.gcuvals[gcu][var][bb][valindx],
                                                                       places=7, msg=msg_)
                                            else:
                                                self.assertAlmostEqual(self.goodouts[gcu][var][bb][valindx],
                                                                       self.SerpOut.gcuvals[gcu][var][bb][valindx],
                                                                       places=5, msg=msg_)


class ScraperNoDepletion(unittest.TestCase):
    def setUp(self):
        self.resfile = os.path.join('testing', 'pwrpin300_res.m')
        self.gcu = ('0',)
        self.gcuvals = res_scraper(self.resfile, self.gcu, varlist,
                                   args=args)
        self.goodouts = {'0': {'INF_TOT': (4.96244E-01, 0.00017, 0.00000E+00, 0.0E+00),
                               'INF_FISS': (3.14349E-03, 0.00012, 0.00000E+00, 0.0E+00),
                               'INF_S0': (4.70200E-01, 0.00017, 0.00000E+00, 0.0E+00,
                                          0.00000E+00, 0.0E+00, 0.00000E+00, 0.0E+00)}}

    def test_burnup_variables(self):
        """Make sure the end resulting values are correct"""
        for gcu in self.gcu:
            if gcu in self.gcuvals:
                for var in varlist:
                    if var in self.gcuvals[gcu]:
                        if len(self.goodouts[gcu][var]) == len(self.gcuvals[gcu][var]):
                            if self.gcuvals[gcu][var] is not None:
                                if len(self.goodouts[gcu][var]) == len(self.gcuvals[gcu][var]):
                                    for valindx in range(len(self.goodouts[gcu][var])):
                                        # even values will be actual group constant values, odds are uncertainty
                                        # except for energy widths
                                        msg_ = '[{}][{}][{}] is {} should be {}'. \
                                            format(gcu, var, valindx,
                                                   self.gcuvals[gcu][var][valindx],
                                                   self.goodouts[gcu][var][valindx])
                                        if valindx % 2 == 0:
                                            self.assertAlmostEqual(self.goodouts[gcu][var][valindx],
                                                                   self.gcuvals[gcu][var][valindx],
                                                                   places=7, msg=msg_)
                                        else:
                                            self.assertAlmostEqual(self.goodouts[gcu][var][valindx],
                                                                   self.gcuvals[gcu][var][valindx],
                                                                   places=5, msg=msg_)
if __name__ == '__main__':
    unittest.main()
