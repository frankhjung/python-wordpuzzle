#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utilities: Solve 9 Letter Word Puzzle.
"""


def is_valid_size(size):
    """ Must have size in range from 1 to 9, inclusive. """
    return 1 <= size <= 9


def is_valid_mandatory(mandatory):
    """ Must have 1 alphabetic character. """
    return mandatory.isalpha() and len(mandatory) == 1


def is_valid_letters(letters):
    """ Must have 9 alphabetic characters. """
    return letters.isalpha() and len(letters) == 9


def is_valid_word(size, mandatory, letters, word):
    """ Check that a dictionary word only contains valid letters
        and is of the correct size.
    """
    if size > len(word) or len(word) > 9:
        return False

    if mandatory not in word:
        return False

    # test all letters in word are valid
    working = letters[:]
    for letter in word:
        if letter in working:
            working.remove(letter)
        else:
            return False

    return True
