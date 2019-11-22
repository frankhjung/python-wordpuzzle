#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Utilities: Solve 9 Letter Word Puzzle. """


def is_valid(size, mandatory, letters, word):
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