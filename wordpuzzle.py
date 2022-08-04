#!/usr/bin/env python3
"""
Solve 9 Letter Word Puzzle.
"""

import argparse
import os.path
import sys
from functools import partial

from library.filters import is_valid_letters, is_valid_word


def arg_test(arg_test_func, param):
    """Test if valid argument.

    Args:
        arg_test_func (func): Function to test argument
        param : Argument to test

    Returns:
        param : the validated argument

    Raises:
        ArgumentTypeError : if argument invalid
    """
    if not arg_test_func(param):
        raise argparse.ArgumentTypeError(f"{param} invalid value")

    return param


#: Validate letters argument
arg_letters = partial(arg_test, is_valid_letters)

#
# MAIN
#
if __name__ == "__main__":

    __version__ = "3.1.1"

    # setup command line parser
    PARSER = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        usage="%(prog)s [options]",
        description="Solve 9 letter word puzzle.",
        epilog="© 2019-2022 Frank Jung mailto:frankhjung@linux.com",
    )
    PARSER.add_argument(
        "-d",
        "--dictionary",
        help="dictionary to use in word search (default: dictionary)",
        type=argparse.FileType(mode="r", encoding="utf-8"),
        default="dictionary",
    )
    PARSER.add_argument(
        "-s",
        "--size",
        help="minimum word size (default: 4). Valid sizes are from 1 to 9.",
        type=int,
        choices=list(range(1, 10)),
        metavar="SIZE",
        default=4,
    )
    PARSER.add_argument(
        "-l",
        "--letters",
        help="letters to create words from (mandatory is first letter)",
        type=arg_letters,
        required=True,
    )
    PARSER.add_argument(
        "--version", help="show version", action="version", version=__version__
    )

    # process command line arguments and check they are all valid
    ARGS = PARSER.parse_args()
    SIZE = int(ARGS.size)
    LETTERS = list(ARGS.letters.lower())
    DICT = ARGS.dictionary.read().splitlines()

    # read in dictionary and print word if valid
    print(
        *list(filter(lambda word: is_valid_word(SIZE, LETTERS, word), DICT)),
        sep="\n",
    )
