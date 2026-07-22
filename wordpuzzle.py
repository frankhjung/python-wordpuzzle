#!/usr/bin/env python3
"""
Solve 9 Letter Word Puzzle.
"""

import argparse
import sys
from pathlib import Path

from library.domain import Puzzle, solve


def _get_version_from_pyproject() -> str:
    """Return project version from pyproject.toml."""
    import tomllib

    pyproject_path = Path(__file__).parent / "pyproject.toml"
    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)
        return data.get("project", {}).get("version", "0.0.0")
    except (FileNotFoundError, tomllib.TOMLDecodeError):
        return "0.0.0"


#
# MAIN
#
def main() -> None:
    """Solve the word puzzles from command-line arguments."""
    version = _get_version_from_pyproject()

    # setup command line parser
    parser = argparse.ArgumentParser(
        prog=Path(sys.argv[0]).name,
        usage="%(prog)s [options]",
        description="Solve 9 letter word puzzle.",
        epilog="© 2019-2026 Frank Jung mailto:frankhjung at linux.com",
    )
    parser.add_argument(
        "-d",
        "--dictionary",
        help="dictionary to use in word search (default: dictionary)",
        type=str,
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
    try:
        with Path(args.dictionary).open(encoding="utf-8") as dict_file:
            dictionary = (line.rstrip() for line in dict_file)
            for word in solve(puzzle, dictionary):
                print(word)
    except OSError as e:
        parser.error(f"Cannot open dictionary: {e}")


if __name__ == "__main__":
    main()
