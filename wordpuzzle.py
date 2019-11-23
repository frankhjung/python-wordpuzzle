#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Solve 9 Letter Word Puzzle. """

import argparse
import os.path
import sys

import utils.filters as utils

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
        help='dictionary to use in word search (default: dictionary/british)',
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
    PARSER.add_argument('--version', action='version', version=__version__)

    # process command line arguments
    ARGS = PARSER.parse_args()
    PROG = PARSER.prog
    DICTIONARY = ARGS.dictionary

    # check input parameters
    if utils.is_valid_size(ARGS.size):
        SIZE = ARGS.size
    else:
        sys.exit(
            "Invalid size. Expected size in range 1..9, got '{size}'.".format(
                size=ARGS.size))

    if utils.is_valid_mandatory(ARGS.mandatory):
        MANDATORY = ARGS.mandatory.lower()
    else:
        sys.exit(
            "Invalid mandatory character. Expected one alphabetic character, got '{mandatory}'."
            .format(mandatory=ARGS.mandatory))

    if utils.is_valid_letters(ARGS.letters):
        LETTERS = list(ARGS.letters.lower())
    else:
        sys.exit(
            "Invalid letters. Expected 9 alphabetic characters, got '{letters}'."
            .format(letters=ARGS.letters))

    # read words in dictionary and print if valid
    for word in DICTIONARY:
        if utils.is_valid_word(SIZE, MANDATORY, LETTERS, list(word.strip())):
            print(word.strip())
