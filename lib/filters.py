#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Library: Solve 9 Letter Word Puzzle.
"""


def is_valid_size(size: int) -> bool:
    """Must have size in range from 1 to 9, inclusive."""
    return 1 <= size <= 9


def is_valid_letters(letters: str) -> bool:
    """Must have 9 alphabetic characters."""
    return letters.isalpha() and len(letters) == 9 and letters.islower()


def is_valid_word(size: int, letters: str, word: str) -> bool:
    """Check that a dictionary word only contains valid letters
    and is of the correct size.

    The mandatory character is chosen as the first letter in the letters
    argument.
    """
    if size > len(word) or len(word) > 9:
        return False

    # mandatory letter must be in word
    if letters[0] not in word:
        return False

    # test all letters in word are valid
    working = letters[:]  # deep copy of str
    return_code = True  # default if loop completes
    for letter in word:
        if letter in working:
            working.remove(letter)
        else:
            return_code = False
    return return_code
