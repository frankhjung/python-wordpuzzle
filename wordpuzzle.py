#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Solve 9 Letter Word Puzzle.
"""

import argparse
import os.path
import sys

import utils.filters as utils


def arg_test(test_arg, param):
    """ Test if valid argument. """
    if not test_arg(param):
        raise argparse.ArgumentTypeError("{0} invalid value".format(param))
    return param


def arg_size(size):
    """ Validate size argument. """
    return arg_test(utils.is_valid_size, size)


def arg_mandatory(mandatory):
    """ Validate mandatory argument. """
    return arg_test(utils.is_valid_mandatory, mandatory)


def arg_letters(letters):
    """ Validate letters argument. """
    return arg_test(utils.is_valid_letters, letters)


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
        epilog='© 2019-2020 Frank Jung mailto:frank.jung@marlo.com.au')
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
