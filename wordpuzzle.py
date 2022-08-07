#!/usr/bin/env python3
"""
Solve 9 Letter Word Puzzle.
"""

import argparse
import os.path
import sys

from library.filters import is_valid_letters, is_valid_word


def alphabetic_letters(value: str) -> str:
    """Valid only if 9 lowercase alphabetic characters."""
    if not is_valid_letters(value):
        raise argparse.ArgumentTypeError(
            f"'{value}' not 9 lowercase alphabetic characters"
        )
    return value


#
# MAIN
#
if __name__ == "__main__":

    __version__ = "3.2.0"

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
        help="letters to make words, where the mandatory is first letter)",
        type=alphabetic_letters,
        required=True,
    )
    PARSER.add_argument(
        "--version", help="show version", action="version", version=__version__
    )

    # process command line arguments and check they are all valid
    ARGS = PARSER.parse_args()
    SIZE = int(ARGS.size)
    LETTERS = list(ARGS.letters)
    DICT = ARGS.dictionary.read().splitlines()

    # read in dictionary and print word if valid
    list(map(print, filter(lambda word: is_valid_word(SIZE, LETTERS, word), DICT)))
