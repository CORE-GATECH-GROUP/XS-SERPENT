"""

m2py
    - Functions to convert strings of MATLAB syntax to python containers

A. Johnson

Functions
    - vec2list: Convert a MATLAB vector to a list

"""
import xsboa.messages as messages


def vec2list(vecstr_, args=None):
    """Convert a MATLAB vector to a list.
     At the moment, works for single line vectors.
     Will add multiline and matrix functionality as needed
    :param vecstr_: String of a MATLAB style vector type:str
    :param args: Additional arguments to pass into fatal for errors
        Fatal requires 'output' key with value of None or string of output file
    :return: List of vector elements
    """
    if '[' not in vecstr_ or ']' not in vecstr_:
        messages.fatal('Could not find complete vector in vec_str:\n' + vecstr_,
                       'vec2list()', args)

    vecstart = vecstr_.index('[')
    vecend = vecstr_.index(']')

    vecsplit = vecstr_[vecstart + 1:vecend].split(' ')
    return [float(v_) for v_ in vecsplit if len(v_) > 1]
