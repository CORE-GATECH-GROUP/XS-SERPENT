"""

test_readparam.py - Testing for the parameter reader function
    
Andrew Johnson

Test should be ran from the same directory as the setup file (home directory)

"""
import os
import unittest

from xsboa import readparam

args = {'quiet': True, 'output': None}


class ReadParam_UO2Mox(unittest.TestCase):
    def setUp(self):
        # Intended outputs
        self.input = os.path.join('testing', 'uo2mox', 'uo2mox.txt')
        self.loc = (0, 17)
        self.nom = {'UO2': {'temp': 900, 'adens': 6.5850E-02},
                    'MOX1': {'temp': 900}, 'MOX2': {'temp': 900},
                    'MOX3': {'temp': 900},
                    'water': {'mdens': 7.088200E-02, 'temp': 600},
                    'burn': 'daystep 1 4 5R5 keep 1 30'}
        self.exe = 'qsub -v INPARG={0} serp.pbs'
        self.branches = {
            'mod_dens': (['water'], 'mdens', [6E-02, 6.5E-02]),
            'uo2_temp': (['UO2'], 'temp', [800., 1100.]),
            'mox_temp': (['MOX1', 'MOX2', 'MOX3'], 'temp', [800., 1100.])
        }
        self.var = ['INF', 'TOX', 'INF_S0']
        self.gcu = ['200']

        # Actual outputs
        self.aloc, self.anom, self.abranches, self.aexe, \
        self.avar, self.agcu = readparam(self.input, args)

    def test_no_file(self):
        """Validate output if the file does not exist."""
        vals = readparam('bad', args)
        self.assertEqual(vals[0], (False, -1))

    def test_no_start(self):
        """Validate output if a file exists but param block start is missing."""
        vals = readparam(os.path.join('testing', 'title.txt'), args)
        self.assertEqual(vals[0], (True, -2))

    def test_no_end(self):
        """Validate output if the file exists but param block end is missing."""
        with open(os.path.join('testing', 'title.txt'), 'r') as title:
            tlines = title.readlines()
        with open(os.path.join('testing', 'title_paramStart.txt'), 'w') as paramStart:
            paramStart.writelines(tlines)
            paramStart.write('/* xsboa start\n')
        vals = readparam(os.path.join('testing', 'title_paramStart.txt'), args)
        os.remove(os.path.join('testing', 'title_paramStart.txt'))
        self.assertEqual(vals[0][1], -1)

    def test_loc(self):
        """Validate location of parameter block - zero indexed."""
        self.assertEqual(self.aloc, self.loc)

    def test_branch(self):
        """Validate branching dictionary."""
        for branch in self.branches:
            with self.subTest(msg='branch {}'.format(branch)):
                self.assertEqual(self.branches[branch], self.abranches[branch])

    def test_exe(self):
        """Validate execution string."""
        self.assertEqual(self.aexe, self.exe)

    def test_nom(self):
        """Validate nominal condition dictionary."""
        for matl in self.nom:
            with self.subTest(msg='nominal material {}'.format(matl)):
                self.assertEqual(self.nom[matl], self.anom[matl])

    def test_var(self):
        """Validate extraction of output variables"""
        self.assertEqual(self.var, self.avar)
