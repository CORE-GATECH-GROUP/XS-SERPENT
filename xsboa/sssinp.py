"""
sssinp

Andrew Johnson

Module for performing operations on SERPENT input file such as 

#. Obtaining cross section parameters
#. Writing branched outputs

Classes: 

"""
import os.path as path

import xsboa.messages as messages
from xsboa.readparam import readparam


class SSSInput(object):
    """SERPENT input file
    
    Arguments
    
    Attributes
    
    """

    def __init__(self, iname: str, rtype: str, **kwargs):
        self.iname = iname
        params = readparam(iname, args=kwargs)
        if params[0][0] is False:
            messages.fatal('Could not open file {}'.format(iname),
                           'SSSInput()', kwargs)
        self.paramloc = params[0]
        self.nominal = params[1]
        self.branches = params[2]
        self.burnstr = params[3]
        self.exe = params[4]
        self.vars = params[5]
        if rtype == 'p':
            self.children = [iname + '_' + bb for bb in self.branches]
            self.children.append(iname + '_nom')
        elif rtype in ('c', 'x'):
            self.children = [self.make_file('nom', self.nominal)]
            for branch in self.branches:
                self.children.extend(self.make_file(branch,
                                                    self.branches[branch]))

    def __str__(self):
        return "SERPENT input file - {0}".format(self.iname)

    def make_file(self, bname: str, branchparam: dict):
        """Convert the input file a file with the various branched edits
        
        :param bname: Name of the branch
        :param branchparam:  dictionary with the perturbed branched
        parameters as keys and then conditions as values
        :return: name of new file
        """
        newfile = self.iname + '_' + bname
        with open(newfile, 'w') as nn:
            nn.write('/* xsboa: {0}\n'.format(self.iname))
            nn.write('branch: {0}\n'.format(bname))
            nn.write('\n'.join(['{0}: {1}'.format(val, branchparam[val]) for val in branchparam]))
            nn.write('\n*/\n')
            # todo make all the necessary edits to the output file as we go

        return newfile


if __name__ == '__main__':
    tfile = path.relpath('../testing/uo2mox.txt')
    test = SSSInput(tfile, 'c')
