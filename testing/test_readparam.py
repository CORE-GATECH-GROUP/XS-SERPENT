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


class TestReadParam(unittest.TestCase):
    def setUp(self):
        # Intended outputs
        self.loc = (0, 19)
        self.nom = {'UO2': {'temp': 900, 'adens': 6.5850E-02}, 'MOX1': {'temp': 900}, 'MOX2': {'temp': 900},
                    'MOX3': {'temp': 900},
                    'water1': {'mdens': 7.088200E-02, 'temp': 600}}
        self.exe = 'qsub -v INPARG={} serp.pbs'
        self.branch = {'hUO2': {'UO2': {'temp': 1200}}, 'hFuel': {'UO2': {'temp': 1200}, 'MOX1': {'temp': 1200},
                                                                  'MOX2': {'temp': 1200}, 'MOX3': {'temp': 1200}},
                       'void40b0': {'water1': {'void': 40}, 'burn': 1}}
        self.burn = ['burn 1 4 5R5 keep 1 30', 'burn 1 4 5R5 keep 1 30']

        # Actual outputs
        self.aloc, self.anom, self.obranch, self.aburn, self.aexe = readparam(inpfile, args)

    def test_no_file(self):
        """Validate output if the file does not exist (False, -2)."""
        b_loc, dum1, dum2, dum3, dum4 = readparam('bad', args)
        self.assertEqual(b_loc, (False, -1))

    def test_no_start(self):
        """Vallidate output if a file exists but param block start is missing (True, -2)."""
        b_loc, dum1, dum2, dum3, dum4 = readparam(os.path.join('testing', 'title.txt'), args)
        self.assertEqual(b_loc, (True, -2))

    def test_no_end(self):
        """Validate output if the file exists but param block end is missing (<int>, -1)."""
        with open(os.path.join('testing', 'title.txt'), 'r') as title:
            tlines = title.readlines()
        with open(os.path.join('testing', 'title_paramStart.txt'), 'w') as paramStart:
            paramStart.writelines(tlines)
            paramStart.write('/* xsboa start\n')
        b_loc, dum1, dum2, dum3, dum4 = readparam(os.path.join('testing', 'title_paramStart.txt'), args)
        os.remove(os.path.join('testing', 'title_paramStart.txt'))
        self.assertEqual(b_loc[1], -1)

    def test_loc(self):
        """Validate location of parameter block - zero indexed."""
        self.assertEqual(self.aloc, self.loc)

    def test_burn(self):
        """Validate burnup list."""
        self.assertEqual(self.aloc, self.loc)

    def test_branch(self):
        """Validate branching dictionary."""
        for branch in self.branch:
            with self.subTest(msg='branch {}'.format(branch)):
                self.assertEqual(self.branch[branch], self.obranch[branch])

    def test_exe(self):
        """Validate execution string."""
        self.assertEqual(self.aexe, self.exe)

    def test_nom(self):
        """Validate nominal condition dictionary."""
        for matl in self.nom:
            with self.subTest(msg='nominal material {}'.format(matl)):
                self.assertEqual(self.nom[matl], self.anom[matl])
