#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solve 9 Letter Word Puzzle.
"""

import argparse
import os.path
import sys
from functools import partial

import utils.filters as utils


def arg_test(arg_test_func, param):
    """ Test if valid argument.

    Args:
        arg_test_func (func): Function to test argument
        param : Argument to test

    Returns:
        param : the validated argument

    Raises:
        ArgumentTypeError : if argument invalid

    """
    if not arg_test_func(param):
        raise argparse.ArgumentTypeError("{0} invalid value".format(param))
    return param


#: Validate size argument
arg_size = partial(arg_test, utils.is_valid_size)

#: Validate mandatory argument
arg_mandatory = partial(arg_test, utils.is_valid_mandatory)

#: Validate letters argument
arg_letters = partial(arg_test, utils.is_valid_letters)

#
# MAIN
#
if __name__ == '__main__':

    __version__ = '1.1.0'

    # setup command line parser
    PARSER = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        usage='%(prog)s [options]',
        description='Solve 9 letter word puzzle.',
        epilog='© 2019-2021 Frank Jung mailto:frank.jung@marlo.com.au')
    PARSER.add_argument(
        '-d',
        '--dictionary',
        help='dictionary to use in word search (default: dictionary)',
        type=argparse.FileType(mode='r', encoding='utf-8'),
        default='dictionary')
    PARSER.add_argument('-s',
                        '--size',
                        help='minimum word size (default: 4)',
                        type=arg_size,
                        default=4)
    PARSER.add_argument('-m',
                        '--mandatory',
                        help='mandatory character',
                        required=True,
                        type=arg_mandatory)
    PARSER.add_argument('-l',
                        '--letters',
                        help='letters to create words from',
                        required=True,
                        type=arg_letters)
    PARSER.add_argument('--version', action='version', version=__version__)

    # process command line arguments and check they are all valid
    ARGS = PARSER.parse_args()
    MANDATORY = ARGS.mandatory.lower()
    LETTERS = list(ARGS.letters.lower())

    # read words in dictionary and print if valid
    for word in ARGS.dictionary:
        if utils.is_valid_word(ARGS.size, MANDATORY, LETTERS, word.strip()):
            print(word.strip())
