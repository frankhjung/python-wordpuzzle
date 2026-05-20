#!/usr/bin/env python3
"""
Solve 9 Letter Word Puzzle.
"""

import argparse
import os.path
import sys

from library.domain import Puzzle, solve


def _get_version_from_pyproject() -> str:
    """Return project version from pyproject.toml."""
    import tomllib

    pyproject_path = os.path.join(os.path.dirname(__file__), "pyproject.toml")
    try:
        with open(pyproject_path, "rb") as f:
            data = tomllib.load(f)
        return data.get("project", {}).get("version", "0.0.0")
    except (FileNotFoundError, tomllib.TOMLDecodeError):
        return "0.0.0"


#
# MAIN
#
def main() -> None:
    """Solve the 9-letter word puzzle from command-line arguments."""
    version = _get_version_from_pyproject()

    # setup command line parser
    parser = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        usage="%(prog)s [options]",
        description="Solve 9 letter word puzzle.",
        epilog="© 2019-2023 Frank Jung mailto:frankhjung at linux.com",
    )
    parser.add_argument(
        "-d",
        "--dictionary",
        help="dictionary to use in word search (default: dictionary)",
        type=argparse.FileType(mode="r", encoding="utf-8"),
        default="dictionary",
    )
    parser.add_argument(
        "-s",
        "--size",
        help="minimum word size (default: 4). Valid sizes are from 1 to 9.",
        type=int,
        choices=list(range(1, 10)),
        metavar="SIZE",
        default=4,
    )
    parser.add_argument(
        "-l",
        "--letters",
        help="letters to make words, where the mandatory is first letter)",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--version", help="show version", action="version", version=version
    )

    # read command line arguments and check they are all valid
    args = parser.parse_args()

    try:
        puzzle = Puzzle(letters=args.letters, min_size=args.size)
    except ValueError as e:
        parser.error(str(e))

    # read each word from the dictionary and print only valid words
    # Use rstrip() to remove newlines from file iterator
    dictionary = (line.rstrip() for line in args.dictionary)
    for word in solve(puzzle, dictionary):
        print(word)


if __name__ == "__main__":
    main()
