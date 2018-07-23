import os
import time
from math import log10

start_time = time.time()

def time_verbose(message, update=False, prefix='', suffix=''):
    """Prints a message with a timestamp. For performance measuring purposes"""
    prefix = "\r\033[K" + prefix
    if update:
        suffix += "\r\033[1A"
    print("{}{:>50} [ {:>10.3f} ]{}".format(
        prefix, message,
        time.time() - start_time,
        suffix))

def output_progress(count, total = 1.0):
    """
    Prints a nice progress bar when doing long computations.

    Parameters
    ----------
    count : float
        Current progress.
    total : float
        Progress when completed. 1 by default.

    Note
    ----
    If total is more than 1, progress is displayed as "X / Y".
    If total is 1, progress is displayed as "XX.XX %"
    """
    p = count / total if total > 0 else 0
    p = min(p, 1)
    columns, _ = os.get_terminal_size(0)
    if total > 1:
        l = int(log10(max(1, total)) + 1)
        columns -= 7 + 2*l
        done = int(columns * p)
        print('\r\033[K[' + '#' * done + ' ' * (columns - done) + ']' +
                ' {:>{}} / {:>{}}'.format(int(count), l, int(total), l),
                end='', flush=True)
    else:
        columns -= 12
        done = int(columns * p)
        print('\r\033[K[' + '#' * done + ' ' * (columns - done) + ']' +
                ' {:>6.2f} %'.format(100 * p),
                end='', flush=True)
<<<<<<< HEAD
=======

def init_progress():
    output_progress(0)

def finalize_progress():
    output_progress(1.0)
    print('')

>>>>>>> 67a3be242b4b13ab9d9da1e2979717acc3b4515c
