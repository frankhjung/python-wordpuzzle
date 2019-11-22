#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Solve 9 Letter Word Puzzle. """

import argparse
import logging
import os.path
import sys
from utils.filters import is_valid

#
# MAIN
#
if __name__ == '__main__':

    __version__ = '1.0.1'

    # setup command line parser
    PARSER = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        usage='%(prog)s [options]',
        description='Solve 9 letter word puzzle.',
        epilog='© 2019 Frank H Jung mailto:frank.jung@marlo.com.au')
    PARSER.add_argument(
        '-d',
        '--dictionary',
        help='dictionary to use in word search (default: dictionary/british',
        type=argparse.FileType(mode='r', encoding='utf-8'),
        default='dictionary/british')
    PARSER.add_argument('-s',
                        '--size',
                        help='minimum word size (default: 4)',
                        type=int,
                        default=4)
    PARSER.add_argument('-m',
                        '--mandatory',
                        help='mandatory character',
                        required=True)
    PARSER.add_argument('-l',
                        '--letters',
                        help='letters to create words from',
                        required=True)
    PARSER.add_argument('-v',
                        '--verbose',
                        help='verbose output',
                        action='count')
    PARSER.add_argument('--version', action='version', version=__version__)

    # process command line arguments
    ARGS = PARSER.parse_args()
    PROG = PARSER.prog
    VERBOSE = ARGS.verbose
    DICTIONARY = ARGS.dictionary
    SIZE = ARGS.size
    MANDATORY = ARGS.mandatory
    LETTERS = list(ARGS.letters)  # split letters into a list

    # set logging level
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    LOGGER = logging.getLogger(__name__)
    # DEBUG: show runtime variables
    if VERBOSE:
        LOGGER.setLevel(logging.DEBUG)

    # read words in dictionary and print if valid
    COUNT = 0
    for word in DICTIONARY:
        if is_valid(SIZE, MANDATORY, LETTERS, list(word.strip())):
            print(word.strip())
            COUNT += 1

    LOGGER.debug('Program name: %s', PROG)
    LOGGER.debug('Version: %s', __version__)
    LOGGER.debug('Dictionary: %s', DICTIONARY.name)
    LOGGER.debug('Size: %s', SIZE)
    LOGGER.debug('Mandatory: %s', MANDATORY)
    LOGGER.debug('Letters: %s', LETTERS)
    LOGGER.debug('Found %s words', COUNT)
