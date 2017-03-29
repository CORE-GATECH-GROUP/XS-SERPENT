"""
Messages
    - Warnings, Errors, and Status Updates

A. Johnson

Functions:
    - warn: Produce a simple warning message for a thing that denotes inspection
    - fatal: Produce a descriptive fatal error message
    - status: Produce a status update
    - oprint: Print to stdout or write to output file
"""
lineBreak = '-' * 40


def oprint(msg: str, output):
    """
    Write message to stdout (screen) or append to output file
    :param output: Either file string to append to or None
        If none, print to string
    :param msg: Message to write
    :return: None
    """
    if output is None:
        print(msg)
        return None
    else:
        with open(output, 'a') as out:
            out.write(msg)
        return None


def status(msg_: str, args: dict):
    """
    Print a simple status update if verbose parameter is true
    :param msg_: Message
    :param args: Dictionary of input arguments
        - requires keys 'verbose': Bool and 'output': (None, str)
    :return: None
    """
    if args['verbose']:
        oprint(msg_, args['output'])
    return None


def warn(msg_: str, loc_, args: dict):
    """
    Print a warning message
    :param msg_: Message
    :param loc_: Location of the warning message
    :param args: Dictionary of input arguments
        - Requires key 'output' : (None or file string)
    :return: None
    """
    oprint('Warning: ' + msg_, args['output'])
    if loc_ is not None:
        oprint(' in ' + loc_, args['output'])
    return None


def fatal(msg_, loc_: str, args: dict):
    """
    Print a descriptive message for a fatal error. Cease operation
    :param msg_: Desciptive message about what went wrong
    :param loc_: Function that called this error message
    :param args: Dictionary of input arguments
        - Requires key 'output' : (None or file string)
    :return: None
    """
    f_str = 'Error: ' + msg_ + '\n in: ' + loc_
    oprint(lineBreak + '\n' + f_str + '\n' + lineBreak, args['output'])
    raise SystemError(f_str)
