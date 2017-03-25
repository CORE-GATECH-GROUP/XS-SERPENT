"""

Messages
    - Warnings, Errors, and Status Updates

A. Johnson

Functions:
    - warn: Produce a simple warning message for a thing that denotes inspection
    - fatal: Produce a descriptive fatal error message
    - status: Produce a status update
    -oprint: Print to stdout or write to output file
"""
lineBreak = '-' * 40


def oprint(args, msg):
    """
    Write message to stdout (screen) or append to output file
    :param args: arguments from argparser in main file
        needs args.output
        If args.output is none, print to stdout
        Else, append to file found at args.output
    :param msg: Message to write
    :return: None
    """
    if args.output is None:
        print(msg)
        return None
    else:
        with open(args.output, 'a') as out:
            out.write(msg)
        return None


def status(msg_, verbose_):
    """
    Print a simple status update if verbose parameter is true
    :param msg_: Message
    :param verbose_: Verbose flag (boolean)
    :return: None
    """
    if verbose_:
        print(msg_)
    return None


def warn(msg_, loc_=None):
    """
    Print a warning message
    :param msg_: Message
    :param loc_: Location of the warning message (optional)
    :return: None
    """
    print('Warning: ', msg_)
    if loc_ is not None:
        print(' in ', loc_)
    return None


def fatal(msg_, loc_):
    """
    Print a descriptive message for a fatal error. Cease operation
    :param msg_: Desciptive message about what went wrong
    :param loc_: Function that called this error message
    :return: None
    """
    f_str = 'Error: ' + msg_ + '\n in: ' + loc_
    print(lineBreak + '\n' + f_str + '\n' + lineBreak)
    raise SystemError(f_str)
